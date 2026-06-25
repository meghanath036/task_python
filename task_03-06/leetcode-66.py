digits=[1,2,3]
sum=0
for i in range(len(digits)):
    sum=sum*10+ digits [i]
sum=sum+1
result=[]
for i in str(sum):
    result.append(int(i))
print(result)
        