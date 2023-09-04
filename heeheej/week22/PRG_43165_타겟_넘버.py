# 타겟 넘버
# 프로그래머스 코딩테스트 고득점 kit > dfs/bfs
# 1189 (+1)
# dfs
# 중첩함수(함수 안의 함수) 사용 시 nonlocal 선언해주어 바깥에 있는 함수의 변수를 쓴다

def solution(numbers, target):
    answer = 0
    
    def dfs(depth, result, arr, target):
        if depth == len(arr):
            if result == target:
                nonlocal answer
                answer += 1
            return
        dfs(depth + 1, result + arr[depth], arr, target)
        dfs(depth + 1, result - arr[depth], arr, target)

    dfs(0, 0, numbers, target)
    
    return answer

# 아래는 중첩함수 안쓴버전

# answer = 0

# def dfs(depth, result, arr, target):
#     if depth == len(arr):
#         if result == target:
#             global answer
#             answer += 1
#         return
#     dfs(depth + 1, result + arr[depth], arr, target)
#     dfs(depth + 1, result - arr[depth], arr, target)

# def solution(numbers, target):
#     global answer
    
#     dfs(0, 0, numbers, target)
    
#     return answer