# Addition of two matrices

a = [ [2, 3] ,
      [4 ,5]  ]

b = [ [1, 2] ,
      [3 ,4] ]

# summer = [ [0,0],
#            [0,0]]

summer = [[float('-inf') for j in range(len(a[0]))] for i in range(len(a))]

print(a[0][0])
print(a[0][1])
print(a[1][0])

for i in range(len(a)):      
    for j in range(len(a[1])):
        summer[i][j] = a[i][j] + b[i][j]

print(summer)