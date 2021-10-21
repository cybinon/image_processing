sentence = input()

dictb = {}

for i in sentence:
  try:
    dictb[i] += 1;
  except:
    dictb[i] = 1

char = ''
max = 0;
for i in sentence:
  if dictb[i]>max:
    max = dictb[i]
    char = i;

print(char +":"+str(max))