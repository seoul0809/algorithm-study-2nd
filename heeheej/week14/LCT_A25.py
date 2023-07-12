# 실패율

# import pprint

def solution(N, stages):
    answer = []
    arr = [0] * (N + 2)  # stage 별 도전 중인 사용자 수를 담은 배열

    for x in stages:
        arr[x] += 1
    total = sum(arr)
    # pprint.pprint(locals())

    for i in range(1, N + 1):
        if total == 0 or arr[i] == 0:
            answer.append((i, 0))
        else:
            answer.append((i, arr[i] / total))
            total -= arr[i]
        # pprint.pprint(locals())
    answer.sort(key=lambda x: (-x[1], x[0]))
    answer = [answer[i][0] for i in range(N)]
    return answer