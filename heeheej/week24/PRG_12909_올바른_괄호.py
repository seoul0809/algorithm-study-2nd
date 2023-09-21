# 올바른 괄호
# 프로그래머스 코딩테스트 고득점 kit > 스택/큐
# 1237 (+4)
# "("일 경우 스택에 넣고 ")"일 경우 스택에서 뺸다.
# 스택이 비었는데 ")"가 나왔을 경우에 False,
# 반복문을 다 돌고나서 스택에 남은 것이 있다면 False

def solution(s):
    answer = True
    
    stack = []
    for x in s:
        if x == "(":
            stack.append(x)
        elif stack:
            stack.pop()
        else:
            answer = False
            break
    if stack:
        answer = False
    return answer