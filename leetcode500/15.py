class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue # if already use i, no need to use any more
            low, high = i + 1, len(nums) - 1
            while low < high:
                three = nums[i] + nums[low] + nums[high]
                if three == 0:
                    res.add((nums[i], nums[low], nums[high]))
                    low += 1
                    high -= 1
                elif three < 0:
                    low += 1
                else:
                    high -= 1
        return res