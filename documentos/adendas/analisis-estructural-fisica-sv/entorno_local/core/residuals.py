def compute_residuals(trajectory):
    residuals = []
    for i in range(len(trajectory) - 1):
        a = trajectory[i]['state']
        b = trajectory[i + 1]['state']
        if a is None or b is None or a == 'U' or b == 'U':
            residuals.append('U')
        elif a == b:
            residuals.append(0)
        else:
            residuals.append(1)
    return residuals
