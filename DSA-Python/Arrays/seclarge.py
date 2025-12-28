nums = [10, 10, 10, 10, 10]
print(nums)

max = float('-inf')
sec_max = float('-inf')
flag = 0 

for num in nums:
    if(num > max):
        max = num
    if(num < max and num > sec_max):
        sec_max = num
        flag=1

if(flag == 0):
    sec_max = -1        

print(max)
print(sec_max)