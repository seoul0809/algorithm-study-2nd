from itertools import permutations

n=int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int, input().split())

min_val=1e9+1
max_val=-1e9-1

signs=[]
for _ in range(add):
    signs.append('+')
for _ in range(sub):
    signs.append('-')
for _ in range(mul):
    signs.append('*')
for _ in range(div):
    signs.append('/')

for p in permutations(signs,n-1):
    sum=data[0]
    for i in range(1,len(data)):
        if p[i-1]=='+':
            sum+=data[i]
        elif p[i-1]=='-':
            sum-=data[i]
        elif p[i-1]=='*':
            sum*=data[i]
        else:
            sum=int(sum/data[i])

    max_val=max(max_val,sum)
    min_val=min(min_val,sum)

print(max_val)
print(min_val)