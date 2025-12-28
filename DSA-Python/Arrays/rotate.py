def rev(nums, st ,end):
    while(st < end):
        temp = nums[st]
        nums[st] = nums[end]
        nums[end] = temp
        st+=1
        end-=1

nums = [1,2,3,4,5,6,7]
k = 3

n = len(nums)
rev(nums,0,n-k-1)
rev(nums,n-k,n-1)
rev(nums,0,n-1)
print(nums)