# PCCP 모의고사 2 1번 실습용로봇

def solution(command):
    answer = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    nx, ny = 0, 0
    d = 0    # 방향인덱스
    
    def rotateRight90(d):
        return (d + 1) % 4
    
    for x in command:
        if x == "G":
            nx += dx[d]
            ny += dy[d]
        elif x == "B":
            nx -= dx[d]
            ny -= dy[d]
        elif x == "R":
            d = (d + 1) % 4
        elif x == "L":
            d -= 1
            if d < 0:
                d = 3
        answer = [nx, ny]
    return answer