import random
num=random.choices(range(0,11),k=20)

tag=[0  for i in range(0,11)]
for i in num:
	tag[i]+=1
print (num)
print (tag)

i=list(range(1,8))  #1,2,3-7
tag=[0,0,0,0,0,0,0]
d=[0,0,0,0,0,0,0]
counter=0
for d[0] in i:
	for d[1] in i:
		for d[2] in i:
			for d[3] in i:
				for d[4] in i:
					for d[5] in i:
						for d[6] in i:
							for dd in d:
								# print (dd)
								tag[dd]=1
							if sum(tag)==7:
								print (d)
								counter+=1
							tag=[0,0,0,0,0,0,0,0]
print (counter)

#7x6x5x..x1
n=1
for i in range(1,8):
	n=n*i
print (n)


