class Solution:
    def bruteLongestOnes(self,nums:list[int],k:int)->int:
        n=len(nums)
        max_length = 0
        for i in range(n):
            zeros = 0
            for j in range(i,n):
                if nums[j]==1 and zeros<=k:
                    max_length = max(max_length,j-i+1)
                if nums[j]==0:
                    zeros+=1    
        return max_length
        

object = Solution()
print(object.bruteLongestOnes([1,1,1,0,0,0,1,1,1,1,0],2))