nums = [1,1,2]

i = 0
j = 1
while(j<len(nums)):
    if(nums[i] != nums[j]):
        i+=1
        j+=1
    else:
        del nums[j]
        print(nums,"\n")

print(nums)
print(len(nums))
