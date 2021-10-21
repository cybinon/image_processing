sentence = input().split(' ')

dictb = {}

for i in sentence:
  dictb[i] = len(i);

char = ''
max = 0;
min = dictb[sentence[0]]
minWord = sentence[0]

for i in sentence:
  if dictb[i]>max:
    max = dictb[i]
    char = i
  if dictb[i]<min:
    min = dictb[i]
    minWord = i

print("Хамгийн урт үг:")
print(char +":"+str(max))
print("Хамгийн богино үг:")
print(minWord +":"+str(min))