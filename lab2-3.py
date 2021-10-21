a = input().split(" ")

s=0;
for i in a:
  s += int(i)

s=s/len(a)

for i in a:
  if int(i) > s:
    print(i)