import copy
space=[[None]*4 for _ in range(4)] # 번호, 방향

for i in range(4):
    tmp=list(map(int,input().split()))
    for j in range(4):
        space[i][j]=[tmp[j*2],tmp[j*2+1]-1]


dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

def fish_move(space,shark_x,shark_y):
    for i in range(1,17):
        x,y=-1,-1
        for a in range(4):
            for b in range(4):
                if space[a][b][0]==i:
                    x,y=a,b
                    break

        if x==-1 and y==-1: continue
        dir=space[x][y][1]

        for j in range(8):
            new_dir=(dir+j)%8
            nx=x+dx[new_dir]
            ny=y+dy[new_dir]
            if 0<=nx<4 and 0<=ny<4 and not (nx==shark_x and ny==shark_y):
                space[x][y][1]=new_dir
                space[x][y],space[nx][ny]=space[nx][ny],space[x][y]
                break

def shark_move(shark_x,shark_y,eat,space):
    global sum
    eat+=space[shark_x][shark_y][0]
    sum=max(sum,eat)
    space[shark_x][shark_y][0]=0

    fish_move(space,shark_x,shark_y)

    shark_dir=space[shark_x][shark_y][1]
    for i in range(1,4):
        nx=shark_x+dx[shark_dir]*i
        ny=shark_y+dy[shark_dir]*i

        if 0<=nx<4 and 0<=ny<4:
            if space[nx][ny][0]>0:
                shark_move(nx,ny,eat,copy.deepcopy(space))


sum=0
shark_move(0,0,0,space)
print(sum)