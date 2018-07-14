#!coding:utf8
import random
num=random.choices(range(0,11),k=12)
welcome="="*14+"\n"+"bubble sort"+"\n"+"="*14
print (welcome)
print ("original numbers:{}".format(num))
for i in range(len(num)):
	for j in range(0,len(num)-i-1):
		if num[j]>num[j+1]:
			temp=num[j]
			num[j]=num[j+1]
			num[j+1]=temp
print ("sorted numbers:{}".format(num))

