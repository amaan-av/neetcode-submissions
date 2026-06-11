class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=""
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()
        lens=len(clean)-1
        for i in range(len(clean)//2):
            if clean[i]!=clean[lens-i]:
                return False
        return True