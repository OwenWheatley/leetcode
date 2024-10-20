class Solution:
    def minOperations(self, nums: List[int]) -> int:
        @lru_cache(None)
        def greatest_proper_divisor(x: int) -> int:
            for i in range(x // 2, 0, -1):
                if x % i == 0:
                    return i
            return 1

        if all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)):
            return 0

        ans = 0

        for i in range(len(nums) - 2, -1, -1):
            while nums[i] > nums[i + 1]:
                gpd = greatest_proper_divisor(nums[i])
                
                if gpd == 1:
                    return -1
                
                nums[i] //= gpd
                ans += 1

                if nums[i] == 1 and nums[i] > nums[i + 1]:
                    return -1

        return ans