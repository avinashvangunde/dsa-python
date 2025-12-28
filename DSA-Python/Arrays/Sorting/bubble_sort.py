#  Sorting code --> Bubble Sort

a = [ 5, 7, 4, 3, 1 ]

print(a)

def swap(avi,j):
    temp = avi[j]
    avi[j] = avi[j+1]
    avi[j+1] = temp
    

for i in range(len(a)):
    for j in range(0,len(a)-i-1):
        if (a[j] > a[j+1]):
            swap(a,j)

print(a)
