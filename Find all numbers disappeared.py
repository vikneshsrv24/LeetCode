b=[]
a=set(nums)
for i in range(1,len(nums)+1):
  if i not in a:
    b.append(i)
return b
