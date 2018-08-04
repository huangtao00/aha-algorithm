#abc+def=ghi
import time
container=[0 for i in range(10)]
flag=[0 for i in range(10)]
count=1
def dfs(step):
    global count
    if step==10:
        a,b,c=container[1:4]
        d,e,f=container[4:7]
        g,h,i=container[7:10]
        if a*100+b*10+c+d*100+e*10+f==(g*100+h*10+i):
            # print (container)
            first=int(f"{a}{b}{c}")
            middle=int(f"{d}{e}{f}")
            result=int(f"{g}{h}{i}")
            print ("{}: {}+{}={}".format(count,first,middle,result),end=" ")
            print (first+middle==result)
            count+=1
            # time.sleep(2)
        return True
    for i in range(1,10):
        if flag[i]==0:
            flag[i]=1
            container[step]=i
            dfs(step+1)
            flag[i]=0
dfs(1)
