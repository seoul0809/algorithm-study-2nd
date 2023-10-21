# 모의고사
# 프로그래머스 코딩테스트 고득점 kit > 완전탐색
# 1280 (+2)
# 1번부터 차례대로 1,2,3번 수포자가 맞았는지 틀렸는지 확인해서 배열에 개수 업데이트하기
# 최대 점수와 같은 사람 번호 answer에 추가하고 정렬

def solution(answers):
    answer = []
    first = [1, 2, 3, 4, 5]*2000
    second = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000
    
    correctCnt = [0]*3
    N = len(answers)
    for i, v in enumerate(answers):
        if first[i] == v:
            correctCnt[0] += 1
        if second[i] == v:
            correctCnt[1] += 1
        if third[i] == v:
            correctCnt[2] += 1
    
    maxIdx = -1
    maxVal = max(correctCnt)
    for i, v in enumerate(correctCnt):
        if maxVal == v:
            answer.append(i+1)
    answer.sort()
    return answer