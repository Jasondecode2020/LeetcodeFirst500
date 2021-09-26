class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search for O(log(m+n)), always nums1 shorter
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        x, y = len(nums1), len(nums2)
        low, high = 0, x
        while low <= high:
            partitionX = (low + high) // 2 # slice 2 part of nums1
            partitionY = (x + y + 1) // 2 - partitionX # math calculate of 2 parts
            maxLeftX = -float('inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]
            maxLeftY = -float('inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 1:
                    return max(maxLeftX, maxLeftY)
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) /2
            elif maxLeftX > minRightY:
                high = partitionX - 1 # move backward of nums1
            else:
                low = partitionX + 1