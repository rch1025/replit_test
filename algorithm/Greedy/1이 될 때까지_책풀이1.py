"""1이 될 때까지, page 98"""
## N이 1이 되기까지 1번과 2번의 과정을 최소로 몇 번 거쳐야 하는가?
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.

## K로 최대한 많이 나누어 주는 게 N을 빠르게 1로 도달시키는 방법이다.
N, K = map(int, input().split())

result = 0
while N >= K:
  # N이 K로 나누어 떨어지지 않는다면 N에서 1씩 빼기
  while N % K != 0:
    N -= 1
    result += 1
  N //= K
  result += 1

while N != 1:
  N -= 1
  result += 1

print(result)
