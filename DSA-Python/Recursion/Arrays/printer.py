def printer(a , i):
    if(i == 0):
        print(a[i])
        return
    
    printer(a,i-1)
    print(a[i])

a = [5,4,3,2,1]
printer(a,len(a)-1)


