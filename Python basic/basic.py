"""리스트 초기화"""
n = 10
a = [0] * n
print("리스트 초기화 :", a)


"""리스트 컴프리헨션"""
a = [i for i in range(20) if i//2==1]
print("리스트 컴프리헨션 :", a)

## NxM 크기의 행렬 0으로 초기화 => 2차원 리스트를 초기화 할 때는 반드시 리스트 컴프리헨션을 사용해야 한다.
N = 3
M = 4
a = [[0]*M for _ in range(N)]
print('행렬 초기화 :', a)


"""readline() : 입력 빠르게 받기"""
# sys 라이브러리
# input() 보다 입력이 훨씬 빠름
# rstrip(): 엔터가 줄 바꿈 기호인 readline()에서 공백을 없애주기에 필수적으로 사용해야 함
import sys
data = sys.stdin.readline().rstrip()
print(data)