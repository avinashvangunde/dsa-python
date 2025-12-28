#  Sorting code --> Selection Sort

a = [ 5, 7, 4, 3, 1 ]

print(a)

def swap(avi,i,j):
    temp = avi[i]
    avi[i] = avi[j]
    avi[j] = temp


for i in range(len(a)-1):
    miny = i
    for j in range(i+1, len(a)):
        if(a[miny] > a[j]):
            miny = j
    swap(a,i,miny)
           

print(a)

