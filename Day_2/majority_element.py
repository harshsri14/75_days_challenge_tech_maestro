# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hMap = {}
        
        for element in nums :
            if element not in hMap :
                hMap[element] = 1
            else :
                hMap[element] += 1
        
        max_, element = 0,0
        for k,v in hMap.items() :
            if v > (len(nums)//2) and v > max_:
                max_ = v
                element = k
        
        return element
