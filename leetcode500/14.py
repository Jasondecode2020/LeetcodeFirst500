class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0] # the first word
        for item in strs:
            while not item.startswith(prefix): # deduct 1 ending char
                prefix = prefix[:-1]
        return prefix