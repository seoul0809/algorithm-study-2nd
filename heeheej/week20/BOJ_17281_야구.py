# 야구
# 115944kb, 896ms
# 구현 문제
# 타순은 다음 이닝에서 유지되므로 이닝이 끝날 때 타순 몇번째인지 기억해야한다.
# r1, r2, r3 변수를 선수가 있으면 1, 없으면 0으로 해서 score 계산 시 조건문 쓰지 않고 더해주기만 하면 된다.
# 여러 변수에 대해 한 칸씩 값을 옮기고 싶을 때 a, b, c = c, a, b 떠올리기

import sys
from itertools import permutations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board =[list(map(int, input().split())) for _ in range(N)]
combs = permutations([i for i in range(1, 9)], 8)
result = 0
for comb in combs:
    score = 0
    next_k = 0
    for i in range(N): # 이닝별로 반복
        arr = [board[i][comb[j]] for j in range(8)]
        arr = arr[:3] + [board[i][0]] + arr[3:]
        r1, r2, r3 = 0, 0, 0
        out, k = 0, next_k
        while out < 3:
            x = arr[k]
            if x == 0:
                out += 1
            elif x == 1:
                score += r3
                r1, r2, r3 = 1, r1, r2
            elif x == 2:
                score += (r2 + r3)
                r1, r2, r3 = 0, 1, r1
            elif x == 3:
                score += (r1 + r2 + r3)
                r1, r2, r3 = 0, 0, 1
            elif x == 4:
                score += (1 + r1 + r2 + r3)
                r1, r2, r3 = 0, 0, 0
            k += 1
            k %= 9
        next_k = k

    result = max(result, score)
print(result)