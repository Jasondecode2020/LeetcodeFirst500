class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        numtolet = {"2": ["a", "b", "c"],
                      "3": ["d", "e", "f"],
                      "4": ["g", "h", "i"],
                      "5": ["j", "k", "l"],
                      "6": ["m", "n", "o"],
                      "7": ["p", "q", "r", "s"],
                      "8": ["t", "u", "v"],
                      "9": ["w", "x", "y", "z"],
                      }
        # e.g. digits = "23"
        result = [''] # [''], ["a", "b", "c"]
        for n in digits: # n = 2, 3
            letters = numtolet[n] # ["a", "b", "c"], ["d", "e", "f"]
            current = [] # [], ["a", "b", "c"]
            for r in result: # r = '', ["a", "b", "c"]
                for l in letters: # l = 'a', l = 'd'
                    current.append(r+l) # ["a", "b", "c"] ["ad","ae","af","bd","be","bf","cd","ce","cf"]
            result = current # ["a", "b", "c"], ["ad","ae","af","bd","be","bf","cd","ce","cf"]

        return result