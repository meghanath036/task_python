l=[9,8,10,45,78,34,56]
min1=l[0]
for i in range(1,len(l)):
    if(min1>l[i]):
        min1=l[i]
print(min1)