# 최소직사각형
# 프로그래머스 코딩테스트 고득점 kit > 완전탐색
# 1219 (+1)
# w, h 중 큰 값은 max_list 작은 값은 min_list에 담는다.
# 두 개의 리스트에서 가장 큰 값을 곱한 값이 정답

def solution(sizes):
    answer = 0
    max_list, min_list = [], []
    for x, y in sizes:
        if x >= y:
            max_list.append(x)
            min_list.append(y)
        else:
            max_list.append(y)
            min_list.append(x)
    answer = max(max_list)*max(min_list)
    return answer