# https://leetcode.com/problems/sort-array-by-parity/submissions/
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odds = list(filter(lambda x: x % 2 != 0, A))
        even = list(filter(lambda x: x % 2 == 0, A))
        return even + odds
