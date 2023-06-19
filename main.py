"""게임 개발, page 118"""
import sys

N, M = map(input().split())
A, B, d = map(input().split())

# 이미 왔다간 좌표를 문자열로 저장?
matrix = [sys.stdin.readline().rstrip() for _ in range(N)]

# 북동남서 방향으로 작성
ax = [-1, -1, 1, 1]

while True:
  if (d == 0) and (matrix[A, B + ax[d]] == 0):
    B += ax[d]
    d += 1
  elif (d == 1) and (matrix[A + ax[d], B] == 0):
    A += ax[d]
    d += 1
  elif (d == 2) and (matrix[A, B + ax[d]] == 0):
    B += ax[d]
    d += 1
  elif (d == 2) and (matrix[A + ax[d], B] == 0):
    A += ax[d]
    d = 1
