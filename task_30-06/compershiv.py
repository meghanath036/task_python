
s = "HI Hello Raju"
V=[]
C=[]
l=[C.append(i) if i not in "aeiouAEIOU" else V.append(i) for i in s if i!=" "]
print("vowels",V)
print( "consonants",C)



