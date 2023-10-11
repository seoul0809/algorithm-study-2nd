# 괄호의 값
# 구현 문제
# 첫번째 포인트는 열린괄호일때 곱하기, 닫힌괄호일때 나누기를 해주는 것.
# 두번째 포인트는 어느 시점에 더하기를 해주느냐? 였는데 생각하기가 어려웠다. 
# 닫힌 괄호를 만났으며 직전괄호가 현재 괄호와 쌍을 이루는 열린 괄호일 때, 덧셈을 해주면 된다. 
# 열린 괄호를 만나면 곱하기+스택에 push, 
# 닫힌 괄호를 만나면 (나누기, stack에서 pop, 
# 만약 이전 괄호와 쌍을 이룬다면 지금까지의 temp를 result에 더하기)를 해준다.
# (()[[]])([])의 경우, (2+3*3)*2 + 3*2 
# 괄호 속을 먼저 계산하는 것이 아니라 풀어서 계산한다고 생각해야한다.
# 즉, 2*2 + 2*3*3 + 2*3으로 생각해야함
# 위의 예제에서 (() 후에 [가 왔을 때, temp에 2가 남아 있고 temp에 *3을 해주게 됨

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

arr = list(input())
result = 0
temp = 1
stack = []
for i, v in enumerate(arr):
    if v == "(":
        temp *= 2
        stack.append(v)
    elif v == "[":
        temp *= 3
        stack.append(v)
    elif v == ")":
        if not stack or stack[-1] == "[":
            result = 0
            break
        elif arr[i-1] == "(":
            result += temp
        stack.pop()
        temp //= 2
    elif v == "]":
        if not stack or stack[-1] == "(":
            result = 0
            break
        elif arr[i-1] == "[":
            result += temp
        stack.pop()
        temp //= 3
if stack:
    print(0)
else:
    print(result)
