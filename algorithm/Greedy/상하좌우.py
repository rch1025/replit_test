"""상하좌우 page 110"""
N = int(input())
plan = list(input().split())

matrix = [[1 for _ in range(N)] for _ in range(N)]
i = 0
j = 0
for move in plan:
  if (move == 'L') & (j != 0):
    j -= 1
  elif (move == 'R') & (j != N - 1):
    j += 1
  elif (move == 'U') & (i != 0):
    i -= 1
  elif (move == 'D') & (i != N - 1):
    i += 1
print(i + 1, j + 1)
