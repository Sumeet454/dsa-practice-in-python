# def rotateArrayRightByKPosition(nums):
#     # k = k%len(nums)
#     temp = nums[len(nums)-1]
#     print(temp)
#     for i in range(1,len(nums)):
#         nums[len(nums)-i]=nums[len(nums)-i-1]
#     nums[0]=temp
#     return nums
#
#
# nums = [1,2,3,4,5,6,7]
# print(rotateArrayRightByKPosition(nums))


def rotateArrayRightByKPosition(arr,k):
    n=len(arr)
    k = k%len(arr)
    temp = arr[n-k:n]
    print(temp)
    for i in range(n-k-1,-1,-1):
        arr[i+k] = arr[i]
    for i in range(k):
        arr[i] = temp[i]
    return arr
arr = [1,2,3,4,5,6,7]
print(rotateArrayRightByKPosition(arr,5))

