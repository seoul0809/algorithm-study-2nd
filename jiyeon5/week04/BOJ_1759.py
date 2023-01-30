# l, c 입력받기
l, c = map(int, input().split())
# 알파벳 입력받기
arr = list(input().split())
# 암호는 증가하는 순서로 배열되어있으므로 정렬 진행
arr.sort()

# 조합을 담을 배열
temp = ['']*l
# 모음 배열
vowel = ['a','e','i','o','u']

def password(cnt, start, vow, cons):
    # 암호길이 만큼 배열이 생성됐을 경우 리턴
    if cnt == l:
        # 암호 조건과 맞았을 경우 배열 문자열로 출력
        if vow >=1 and cons >=2:
            print("".join(temp))
        return

    for i in range(start, c):
        # 모음일 경우
        if arr[i] in vowel:
            temp[cnt] = arr[i]
            password(cnt+1,i+1,vow+1,cons)
        # 자음일 경우
        else:
            temp[cnt] = arr[i]
            password(cnt+1,i+1,vow,cons+1)

password(0,0,0,0)