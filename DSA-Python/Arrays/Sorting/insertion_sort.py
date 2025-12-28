#  Sorting code --> Insertion Sort

a = [ 5, 7, 4, 3, 1 ]

print(a)

for j in range(1,len(a)):
    i = j - 1
    ele = a[j]

    while(i>=0 and ele < a[i]):
        a[i+1] = a[i]
        i-=1
        
    a[i+1] = ele 
        
print(a)
