"""거스름돈 문제 복습"""
N, M, K = map(int, input().split())
number = list(map(int, input().split()))
# K는 항상 M보다 작거나 같음
# number는 N개를 가지고 있어야 함

max1 = max(number)
number.remove(max1)
max2 = max(number)

i = 0
sum_ = 0
while True:
  for _ in range(K):
    sum_ += max1
    i += 1
    if i == M:
      break
  sum_ += max2
  i += 1
  if i == M:
    break
print(sum_)
