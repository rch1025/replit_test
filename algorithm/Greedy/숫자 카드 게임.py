"""숫자 카드 게임: page 96"""
N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

small_num = []
for idx in range(N):
  small_num.append(min(mat[idx]))

final = max(small_num)
print(final)
