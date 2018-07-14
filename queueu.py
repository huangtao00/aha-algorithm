#!coding:utf8
import random
num=random.choices(range(0,11),k=12)
num=[6,3,1,7,5,8,9,2,4]
print (num)
head=0
tail=9

while head<tail:
	print (num[head],end="+")
	head+=1
	if head==tail:
		break
	# print (num)
	# print ("tail",tail)
	# print ('head',head)
	num.append(num[head])
	tail+=1
	head+=1
print ("\n")
