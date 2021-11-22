class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        a=''.join(reversed(x))
        if a==x:
            return True
        else:
            return False
