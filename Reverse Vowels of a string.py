a=['a','e','i','o','u','A','E','I','O','U']
b=[]
for i in s:
  if i in a:
    b+=i
    b.reverse()
        
new=""
j=0
for i in range(len(s)):
  if s[i] not in a:
    new+=s[i]
  else:
    new+=b[j]
    j+=1
return new


        
