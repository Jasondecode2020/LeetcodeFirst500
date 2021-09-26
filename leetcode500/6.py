class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # this is for edge cases
        if numRows == 1 or len(s) <= numRows:
            return s
        # put all rows of chars in buckets
        bucket = [[] for i in range(numRows)]
        flip = -1
        row = 0
        # how to put chars in bucket as rows increase and decrease
        for c in s:
            bucket[row].append(c)
            if row == 0 or row == numRows - 1:
                flip *= -1
            row += flip
        # connect all chars
        for i in range(len(bucket)):
            bucket[i] = "".join(bucket[i])
        return "".join(bucket)