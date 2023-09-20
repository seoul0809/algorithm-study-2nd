# 같은 숫자는 싫어
# 프로그래머스 코딩테스트 고득점 kit > 스택/큐
# 1233 (+2)
# 스택, 큐 활용
# 큐로 굳이 안바꿔도 속도는 비슷하다..

from collections import deque

def solution(arr):
    answer = []
    q = deque(arr)
    
    for x in q:
        if len(answer) != 0 and x != answer[-1]:
            answer.append(x)
        elif len(answer) == 0:
            answer.append(x)
    answer = list(answer)
    return answer