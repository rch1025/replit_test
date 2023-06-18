"""상하좌우 복습, page 110"""
# dict 형태의 직접적인 좌표값 말고, 다른 형태로 구성해보자
N = int(input())
A = list(input().split())

dict1 = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
start_point = [1, 1]
for idx in A:
  row, col = dict1[idx]
  if (start_point[0] + row < 1) or (start_point[0] + row > N) or (
      start_point[1] + col < 1) or (start_point[1] + col > N):
    pass
  else:
    start_point = [start_point[0] + row, start_point[1] + col]

print(start_point)
