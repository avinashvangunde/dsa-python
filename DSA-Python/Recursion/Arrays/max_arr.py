
def max_of_Arr(a,i):
    if(i == 0):
        return a[i]
    
    return max(a[i],max_of_Arr(a,i-1 ))

a = [5,3,4,9,6]
print(max_of_Arr(a,len(a)-1))