# 네트워크
# 프로그래머스 코딩테스트 고득점 kit > bfs/dfs
# 1194 (+4)
# bfs

from collections import deque

def bfs(start, visited, computers):
    q = deque()
    q.append(start)
    visited[start] = True
    n = len(visited)
    while q:
        x = q.popleft()
        arr = computers[x]
        for i in range(n):
            if i == x:
                continue
            if arr[i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            bfs(i, visited, computers)
            answer += 1
    return answer