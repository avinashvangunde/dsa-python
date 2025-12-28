# Merge Sort in Arrays using Recursion

def merge(a,l,mid,r):
    i = j = 0
    k = l

    left = []
    n1 = mid-l+1
    right = []
    n2 = r - mid

    for ele in range(n1):
        left.append(a[ele+l])
    
    for ele in range(n2):
        right.append(a[ele+mid+1])
    
    while(i<len(left) and j<len(right)):
        if(left[i] <= right[j]):
            a[k] = left[i]
            k+=1 
            i+=1
        else:
            a[k] = right[j]
            k+=1
            j+=1
    
    while(i<len(left)):
        a[k] = left[i]
        k+=1
        i+=1
    
    while(j<len(right)):
        a[k] = right[j]
        k+=1
        j+=1

def mergeSort(a , l , r):
    if(l>=r):
        return a
    
    mid = int((l+r)/2)
    mergeSort(a,l,mid)
    mergeSort(a,mid+1,r)
    merge(a,l,mid,r)


a = [50,40,30,20,10]
print(a)
mergeSort(a,0,len(a)-1)
print(a)