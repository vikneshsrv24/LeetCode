nums=[3,0,1]
a=0
n=len(nums)
b=(n*(n+1)/2)
for i in nums:
  a+=i
return int(b-a)
