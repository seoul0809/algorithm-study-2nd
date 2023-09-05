# K번째수
# 프로그래머스 코딩테스트 고득점 kit > 정렬
# 1190 (+1)

def solution(array, commands):
    answer = []
    N = len(commands)
    for command in commands:
        i, j, k = command
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
    return answer