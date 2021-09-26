class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lo, hi = i + 1, len(nums) - 1
            while lo < hi:
                three = nums[i] + nums[lo] + nums[hi]
                if three == target:
                    return target
                if abs(three - target) < abs(res - target):
                    res = three
                if three < target:
                    lo += 1
                else:
                    hi -= 1
        return res
            