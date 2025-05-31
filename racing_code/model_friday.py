def reward_function(params):
    reward = 1e-3

    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering_angle = params['steering_angle']
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']

    marker_1 = 0.25 * track_width

    # 1
    if distance_from_center <= marker_1 and not is_left_of_center:
        reward *= 1.02

    # 2
    if steering_angle > 10 and distance_from_center <= marker_1 and is_left_of_center:
        reward *= 1.03

    # 3
    if not all_wheels_on_track:
        return 1e-3
    else:
        reward = reward + (params['progress'])

    # 4
    if speed < 0.70:
        reward *= 0.90
    elif speed < 1.30:
        reward *= 0.80
    elif speed >= 1.30 and speed <= 2.40:
        reward += speed
    else:
        reward = speed * speed + reward

    return float(reward)
