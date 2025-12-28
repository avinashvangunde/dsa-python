nums = [-2,-3,-5]

maxi = float('-inf')
pref = 0
for n in nums :
    pref += n
    
    if pref > maxi : 
        maxi = pref

    if pref < 0: 
        pref = 0

print(maxi)