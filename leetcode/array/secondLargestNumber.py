def secondLargestNumber(nums):
    largest=float('-inf')
    second_largest=float('-inf')
    for num in nums:
        if num>largest:
            second_largest = largest
            largest = num
        elif largest > num > second_largest:
            second_largest = num
    return second_largest


nums = [1,2,3,4,5,6,7]
print(secondLargestNumber(nums))
