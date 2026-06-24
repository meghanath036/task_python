#  If two values are same values perform “XOR” operation 
# what willbe the output

x=1
y=1
z=x^y
print(z)


# Perform and operation 1 is even? Or odd?
#   What will the output?
x=int(input("enter a number"))
if(x&1==0):
    print("even")
else:
    print("odd")


# parctice all bitwise operators
x=90
y=54
print(x&y)
print(x|y)
print(x^y)
print(~x)
print(x<<2)
print(x>>2)



# using bitwise operators with assignment
x=int(input("Enter a number: "))
y=int(input("Enter another number: "))
x &= y
print(x)
x |= y
print(x)
x ^= y
print(x)
x <<= 2
print(x)
x >>= 2
print(x)
