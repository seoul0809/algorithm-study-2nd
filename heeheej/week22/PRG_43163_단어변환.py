# 단어 변환
# 프로그래머스 코딩테스트 고득점 kit > bfs/dfs
# 1197 (+3)
# bfs 이용해서 현재 단어와 다음 단어 한자씩 비교, 글자 한개만 다를 경우에만 큐에 넣어준다.
# 단, 큐에 넣기 직전에 target과 같으면 return 단계수 해준다.

from collections import deque

def solution(begin, target, words):
    answer = 0
    
    if not target in words:
        return 0
    
    N = len(words)
    visited = [False]*N
    L = len(words[0])
    
    def bfs(begin, target, words):
        q = deque()
        q.append((list(begin), 0))
        while q:
            word, depth = q.popleft()
            for i in range(N):
                if not visited[i]:
                    next = words[i]
                    flag1, flag2 = False, False
                    for j in range(L):
                        if word[j] != next[j]:
                            if not flag1:
                                flag1 = True
                            else:
                                flag2 = True
                                break
                    if flag1 and not flag2:
                        if next == target:
                            return depth + 1
                        q.append((next, depth+1))
                        visited[i] = True
        return 0
        
    answer = bfs(begin, target, words)
    return answer