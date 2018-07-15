

data=[("toy",3),("tom",27),("jack",33),("nacy",44)]
insert_cell=("Jim",30)
print ("original data:{}".format(data))
print ("we have to insert cell:{}".format(insert_cell))
for index in range(len(data)):
	if data[index][1]>insert_cell[1]:
		data.insert(index,insert_cell)
		break

print ("final data:{}".format(data))
 
