class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        longest, left, right = 1, 0, 1
        if len(s) < 2:
            return len(s)
        # right poiner move forwards
        while right < len(s):
            if s[right] not in s[left: right]:
                longest = max(longest, right - left + 1)
            else:
                left = s.index(s[right], left, right) + 1
            right += 1
        return longest