# 여행경로
# 프로그래머스 코딩테스트 고득점 kit > bfs/dfs
# 1218 (+12)
# 큐에 (현재까지 경로, 남은 티켓 리스트)를 튜플로 넣어서 bfs

from collections import deque
def solution(tickets):
    answer = []
    tickets.sort(key = lambda x: (x[0], x[1]))
    
    def bfs(start):
        q = deque()
        q.append(([start], tickets))
        nonlocal answer
        
        while q:
            path, remains = q.popleft()
            if len(remains) == 0:
                answer = path
                return
            now = path[-1]
            for i, remain in enumerate(remains):
                a, b = remain[0], remain[1]
                if a == now:
                    q.append((path + [b], remains[:i]+remains[i+1:]))
    bfs("ICN")
    return answer