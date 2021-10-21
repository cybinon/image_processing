a = input()
b = input()


dictb = {}
sumb = 0;

for i in a:
  try:
    dictb[i] += 1;
  except:
    dictb[i] = 1
 
for i in b:
  if i in a and dictb[i] > 0:
    dictb[i] -= 1
    sumb +=1

if(sumb == len(b)):
  print("true")
else:
  print("false")

  
