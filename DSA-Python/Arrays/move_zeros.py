def swap(nums,a,b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp



nums = [0,1,0,3,12]    
i = 0
j = 1
while(j < len(nums)):
    if(nums[i]==0 and nums[j]!=0):
        swap(nums,i ,j)
        i+=1
        j+=1
    elif(nums[i]==0 and nums[j]==0):
        j+=1
    elif(nums[i]!=0 and nums[j]==0):
        j+=1        
            
print(nums)