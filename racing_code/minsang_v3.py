def reward_function(params):
    base_reward = 1.0  # 기본값

    # 파라미터 추출
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    raw_steering_angle = params['steering_angle']
    steering_angle = abs(raw_steering_angle)
    speed = params['speed']
    all_wheels_on_track = params['all_wheels_on_track']
    is_left_of_center = params['is_left_of_center']
    is_right_of_center = not is_left_of_center
    progress = params['progress']
    is_offtrack = params.get('is_offtrack', False)
    wheels_off_track = params.get('wheels_off_track', 0)
    
    marker_2 = 0.25 * track_width

    # [전략 1] 우측 주행
    if distance_from_center <= marker_2 and is_right_of_center:
        base_reward += 0.2

    # [전략 2] 방향별 코너링
    if raw_steering_angle > 10 and is_right_of_center:
        base_reward += 0.3
    elif raw_steering_angle < -10 and is_left_of_center:
        base_reward += 0.3

    # [전략 3] 속도 관리 (직선/코너)
    if steering_angle < 10:
        if speed > 3.0:
            base_reward += 3.0
        else:
            base_reward += speed
    else:
        if speed > 2.0:
            base_reward -= 0.5  # 과속 코너링 감점
        else:
            base_reward += 0.5  # 저속 코너링 보상

    # [전략 4] 이탈 패널티
    if not all_wheels_on_track:
        if is_offtrack:
            base_reward = 1e-3  # 완전 이탈 최소 보상
        elif wheels_off_track >= 3:
            base_reward -= 0.8  # 큰 감점
        elif wheels_off_track >= 1:
            base_reward -= 0.5  # 중간 감점
    else:
        base_reward += progress * 0.1

    # 보상은 최소 1e-3 이상으로 클램프
    final_reward = max(base_reward, 1e-3)

    return float(final_reward)
