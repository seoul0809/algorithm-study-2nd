# 피로도
# 프로그래머스 코딩테스트 고득점 kit > 완전탐색
# 1277 (+7)
# 순열 완전탐색

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    N = len(dungeons)
    arr = [i for i in range(N)]
    perms = permutations(arr, N)
    for perm in perms:
        temp = k
        cnt = 0
        for i in perm:
            x, y = dungeons[i]
            if x > temp:
                break
            else:
                temp -= y
                cnt += 1
        answer = max(answer, cnt)
    return answer