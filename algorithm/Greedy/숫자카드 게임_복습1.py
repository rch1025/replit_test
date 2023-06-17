"""숫자 카드 게임: page 96"""
N, M = map(int, input().split())

result = 0
for _ in range(N):
  ll = list(map(int, input().split()))
  if result < min(ll):
    result = min(ll)
print(result)
