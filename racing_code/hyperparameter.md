# 환경 파라미터 (Environment Parameters)

| **파라미터 이름**        | **설명** |
|--------------------------|----------|
| all_wheels_on_track      | 차량의 모든 바퀴가 트랙 위에 있는지 여부 (True / False) |
| x                        | 차량의 현재 X 좌표 (float) |
| y                        | 차량의 현재 Y 좌표 (float) |
| closest_objects          | 트랙 상에서 가장 가까운 두 개의 장애물 인덱스 (리스트) |
| closest_waypoints        | 현재 위치에서 가장 가까운 두 개의 웨이포인트 인덱스 (리스트) |
| distance_from_center     | 트랙 중앙으로부터 차량의 거리 (float) |
| is_crashed               | 차량이 충돌했는지 여부 (True / False) |
| is_left_of_center        | 차량이 트랙 중앙 기준 왼쪽에 위치하는지 여부 (True / False) |
| is_offtrack              | 차량이 트랙을 이탈했는지 여부 (True / False) |
| is_reversed              | 차량이 역방향으로 주행 중인지 여부 (True / False) |
| heading                  | 차량의 현재 진행 방향 각도 (float, 단위: degree) |
| progress                 | 트랙 주행 진행률 (%) (float, 0~100) |
| speed                    | 현재 속도 (float, 단위: m/s) |
| steering_angle           | 현재 조향(핸들) 각도 (float, 단위: degree) |
| steps                    | 현재까지 실행된 스텝 수 (int) |
| track_length             | 전체 트랙 길이 (float, 단위: m) |
| track_width              | 트랙의 너비 (float, 단위: m) |
| waypoints                | 트랙의 모든 웨이포인트 좌표 (리스트, [x, y] 형식) |
<br>
# 하이퍼파라미터 (Hyperparameters)

| **파라미터 이름**             | **설명** |
|-------------------------------|----------|
| learning_rate                 | 학습 속도 (모델이 얼마나 빠르게 학습할지 결정) |
| batch_size                    | 한 번에 학습할 데이터 묶음의 크기 |
| num_epochs                    | 동일한 데이터를 몇 번 반복해서 학습할지 |
| entropy                       | 정책의 랜덤성 조절 (탐험 vs. 익숙한 행동) |
| discount factor (γ)           | 미래 보상을 현재 가치에 얼마나 반영할지 결정 |
| epsilon                       | 초기 탐험 비율 (처음에 얼마나 랜덤하게 행동할지) |
| epsilon decay                 | 탐험 비율 감소 속도 |
| clipping parameter            | 정책 업데이트 시 변화 폭 제한 (학습 안정성 확보) |
| lambda                        | 일반적으로 계산 안정성을 위한 보조 파라미터 |
| loss type                     | 사용되는 손실 함수의 종류 |
| policy updating iteration     | 정책 업데이트를 수행하는 반복 횟수 |
| num_episodes                  | 전체 학습 반복 횟수 (에피소드 수) |
