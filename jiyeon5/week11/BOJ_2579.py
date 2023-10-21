n=int(input())
steps=[]
memo=[0]*n

for _ in range(n):
    steps.append(int(input()))

if n<=2:
    print(sum(steps))
else:
    memo[0]=steps[0]
    memo[1]=steps[0]+steps[1]
    memo[2]=max(steps[0]+steps[2],steps[1]+steps[2])

    for i in range(3,n):
        memo[i]=max(memo[i-3]+steps[i-1],memo[i-2])+steps[i]

    print(memo[-1])