# A -> B
# 113112kb, 112ms
# top - down 방식으로 풀기!
# 거꾸로 생각해보자! B에서 A를 만들어보자.

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

A, B = map(int, input().split())
cnt = 1
x = B
while True:
    if x % 10 == 1: # 일의자리수가 1이면 맨 오른쪽에 붙은 1 떼기
        x //= 10
    elif x % 2 == 0:    # 윗 연산을 못했는데 짝수라면 2로 나누기
        x //= 2
    else:   # 둘 다 안되는 경우, 만들 수 없는 경우가 된다.
        print(-1)
        break

    if x == A:
        print(cnt + 1)
        break
    elif x < A:
        print(-1)
        break
    else:
        cnt += 1