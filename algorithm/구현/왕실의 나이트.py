"""왕실의 나이트, page 115"""
# ord()를 사용해서 풀어보기
night_state = input()

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
move_plan = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2],
             [-1, -2]]

row = dict1[night_state[0]]
col = int(night_state[1])

count = 0
for idx in move_plan:
  if (row + idx[0] >= 1) & (row + idx[0] <= 8) & (col + idx[1] <=
                                                  8) & (col + idx[1] >= 1):
    count += 1

print(count)
