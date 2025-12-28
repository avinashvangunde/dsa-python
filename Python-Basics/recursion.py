print("Recursion")

#  write code to print in 1->10 using recursion
def print_inc(n):
    if(n == 10):
        print(n)
        return 
    
    print(n)
    print_inc(n+1)
    


# print_inc(1)



#  write code to get sum of all values in a given list

l = [1,2,3,4,5]

def getSum(l , idx):
    if(idx == len(l)):
        return 0
    
    return l[idx] + getSum(l,idx+1)


print(getSum(l,0))