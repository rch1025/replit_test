"""시각, page 113"""
# 다음에는 for문으로 풀어보기
# 5959에서 줄여나가기
N = int(input())
count = 0

while N != -1:
  min = 59
  while min != -1:
    sec = 59
    while sec != -1:
      if ('3' in str(sec)) or ('3' in str(min)) or ('3' in str(N)):
        count += 1
      sec -= 1
    min -= 1
  N -= 1

print(count)