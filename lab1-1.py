nums = range(1000, 9999)

txt = open("digits.txt", "at")
for i in nums:
  c = [int(j) for j in str(i)]
  if(c[0] == c[1] or  c[0] == c[2] or c[0] == c[3] or c[1] == c[2] or c[1] == c[3] or c[2] == c[3]):
    continue
  else:
    txt.write(str(i)+"\n")

txt.close()