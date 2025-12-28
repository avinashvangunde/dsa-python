
num = "4206" 
if int(num) % 2 != 0:
    print(num)

maxOdd = float('-inf')

for char in num:
    n = int(char)

    if n%2 != 0:
      maxOdd = max(n,maxOdd)
    
print(str(maxOdd))
