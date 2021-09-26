class Solution:
    def myAtoi(self, s: str) -> int:
        # get rid of starting and ending of spaces
        s = s.strip()
        # check the signs
        sign = ['+', '-']
        # get numbers
        res = ""
        for i, c in enumerate(s):
            if i == 0 and c in sign:
                res += c
                continue
            if c.isnumeric():
                res += c
            else:
                break
        # not correct num, return 0
        if not res or res in sign:
            return 0
        # return numbers if inside
        return min(max(int(res), -2**31), 2**31 - 1)
        