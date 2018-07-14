#!coding:utf8
import random
num=random.choices(range(0,11),k=10)  #choose 10 number for 0 to 10 randomly
welcome="="*14+"\n"+"bucket sort"+"\n"+"="*14
print (welcome)

book=[0 for i in range(11)]
# print (book)
for i in num:
	book[i]+=1
# print (book)
result=[]
for i in range(len(book)):
	for j in range(book[i]):
		result.append(i)
print ("original numbers:{}".format(num))
print ("sorted numbers:{}".format(result))
# print result
