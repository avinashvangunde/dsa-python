print("Python basics")


arr = [1,2,3,4,5]

# for ele in arr :
#     print(ele)

# for ele in range(0,len(arr)):
#     print(arr[ele])


val = 5

def search():
    for ele in arr:
        if ele == val:
            return True
    return False
    

ans = search()

if(ans == True):
    print("val is present")  
else:  
    print("val not present")
