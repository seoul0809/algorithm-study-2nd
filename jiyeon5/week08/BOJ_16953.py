a,b=map(int,input().split())

answer=1
while b>a:
    origin=b
    if b%10==1:
        b//=10
    elif b%2==0:
        b//=2
    else:
        break
    answer+=1

if b==a:
    print(answer)
else:
    print(-1)