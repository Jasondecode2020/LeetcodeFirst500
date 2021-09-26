class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        prev = table["M"]
        res = 0
        for c in s:
            res += table[c]
            if prev < table[c]: # table[c] is curr
                res -= 2 * prev
            prev = table[c]
        return res