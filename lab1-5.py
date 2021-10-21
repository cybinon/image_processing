n = int(input())

nums = range(1, n+1)
for i in nums:
  r = range(1, i+1)
  n = i;
  sumb = 0;
  for j in r:
    if(i%j == 0):  
      sumb += j  
  print(sumb)
  if i == sumb:
    print(i)