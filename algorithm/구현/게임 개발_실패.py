"""게임 개발, page 118"""
## 좌표 지정 -> 리스트 컴프리헨션
## 움직임 좌표 설정 -> 좌표값 선지정
## 캐릭터의 움직임(왼쪽 회전)에 대한 함수 설정

N, M = map(int, input().split())
A, B, d = map(int, input().split())

# N행 M열 생성
mat = [[0] * M for _ in range(N)]

for idx in range(N):
  mat[idx] = list(map(int, input().split()))

print(mat)

# 북, 동, 남, 서에 대한 좌표 설정
ax = [0, -1, 0, 1]
ay = [-1, 0, 1, 0]

# 갔던 곳 저장
# place = []
# place.append((A, B))


# 좌회전 함수
def turn_left(A, B):
  global d
  A = A + ax[d]
  B = B + ay[d]
  if d == 3:
    d = 0
  else:
    d += 1
  return A, B


# 회전 가능성 확인
def change_prob(A, B):
  a, b = turn_left(A, B)
  if (mat[a][b] == 1):
    return False
  else:
    return True


count = 0
null_count = 0
while True:
  if change_prob(A, B):
    print(A, B)
    mat[A][B] = 1
    A, B = turn_left(A, B)
    # place.append((A, B))
    count += 1
    null_count = 0
    print("#", mat)
    if count == 3:
      break
  else:
    null_count += 1
    if d == 3:
      d = 0
    else:
      d += 1

  if null_count == 4:
    break

print(count)
