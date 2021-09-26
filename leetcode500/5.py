class Solution:
    def longestPalindrome(self, s: str) -> str:
        # help to get the longest str
        def helper(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        res = ""
        for i in range(len(s)):
            test = helper(i, i) # odd cases
            if len(test) > len(res): res = test
            test = helper(i, i+1) # even cases
            if len(test) > len(res): res = test
        return res