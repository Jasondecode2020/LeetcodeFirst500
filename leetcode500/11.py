class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2 pointers
        lo, hi = 0, len(height) - 1
        res = 0
        while lo < hi:
            res = max(res, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1
        return res
            