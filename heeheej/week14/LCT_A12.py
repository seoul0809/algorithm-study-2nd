# 기둥과 보 설치
# https://school.programmers.co.kr/learn/courses/30/lessons/60061
# 현재 각 좌표에 기둥이 있는지 여부 -> col_map, 보가 있는지 여부 -> row_map
# boolean값을 원소로 가지는 2차원배열 col_map, row_map 두개를 만들어서 판단했다.
# 기둥의 설치 및 삭제는 그때그떄 처리하는 것 대신, build_frame에 대한 반복을 모두 끝낸 다음
# 한번에 col_map, row_map를 확인해서 True인것을 answer에 담아줬다.

def build_check(x, y, a, col_map, row_map):
    if a == 0:  # 기둥 설치
        if y == 0 or row_map[x-1][y] or row_map[x][y] or col_map[x][y-1]:
            return True
        else:
            return False
    else:   # 보 설치
        if col_map[x][y-1] or col_map[x+1][y-1] or (row_map[x-1][y] and row_map[x+1][y]):
            return True
        else:
            return False

def remove_check(x, y, a, col_map, row_map):
    if a == 0:  # 기둥 삭제
        # 임시로 기둥 삭제
        col_map[x][y] = False
        if col_map[x][y+1] and not build_check(x, y+1, 0, col_map, row_map):
            return False
        if row_map[x-1][y+1] and not build_check(x-1, y+1, 1, col_map, row_map):
            return False
        if row_map[x][y+1] and not build_check(x, y+1, 1, col_map, row_map):
            return False
        return True
    else:   # 보 삭제
        # 임시로 보 삭제
        row_map[x][y] = False
        if col_map[x][y] and not build_check(x, y, 0, col_map, row_map):
            return False
        if col_map[x+1][y] and not build_check(x+1, y, 0, col_map, row_map):
            return False
        if row_map[x-1][y] and not build_check(x-1, y, 1, col_map, row_map):
            return False
        if row_map[x+1][y] and not build_check(x+1, y, 1, col_map, row_map):
            return False
        return True

def solution(n, build_frame):
    answer = list()
    col_map = [[False]*(n+2) for _ in range(n+2)]
    row_map = [[False]*(n+2) for _ in range(n+2)]

    for x, y, a, b in build_frame:
        if b == 1 and build_check(x, y, a, col_map, row_map):
            if a == 0:
                col_map[x][y] = True
            else:
                row_map[x][y] = True
        elif b == 0 and not remove_check(x, y, a, col_map, row_map):
            if a == 0:
                col_map[x][y] = True
            else:
                row_map[x][y] = True
        # pprint.pprint(locals())

    for i in range(n+1):
        for j in range(n+1):
            if col_map[i][j]:
                answer.append([i, j, 0])
            if row_map[i][j]:
                answer.append([i, j, 1])

    answer.sort(key = lambda x:(x[0], x[1], x[2]))
    return answer