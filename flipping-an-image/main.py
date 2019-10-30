# https://leetcode.com/problems/flipping-an-image/submissions/
class Solution:
    def swap(self, value):
        return 1 - value
    
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for each in A:
            each = list(map(self.swap, each))
            
            each.reverse()
            result.append(each)
        return result
    
    
