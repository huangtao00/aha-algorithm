#depth first search

data=list(range(1,10))

book=[0 for i in range(0,10)]
container=[0 for i in range(0,10)]
import time
total=0
def dfs(step):
	global total
	if step==10:
		# print (container)
		a,b,c=container[1:4]
		d,e,f=container[4:7]
		g,h,i=container[7:10]
		if a*100+b*10+c+d*100+e*10+f==(g*100+h*10+i):
			print (container)
			total+=1
		# time.sleep(2)
		return True	
	for i in data:
		if book[i]==0:
			container[step]=i
			book[i]=1
			dfs(step+1)
			book[i]=0


dfs(1)
print(f"total={total}")
