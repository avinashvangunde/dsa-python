nums1 = [1, 1, 4, 6, 7]

nums2 = [4]

ans = set()
i = 0 
j = 0 
while(i < len(nums1) and j<len(nums2)):
    if(nums1[i] < nums2[j]):
        ans.add(nums1[i])
        i+=1
        j+=1
    elif(nums1[i] > nums2[j]):
        ans.add(nums2[j])
        j+=1
    elif(nums1[i] == nums2[j]):
        ans.add(nums1[j])
        i+=1
        j+=1

if(i!=len(nums1)):
    while(i<len(nums1)):
        ans.add(nums1[i])
        i+=1

if(j!=len(nums2)):    
    while(j<len(nums2)):
        ans.add(nums2[j])
        j+=1


print(ans)