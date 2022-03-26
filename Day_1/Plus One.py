# problem link: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        
        for d in digits :
            num += str(d)
        
        num = int(num)+1
        
        result = []
        for d in str(num) :
            result.append(d)
        
        return result
