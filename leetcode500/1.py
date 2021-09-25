class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, val in enumerate(nums):
            res = target - val
            if res in d:
                return [d[res], idx]
            d[val] = idx