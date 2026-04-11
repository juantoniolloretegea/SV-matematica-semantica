def build_trajectory(states, transforms=None):
    transforms = transforms or []
    trajectory = []
    for i, state in enumerate(states):
        trajectory.append({
            'state': state,
            'transform': transforms[i] if i < len(transforms) else None,
            'index': i
        })
    return trajectory
