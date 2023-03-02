# 제로
# 144ms, 118100kb
# 그냥 스택

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

K = int(input())
stack = list()
for _ in range(K):
    n = int(input())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)
print(sum(stack))