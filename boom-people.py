map=[["#","#","#","#","#","#","#","#","#","#"],\
     ["#","g",".","g","g","g","g",".",".","#"],\
     ["#","g",".","g","g","g","g",".",".","#"],\
     ["#","g",".","g","g","g","g",".","g","#"],\
     ["#","g","#","g","g",".","g","g",".","#"],\
     ["#","g","g","g","g","g","g",".",".","#"],\
     ["#","#","#","#","#","#","#","#","#","#"]]

# # =brick   .= empty  g=monster
def boom(x,y):
    global map
    sum=0
    if map[x][y]==".":
        i=x
        j=y
        while map[i][j]!="#":  #up
            # print (map[i][j])
            if map[i][j]=="g":
                sum+=1
            i-=1
        i=x
        j=y
        while map[i][j]!="#":  #down
            if map[i][j]=="g":
                sum+=1
            i+=1
        i=x
        j=y
        while map[i][j]!="#":  #down
            if map[i][j]=="g":
                sum+=1
            j-=1
        i=x
        j=y
        while map[i][j]!="#":  #down
            if map[i][j]=="g":
                sum+=1
            j+=1
    return (x,y,sum)

max_monster=0
i,j=0,0
for ii in range(len(map)):
    for jj in range(len(map[0])):
        x,y,sum=boom(ii,jj)
        # print (x,y,sum,max_monster)
        if max_monster<sum:
            # print (x,y,max_monster,sum)
            max_monster=sum
            i,j=x,y
            # print (i,j)
print (i,j,max_monster)
