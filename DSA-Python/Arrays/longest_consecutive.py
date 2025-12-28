my_set = set()
maxi = 0 
nums = [100,4,200,1,3,2]

for n in nums:
    my_set.add(n)

cnt = 0
for n in nums:
    cnt = 0
    if (n-1 in my_set):  
        cnt+=1
        val = n-1
        while( val  in my_set ):
            cnt+=1
            val-=1
    
    maxi = max(cnt , maxi)
    cnt = 0
    if (n+1 in my_set):
        cnt = 1
        val = n+1
        while( val not in my_set ):
            cnt+=1
            val+=1
            
    maxi = max(cnt , maxi)

print(maxi)