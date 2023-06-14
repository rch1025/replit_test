"""
<큰 수의 법칙>
page: 92
"""
N, M, K = map(int, input().split())
# 5 8 3
num_array = list(map(int, input().split()))
# 2 4 5 4 6
max_n = max(num_array)
num_array.remove(max_n)
max_n2 = max(num_array)

sum_n = 0
i = 0
while i < M:
  print('#', i)
  for _ in range(K):
    sum_n += max_n
    i += 1
    if i >= M:
      break
  sum_n += max_n2
  i += 1

print(sum_n)
