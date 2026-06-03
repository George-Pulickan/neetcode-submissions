class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 1
        while (1):
            if start not in nums:
                return start
            else:
                start = start+1

        