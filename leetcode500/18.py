class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        num_set = set()
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]: continue
            for j in range(i + 1, len(nums)):
                lo, hi = j + 1, len(nums) - 1
                while lo < hi:
                    four = nums[i] + nums[j] + nums[lo] + nums[hi]
                    if four == target:
                        num_set.add((nums[i], nums[j], nums[lo], nums[hi]))
                        lo += 1
                        hi -= 1
                    elif four < target:
                        lo += 1
                    else:
                        hi -= 1
        return num_set