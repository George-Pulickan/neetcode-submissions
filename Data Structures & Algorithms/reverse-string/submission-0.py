class Solution:
    def reverseString(self, s: List[str]) -> None:
        p1 = 0
        p2 = len(s) - 1

        while p1 < p2:
            temp_val = s[p1]
            s[p1] = s[p2]
            s[p2] = temp_val
            p1 += 1
            p2 -= 1
        