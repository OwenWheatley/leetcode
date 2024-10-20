class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        thisdict = {}
        for i, n in enumerate(nums):
            if (target - n) in thisdict:
                return [thisdict.get(target - n), i]
            else:
                thisdict.update({n : i})