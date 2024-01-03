# A와 B 2
# S에서 T를 만드는게 아니라, T에서 S를 만드는 방식으로 접근
# 108080kb, 108ms

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

S = input().rstrip()
T = input().rstrip()

def task(t):
    if S == t:
        print(1)
        exit()
    elif len(t) <= len(S):
        return
    
    if t[-1] == 'A':
        task(t[:len(t)-1])
    if t[0] == 'B':
        t = t[::-1]
        t = t[:len(t)-1]
        task(t)

task(T)
print(0)