# using dict
b=[]
c = {}
for i in nums:
  if i in c:
    c[i]+=1
  else:
    c[i]=1
for key,value in c.items():
  if value>=2:
    b.append(key)     
return b

# using set
res = []
s = set()
for n in nums:
  if n in s:
    res.append(n)
  else:
    s.add(n)
return res
