class Solution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        leftP, rightP = 0, len(strX) - 1
        while leftP < rightP:
            if strX[leftP] != strX[rightP]:
                return False
            leftP += 1
            rightP -= 1
        return True
