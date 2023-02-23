# A -> B
# 160ms, 116636kb
# bfs 이용

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def bfs(x):
    queue = deque()
    queue.append((1, x))

    while queue:
        n, a = queue.popleft()
        for ax in [int(str(a)+"1"), a*2]:
            if ax == B:
                return n + 1
            elif ax < B:
                queue.append((n + 1, ax))
    return -1

A, B = map(int, input().split())
print(bfs(A))