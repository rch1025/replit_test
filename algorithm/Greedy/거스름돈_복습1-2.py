"""거스름돈 문제 복습 -> 처음과 다른 방향으로 풀어보기"""
N, M, K = map(int, input().split())
number = list(map(int, input().split()))
# K는 항상 M보다 작거나 같음
# number는 N개를 가지고 있어야 함

max1 = max(number)
number.remove(max1)
max2 = max(number)

list_ = [max1 for _ in range(K)]
list_.append(max2)

sum_ = 0
idx = 0
while True:
  for num in list_:
    sum_ += num
    idx += 1
    if idx == M:
      break
  if idx == M:
    break
print(sum_)