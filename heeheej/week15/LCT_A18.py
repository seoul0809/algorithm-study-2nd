# 괄호 변환 (PRG 60058)
# https://school.programmers.co.kr/learn/courses/30/lessons/60058

def solution(w):
    wLen = len(w)
    # 1. 빈 문자열일 경우
    if wLen == 0:
        return ""

    # 2. 두 문자열 u, v로 분리
    lCnt, rCnt = 0, 0
    u, v = "", ""
    flag = True  # u가 올바른문자열인지 여부
    for i in range(wLen):
        if w[i] == "(":
            lCnt += 1
        else:
            rCnt += 1
        if lCnt == rCnt:
            u = w[:i + 1]
            if i == wLen - 1:
                v = ""
            else:
                v = w[i + 1:]
            break
        elif lCnt < rCnt:
            flag = False
    # 3. u가 올바른 괄호 문자열인지 확인
    if flag:
        return u + solution(v)  # 3-1
    else:  # 4
        new = "(" + solution(v) + ")"
        u = u[1:len(u) - 1]
        for x in u:
            if x == ")":
                new += "("
            else:
                new += ")"
        return new