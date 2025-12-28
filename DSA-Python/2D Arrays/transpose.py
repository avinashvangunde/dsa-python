a = [ [1,2],
      [5,6]]

# outplace
at = [ [0 for j in range(len(a))] for i in range(len(a[0]))]

for i in range(len(a[0])):
    for j in range(len(a)):
        at[i][j] = a[j][i]

for lst in at:
    print(lst)

print()

# inplace
for i in range(len(a)):
    for j in range(i,len(a)):
        temp = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = temp

for lst in a:
    print(lst)