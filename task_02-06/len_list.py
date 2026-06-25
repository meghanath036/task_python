l=[1,4,5,78,9,0,4,3]
len=0
for i in l:
    len+=1
print(len)


'''using while'''
l=[1,4,5,78,9,0,4,3]
len=0
while(l):
    l.pop()
    len+=1
print(len)