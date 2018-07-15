#!coding:utf8
#palindrome practice
lrrl="xyzaazyx"
lrrl=input("please input some strings:>")
len_str=len(lrrl)


mid=int(len(lrrl)/2)-1

top=0 

half=""
i=0

#save the first half
while i<=mid:
	half+=lrrl[i]
	top+=1
	i+=1
if len_str%2:
	next=mid+2
else:
	next=mid+1
#compare firt half with end half
for i in range (next,len(lrrl)):
	top-=1
	print(i)
	if lrrl[i]!=half[top]:
		break
if top==0:
	print ("yes")
else:
	print ("no")
