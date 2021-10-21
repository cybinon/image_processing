setence1 = input().split(' ')
setence2 = input().split(' ')

matchWord = ""
max = 0
for word in setence1:
  if word in setence2 and len(word)>max:
    matchWord = word;
    max = len(word);
    
print(matchWord + " - " + str(max))
