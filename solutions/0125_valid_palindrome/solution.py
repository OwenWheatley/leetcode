class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = []
        for c in s:
            if c.isalnum():
                s2.append(c.lower())
        leftP = 0
        rightP = len(s2) - 1
        while leftP < rightP:
            if s2[leftP] != s2[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True