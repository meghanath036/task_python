l=[9,8,10,45,78,34,56]
max1=l[0]
for i in range(1,len(l)):
    if(max1<l[i]):
        max1=l[i]
print(max1)