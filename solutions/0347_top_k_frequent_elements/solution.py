class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen_count_dict = {}

        for n in nums:
            seen_count_dict[n] = seen_count_dict.get(n, 0) + 1
        return sorted(seen_count_dict, key=seen_count_dict.get, reverse=True)[:k]