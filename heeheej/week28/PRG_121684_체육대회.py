# PCCP 모의고사 1 2번 체육대회
# dfs + 백트래킹

def solution(ability):
    answer = 0
    new = []
    N = len(ability)    # 학생수
    M = len(ability[0]) # 종목 개수
    
    for j in range(M):
        arr = []
        for i in range(N):
            arr.append((ability[i][j], i))
        arr.sort(key = lambda x:-x[0])
        new.append(arr)
    visited = [False]*N

    def dfs(i, a_sum):
        if i == M:
            nonlocal answer
            answer = max(answer, a_sum)
            return
        
        for j in range(N):
            a, idx = new[i][j]
            if not visited[idx]:
                visited[idx] = True
                dfs(i+1, a_sum + a)
                visited[idx] = False

    dfs(0, 0)
    
    return answer