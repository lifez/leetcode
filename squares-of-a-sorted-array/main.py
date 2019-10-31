# https://leetcode.com/problems/squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        double_list = list(map(lambda x: x*x, A))
        return sorted(double_list)
