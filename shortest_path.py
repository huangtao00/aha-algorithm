#1: block 2: friend 0: road
map=[
[0,0,1,0],
[0,0,0,0],
[0,0,1,0],
[0,1,2,0],
[0,0,0,1]
]
book=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
short_path=[]
last_path=[]
mini_step=100
d_xy=[[0,1],[1,0],[0,-1],[-1,0]]
import time
def dfs(row,col,step):
    global mini_step
    global short_path
    global last_path
    if map[row][col]==2: #i catch u
        print (short_path,step)
        # time.sleep(1)
        if step<mini_step:
            mini_step=step
            last_path=short_path[:]
        short_path=[]
        return True
    tx=row
    ty=col
    for drow,dcol in d_xy:
        row=tx+drow
        col=ty+dcol
        #out of boundary
        if (row<0 or col<0 or row>4 or col>3 ):
            continue
        # print (row,col)
        if (map[row][col]==0 or map[row][col]==2) and book[row][col]==0:
            book[row][col]=1
            # print (row,col)
            short_path.append((row,col))
            # time.sleep(1)
            dfs(row,col,step+1)
            book[row][col]=0
book[0][0]=1
dfs(0,0,0)
print ("#"*60)
print ("minimum path={} steps".format(mini_step))
print ("The detail path is shown below:")
for i in last_path[:-1]:
    print ("{}->".format(i),end="")
print (last_path[-1])
