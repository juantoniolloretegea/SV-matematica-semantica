def evaluate_boundary(classification):
    if classification and all(c == 1 for c in classification):
        return 'CERRABLE'
    if any(c == 0 for c in classification):
        return 'NO_CERRABLE'
    return 'ABIERTA'
