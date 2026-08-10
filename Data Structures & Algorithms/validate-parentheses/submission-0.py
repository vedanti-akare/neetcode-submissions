class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opentoclose={
            ']':'[',')':'(','}':'{'
        }

        for ch in s:
            if ch in opentoclose:
                if not stack or stack[-1]!=opentoclose[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack


        