from collections import deque
class Solution:
    def bruteForceMaxSlidingWindow(self, nums: list[int], k: int):
        n=len(nums)
        result = []
        for i in range(n-k+1):
            window_max = nums[i]
            for j in range(1,k):
                if nums[i+j]>window_max:
                    window_max = nums[i+j]
            result.append(window_max)
        return result
    def maxSlidingWindow(self, nums: list[int], k: int):
        n=len(nums)
        result=[]
        dq = deque()
        for i in range(n):
            if dq and dq[0]<=i-k:
                dq.popleft()
            while dq and nums[dq[-1]]<nums[i]:
                dq.pop()
            dq.append(i)
            if i >= k-1:
                result.append(nums[dq[0]])
        return result 

object=Solution()
# print(object.bruteForceMaxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
print(object.bruteForceMaxSlidingWindow([1,-1], 1))           
# print(object.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))       
print(object.maxSlidingWindow([1,-1], 1))          