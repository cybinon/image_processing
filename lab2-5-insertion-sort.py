n = input().split(" ")

for i in range(1, len(n)):
  key = n[i]
  j = i-1
  while j>=0 and key < n[j]:
    n[j+1] = n[j]
    j=j-1
  n[j+1] = key

for i in n:
  print(i, end=' ')