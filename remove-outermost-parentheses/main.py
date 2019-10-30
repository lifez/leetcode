class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack = []
        result = []
        for each in S:
            if each == "(":
                
                if len(stack) > 0:
                    result.append(each)
                stack.append(each)
            else:
                stack.pop()
                if len(stack) > 0:
                    result.append(each) 
        return ''.join(result)
                
