# https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        #count = 0
        minDifference = 1000**1000
        
        for i in range(n) :
            j = i+1
            k = n-1
            
            while j<k :
                sum_ = nums[i]+nums[j]+nums[k]
                
                if sum_ == target :
                    return target
                    
                elif sum_ > target :
                    k -= 1
                
                else : 
                    j += 1
                
            
                if minDifference > abs(target-sum_) :
                    minDifference = abs(target-sum_)
                    result = sum_
        
        return result
