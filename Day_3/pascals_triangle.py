# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
            
        if numRows == 1 :
            return result
        
        elif numRows == 2 :
            result.append([1,1])
            return result
        
        else :
            result = [[1], [1,1]]
            
            for i in range(2, numRows) :
                row = [1]
                
                for j in range(1, len(result[i-1])) :
                    sum_ = result[i-1][j-1] + result[i-1][j]
                    row.append(sum_)
                
                row.append(1)
                result.append(row)
            
            return result
