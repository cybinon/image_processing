nums = range(10,100)

for i in nums:
  sq = i*i;
  c = [int(j) for j in str(sq)]
  cub = 0;
  for j in c:
    cub+=j
  cub*=cub*cub;

  if(cub==sq):
    print(i)