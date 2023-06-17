"""1이 될 때까지, page 98"""
## N이 1이 되기까지 1번과 2번의 과정을 최소로 몇 번 거쳐야 하는가?
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다.

N, K = map(int, input().split())
i = 0
while N != 1:
  i += 1
  if N % K == 0:
    N = N // K
  else:
    N -= 1
print(i)