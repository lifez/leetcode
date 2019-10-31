# https://leetcode.com/problems/unique-number-of-occurrences/submissions/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a = dict()
        for each in arr:
            if a.get(each):
                a[each] += 1
            else:
                a[each] = 1
        return len(list(a.values())) == len(set(a.values()))
        


