def reopen(trajectory, new_states):
    extension = []
    start = len(trajectory)
    for offset, state in enumerate(new_states):
        extension.append({'state': state, 'transform': None, 'index': start + offset})
    return trajectory + extension
