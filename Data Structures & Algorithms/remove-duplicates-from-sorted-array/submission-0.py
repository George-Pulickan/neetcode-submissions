class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0

        while (p1 < len(nums) - 1):
            if nums[p1] == nums[p1 + 1]:
                del nums[p1 + 1]
            else:
                p1 += 1

        return len(nums)

        