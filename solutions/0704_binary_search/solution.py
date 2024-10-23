class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftP, rightP = 0, len(nums) - 1

        while leftP <= rightP:
            m = leftP + ((rightP - leftP) // 2)
            if nums[m] > target:
                rightP = m - 1
            elif nums[m] < target:
                leftP = m + 1
            else:
                return m
        return -1