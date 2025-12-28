# multiplication of matrices
a = [ [1,2,3,4],
      [5,6,7,8]]

b = [ [1,2,1],
      [0,1,0],
      [4,1,2],
      [2,3,1]]

c = [[0 for j in range(len(b[0]))] for i in range(len(a))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(b)):
            c[i][j] += a[i][k] * b[k][j]

print(c)