"""게임 개발, page 118"""
# 왼쪽 방향으로 회전한 다음에 이동함
# 가본 곳과 아닌 곳을 확인하는 map_이 필요함
# 바다와 육지를 입력 받는 place가 필요함

N, M = map(int, input().split())

# 게임 캐릭터가 있는 좌표 입력
A, B, d = map(int, input().split())

# 방향에 따른 좌표 값 설정
ax = [-1, 0, 1, 0]
ay = [0, 1, 0, -1]

# place: 육지와 바다 지도
place = []
for _ in range(N):
  place.append(list(map(int, input().split())))

# map_: 사용자가 갔던 곳 표시
map_ = [[0] * M for _ in range(N)]
map_[A][B] = 1  # 현재 위치는 갔다고 지정


# 왼쪽 회전에 대한 함수 정의
def turn_left():
  global d
  if d == 0:
    d = 3
  else:
    d -= 1  # 왼쪽으로 돌아야 하기 때문에 -1을 해줌


# 캐릭터가 방문한 칸의 개수 (현재 칸을 포함해야 함)
count = 1
# 왼쪽으로 몇 번 돌았는가?
left_count = 0

while True:
  turn_left()
  An = A + ax[d]
  Bn = B + ay[d]
  if (map_[An][Bn] == 0) and (place[An][Bn] == 0):
    A = An
    B = Bn
    map_[A][B] = 1
    count += 1
    left_count = 0
    continue
  else:
    left_count += 1

  if left_count == 4:
    An = A - ax[d]
    Bn = B - ay[d]
    if place[An][Bn] != 1:
      A = An
      B = Bn
      if map_[A][B] != 1:
        count += 1
      left_count = 0
    else:
      break

print(count)
