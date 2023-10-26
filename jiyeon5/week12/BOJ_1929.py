# 제곱근 이용
m,n=map(int,input().split())
for i in range(m,n+1):
    if i==1: continue
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else: print(i)

# 에라토스테네스체 이용
m,n=map(int,input().split())
arr=[True]*(n+1)
arr[1]=False

for i in range(2,int(n**0.5)+1):
    if arr[i]:
        j=2
        while i*j<=n:
            arr[i*j]=False
            j+=1

for i in range(m,n+1):
    if arr[i]:
        print(i)