a = input().split(" ")

max = 0;
for i in a:
  if int(i)<0 and max<int(i)*-1:
    max=int(i)*-1

print(max*-1)