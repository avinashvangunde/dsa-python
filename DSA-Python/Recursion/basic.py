#  print 1->5
# n = 1

# def printer(n):
#     print(n)

# printer(n)
# printer(n+1)
# printer(n+2)
# printer(n+3)
# printer(n+4)


def printer(n):
    if(n==1):
        print(n)
        return
    
    print(n)
    printer(n-1)
    print(n)

n=5
printer(n)

