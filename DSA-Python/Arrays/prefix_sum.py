# Prefix sum   , Subarrays                    
nums  = [1,2,1,2,1]


# prefix_sum = []
# prefix_sum.append(nums[0])

# for i in range(1,len(nums)):
#     prefix_sum.append(nums[i] + prefix_sum[i-1])
# print(prefix_sum)


# # Brute force Approach
# # # print all subarrays for nums and get max sum from this 
# # # nums = [1,2,1,2,1]

# print(nums,"\n")
# max = float('-inf')

# for i in range(len(nums)):
#     for j in range(i , len(nums)):
#         print("[",end = "")
#         cur_sum = 0
#         for k in range(i,j+1):
#             print(nums[k],end="")
#             cur_sum += nums[k]
#         print("]")
#         print(cur_sum)
#         if (cur_sum > max):
#             max = cur_sum

# print("Max sum is : ",max)


# # print all subarrays for nums and tell if sum(subarray) exists with given sum 'k'
# # nums = [1,2,3,4,5] , m = 9

# m = 9
# for i in range(len(nums)):
#     for j in range(i , len(nums)):
#         cur_sum = 0
#         ans = []
#         for k in range(i,j+1):
#             cur_sum += nums[k]
#             ans.append(nums[k])
#         if(cur_sum == m):
#             print(ans)
        
        
# print all longest subarray for nums and tell if sum(subarray) exists with given sum 'k'
# nums = [1,2,3,4,5] , m = 9

# nums = [1,1,1]



# m = 2
# max_list = []
# for i in range(len(nums)):
#     for j in range(i , len(nums)):
#         cur_sum = 0
#         ans = []
#         for k in range(i,j+1):
#             cur_sum += nums[k]
#             ans.append(nums[k])
#         if(cur_sum == m):
#             if(len(max_list) < len(ans)):
#                 max_list = ans 

# print(max_list)


# cnt = 0
# for i in range(len(nums)):
#     for j in range(i , len(nums)):
#         cur_sum = 0
#         for k in range(i,j+1):
#             cur_sum += nums[k]
#         if(cur_sum == m):
#             cnt += 1
        
# print(cnt)


# optimal code
m = 7
cnt = 0
pref = 0
my_dict = {0: 1} 

for n in nums:
    pref += n
    i = pref - m
    if (i in my_dict):
        cnt+=my_dict[i]

    if(pref in my_dict):
        my_dict[pref] += 1
    else:
        my_dict[pref] = 1

print(my_dict)
print(cnt)
