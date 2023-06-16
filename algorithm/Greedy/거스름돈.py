"""거스름돈의 최소 개수 구하기"""
n = 1260
count = 0

coin_t = [500, 100, 50, 10]
for c in coint_t:
  count += n // c
  n %= c

print(count)
