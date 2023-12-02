# PCCP 모의고사 1 3번 유전법칙
# 재귀함수
# 4의 배수일 때 4로 나눈 나머지 0인 경우 4로 해줘야함

from collections import defaultdict

def solution(queries):
    answer = []
    d = defaultdict(list)
    d["RR"] = ["RR", "RR", "RR", "RR"]
    d["Rr"] = ["RR", "Rr", "Rr", "rr"]
    d["rr"] = ["rr", "rr", "rr", "rr"]
    
    for n, p in queries:
        arr = []
        if p % 4 == 0:
            arr.append(4)
        else:
            arr.append(p % 4)
        
        def recursive(gen, p):
            if gen == 2:
                return
            # arr.append((p//4+1)%4)
            # recursive(gen-1, p//4+1)
            if p % 4 == 0:
                arr.append((p//4)%4)
                recursive(gen-1, p//4)
            else:
                arr.append((p//4+1)%4)
                recursive(gen-1, p//4+1)
        
        if n == 1:
            answer.append("Rr")
        else:
            recursive(n, p)
            arr = arr[::-1]
            prev = "Rr"
            for x in arr:
                prev = d[prev][x-1]
                print(prev)
            answer.append(prev)
        
    return answer