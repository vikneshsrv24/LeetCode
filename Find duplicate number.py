# Using loop
nums.sort()
i,n = 0, len(nums)
while i<(n-1):
  if nums[i]==nums[i+1]:
    return nums[i]
    i+=1

# Using dict
d={}
for num in nums:
  if num in d:
    d[num]+=1
  else:
    d[num] = 1
  for num,num1 in d.items():
    if num1>1:
      return num
  return 0 
            
