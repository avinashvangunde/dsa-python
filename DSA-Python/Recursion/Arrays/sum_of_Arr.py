
def Sum_of_Arr(a , i):
    if(i == len(a)-1):
        return a[i]
    
    return a[i] + Sum_of_Arr(a,i+1)

a = [2,3,5,2,1]
print(Sum_of_Arr(a,0))