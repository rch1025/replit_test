"""게임 개발, page 118"""
## 빈 좌표 설정 -> 리스트 컴프리헨션 -> 갔던 곳 저장
## 입력 좌표 확인
## 움직임 좌표 설정 -> 좌표값 선지정
## 캐릭터의 움직임(왼쪽 회전)에 대한 함수 설정

N, M = map(int, input().split())
A, B, d = map(int, input().split())

# map 입력
map_ = []
for i in range(N):
  map_.append(list(map(int, input().split())))

# 갔던 곳을 기억하기 위한 좌표 설정
place = [[0] * M for _ in range(N)]
place[A][B] = 1  # 처음 서있는 위치에 1 지정

ax = [-1, 0, 1, 0]
ay = [0, 1, 0, -1]


# 왼쪽 전환 함수
def turn_left():
  global d
  if d == -1:
    d = 3
  else:
    d -= 1


count = 1  # 첫 자리 1
count_non = 0
while True:
  turn_left()
  An = A + ax[d]
  Bn = B + ay[d]
  print(An, Bn)
  if place[An][Bn] == 0 and map_[An][Bn] == 0:
    place[An][Bn] = 1
    A = An
    B = Bn
    count_non = 0  # 회전 후 이동이 가능하다면 count_non = 0
    count += 1
    continue  # 바로 다음 반복으로 넘어감
  else:
    count_non += 1  # 회전이 불가능하면 count_non += 1

  if (count_non == 4):
    An = A - ax[d]
    Bn = B - ay[d]
    if map_[An][Bn] == 0:
      A = An
      B = Bn
    else:
      break
    count_non = 0

print(count)
