class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        L = 0
        R = len(s)-1
        while L < R :
            if s[L] == s[R] :
                L += 1 
                R -= 1
            else:
                return False
        return True