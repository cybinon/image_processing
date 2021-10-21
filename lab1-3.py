nums = range(10,99)

for i in nums:
  a = i%10;
  b = i//10;

  if(i%(b+a) == 0):
    print(i)