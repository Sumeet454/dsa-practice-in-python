# 1st approach

# def largestNumber(nums):
#     largest_number=nums[0]
#     for num in nums:
#         if num > largest_number:
#             largest_number = num
#     return largest_number
#
# nums = [1,2,3,4,5,6,7]
# print(largestNumber(nums))

# 2nd approach

def largestNumber(nums):
    n= len(nums)
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            nums[i],nums[i+1]=nums[i+1],nums[i]
    return nums[-1]
nums = [1,2,3,9,5,6]
print(largestNumber(nums))
