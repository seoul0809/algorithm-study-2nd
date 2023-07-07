# 자물쇠와 열쇠
# https://school.programmers.co.kr/learn/courses/30/lessons/60059

def rotate_key(key):
    M = len(key)
    new_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            new_key[j][M - 1 - i] = key[i][j]
    return new_key


def check(new_lock):  # 자물쇠 중앙이 모두 1인지 확인
    N = len(new_lock) // 3
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    M, N = len(key), len(lock)

    # 자물쇠 배열의 3배 크기되는 배열 만들고 중앙에 자물쇠가 오도록 하기.
    new_lock = [[0] * 3 * N for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            new_lock[N + i][N + j] = lock[i][j]

    for k in range(4):
        key = rotate_key(key)
        for x in range(2 * N):
            for y in range(2 * N):
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock):  # 중앙이 모두 1인지 확인
                    return True

                # 자물쇠 원상복구하기
                for i in range(M):
                    for j in range(M):
                        new_lock[x + i][y + j] -= key[i][j]

    return False