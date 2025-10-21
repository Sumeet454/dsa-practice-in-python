# brute force approach
def intersectionOfArray(arr1, arr2):
    res=[]
    len_of_arr2 = len(arr2)
    vis= [0]*len_of_arr2
    for i in range(len(arr1)):
        for j in range(len_of_arr2):
            if arr1[i] == arr2[j] and vis[j] == 0:
                res.append(arr1[i])
                vis[j] = 1
                break
            if arr2[j]>arr1[i]:
                break
    return res

# optimal approach(two pointer approach)

def intersectionOfArrayOptimal(arr1, arr2):
    i=0
    j=0
    m=len(arr1)
    n=len(arr2)
    res=[]
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            i+=1
        elif arr2[j] < arr1[i]:
            j+=1
        else:
            res.append(arr1[i])
            i+=1
            j+=1
    return res

arr1 = [1,2,2,2,2,3,4,5,6,6,7]
arr2 = [2,2,2,6,7,8,9]
res = intersectionOfArrayOptimal(arr1, arr2)
print(res)
