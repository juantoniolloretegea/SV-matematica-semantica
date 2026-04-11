def compute_verdict(boundary):
    if boundary == 'CERRABLE':
        return 'APTO'
    if boundary == 'NO_CERRABLE':
        return 'NO APTO'
    return 'INDETERMINADO'
