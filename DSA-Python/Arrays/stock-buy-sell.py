nums = [2,4,1]

buy = nums[0]
sell = 0
for i in range(1,len(nums)):
    if(nums[i] < buy):
        buy = nums[i]
        
    elif( nums[i] > sell ):
        if(nums[i] > buy):
            sell = nums[i]

if(sell - buy < 0):
    print(0)

print(sell - buy)