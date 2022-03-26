# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        totalSum = sum(nums)
        
        for i in range(len(nums)) :
            leftSum = sum(nums[:i])
            rightSum = totalSum - leftSum - nums[i]
            
            if leftSum == rightSum :
                return i
        
        return -1
