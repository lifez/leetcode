# https://leetcode.com/problems/self-dividing-numbers
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for each in range(left, right+1):
            if all(each_num != 0 and each % each_num == 0 for each_num in list(map(lambda x: int(x), str(each)))):
                   result.append(each)
        return result
