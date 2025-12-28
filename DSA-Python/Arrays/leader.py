
arr = [1, 2, 5, 3, 1, 2]

# def findMax(st ,end , nums):
#     maxi = float('-inf')
#     for i in range(st,end+1):
#         maxi = max(nums[i],maxi)
#     return maxi

# i = 0
# n = len(nums)-1
# ans = []

# while(i != n):
#     m = findMax(i+1,n,nums)
#     if(nums[i] > m):
#         ans.append(nums[i])
#     i+=1

# ans.append(nums[i])
# print(ans)


max_ele = arr[len(arr)-1]
ans = []
ans.append(max_ele)


for i in range(len(arr)-2,-1,-1):
    if(max_ele < arr[i]):
        ans.append(arr[i])
        max_ele = arr[i]
ans.sort()
    
print(ans)