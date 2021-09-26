class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        old_x = x # x need to change
        reverse_x = 0
        while x:
            remainder = x % 10
            reverse_x = reverse_x * 10 + remainder
            x //= 10
        return reverse_x == old_x