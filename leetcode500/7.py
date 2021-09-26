class Solution:
    def reverse(self, x: int) -> int:
        # reverse pos num, if negative, convert to pos
        def reverse_pos_num(num):
            reverse = 0
            while num:
                remainder = num % 10
                reverse = reverse * 10 + remainder
                num //= 10
            return reverse
        if x >= 0 and reverse_pos_num(x) <= 2**31 - 1:
            return reverse_pos_num(x)
        elif x < 0 and -reverse_pos_num(-x) >= -2**31:
            return -reverse_pos_num(-x)
        else:
            return 0