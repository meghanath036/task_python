# 1. ValueError
age = int(input("Enter age: "))

# Input:
# text
# abc


'''Output:

text
ValueError: invalid literal for int()'''


### 2. EOFError

# Occurs when no input is provided.

# python
name = input("Enter name: ")


'''Output:

text
EOFError: EOF when reading a line'''


## Output Errors

### 1. TypeError

# Occurs when incompatible data types are combined.

age = 20
# it my be error
# print("Age = " + age)


'''Output:
text
TypeError: can only concatenate str (not "int") to str'''


# Correct:

# python
print("Age =", age)
print(age)
