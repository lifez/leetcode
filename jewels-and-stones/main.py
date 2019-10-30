class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        result = 0
        list_of_j = list(J)
        for each in list_of_j:
            result += S.count(each)
        return result
