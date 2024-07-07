a=int(dividend/divisor)
if a>(2**31-1) or a<(-2**31-1):
  return 2**31-1
else:
  return a
