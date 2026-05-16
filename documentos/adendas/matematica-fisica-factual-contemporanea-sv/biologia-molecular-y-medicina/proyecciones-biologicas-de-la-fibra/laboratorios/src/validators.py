from pathlib import Path
from .io_utils import read_csv

COMMON_REQUIRED = ['id_banco','id_caso','dominio','observable','senal','unidad_externa','primitivo_sv','transductor','canal','diccionario','condicion','estado_condicion','residual','retorno','salida_esperada','negativo_principal','estado_esperado','error_codigo','anchor','critico']
VALID_STATES = {'PASS','FAIL','U','NO_APTO'}
VALID_COND = {'0','1','U'}

class ValidationError(Exception):
    pass

def fail(message):
    raise ValidationError(message)

def require(condition, message):
    if not condition:
        fail(message)

def load_bank(data_dir, filename):
    rows = read_csv(Path(data_dir) / filename)
    require(rows, f'banco vacío: {filename}')
    cols = set(rows[0].keys())
    missing = [c for c in COMMON_REQUIRED if c not in cols]
    require(not missing, f'{filename} sin columnas obligatorias: {missing}')
    return rows

def validate_rows(rows, filename):
    ids = set()
    for r in rows:
        rid = r.get('id_caso','')
        require(rid and rid not in ids, f'id ausente o duplicado en {filename}: {rid}')
        ids.add(rid)
        for key in COMMON_REQUIRED:
            # error_codigo can be empty for positive rows; anchor can be empty in non-public rows only if not critical.
            if key in {'error_codigo','anchor'}:
                continue
            require(str(r.get(key,'')).strip() != '', f'campo vacío en {filename}:{rid}:{key}')
        require(r['estado_condicion'] in VALID_COND, f'estado_condicion inválido {filename}:{rid}')
        require(r['estado_esperado'] in VALID_STATES, f'estado_esperado inválido {filename}:{rid}')
    return True

def validate_registry(data_dir):
    reg = read_csv(Path(data_dir) / 'registro_bancos.csv')
    require(len(reg) == 11, f'registro debe contener 11 bancos, contiene {len(reg)}')
    seen = set()
    for r in reg:
        require(r['id_banco'] not in seen, f'id_banco duplicado {r["id_banco"]}')
        seen.add(r['id_banco'])
        require((Path(data_dir)/r['fichero']).exists(), f'fichero de banco ausente {r["fichero"]}')
    return reg

def validate_error_catalog(data_dir):
    errors = read_csv(Path(data_dir) / 'catalogo_errores.csv')
    require(len(errors) == 48, f'catálogo de errores debe tener 48 entradas, contiene {len(errors)}')
    codes = [e['codigo'] for e in errors]
    require(len(codes) == len(set(codes)), 'códigos de error duplicados')
    require(codes[0] == 'E-01' and codes[-1] == 'E-48', 'rango de errores no canónico')
    return errors

def validate_labs_catalog(data_dir):
    labs = read_csv(Path(data_dir) / 'catalogo_laboratorios.csv')
    require(len(labs) == 54, f'catálogo de laboratorios debe tener 54 entradas, contiene {len(labs)}')
    ids = [l['id_lab'] for l in labs]
    require(len(ids) == len(set(ids)), 'laboratorios duplicados')
    require(ids[0] == 'LAB-01' and ids[-1] == 'LAB-54', 'rango de laboratorios no canónico')
    return labs

def has_error(negative_rows, code):
    return any(r.get('error_codigo') == code and r.get('estado_esperado') == 'FAIL' for r in negative_rows)

def rows_with_state(rows, state):
    return [r for r in rows if r.get('estado_esperado') == state]

def check_no_empty_unit_primitive(rows):
    for r in rows:
        if r.get('critico') == '1':
            require(r.get('unidad_externa','').strip(), f'unidad ausente {r.get("id_caso")}')
            require(r.get('primitivo_sv','').strip(), f'primitivo ausente {r.get("id_caso")}')
    return True

def check_returns(rows):
    for r in rows:
        require(r.get('retorno','').strip(), f'retorno ausente {r.get("id_caso")}')
        require(r.get('residual','').strip(), f'residual ausente {r.get("id_caso")}')
    return True

def check_u_preserved(rows):
    u = [r for r in rows if r.get('estado_esperado') == 'U' or r.get('estado_condicion') == 'U']
    require(u, 'no hay U legítimos para conservar')
    for r in u:
        require(r.get('estado_esperado') == 'U', f'U degradada en {r.get("id_caso")}')
    return True
