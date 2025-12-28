my_dict = {}
nums = [2,7,11,15] 
target = 9      

for i in range(0,len(nums)):
    if((target - nums[i]) in my_dict):
        
        print([i, my_dict.get(target - nums[i])])
        break
    else:
        my_dict[nums[i]] = i
        