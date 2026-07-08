'''You are given a positive integer n. Each digit of n has a sign according to the following rules:

The most significant digit is assigned a positive sign.
Each other digit has an opposite sign to its adjacent digits.
Return the sum of all digits with their corresponding sign.

 

Example 1:

Input: n = 521
Output: 4
Explanation: (+5) + (-2) + (+1) = 4.'''






n=521
r = 0
m = list(str(n))
for i in range(len(m)):
    if i % 2 == 0:
        r += int(m[i])
    else:
        r -= int(m[i])
print(r)
        