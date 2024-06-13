a=['a','e','i','o','u','A','E','I','O','U']
b=[]
for i in s:
  if i in a:
    b.append(i)

b.sort()
res = ""
j=0
for i in range(len(s)):
  if s[i] not in a:
    res += s[i]
  else:
    res+=b[j]
    j+=1
return res
