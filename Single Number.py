# Using for loop
for i in nums:
  a=nums.count(i)
  if a==1:
    return i
    i+=1
 # Usiing XOR -> opti
  a = 0
  for i in nums:
    a = a^i
    return a
