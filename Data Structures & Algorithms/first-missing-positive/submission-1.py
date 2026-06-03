class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 1. Cyclic sort: Place each number in its correct index if possible
        for i in range(n):
            # Keep swapping until the current element is in its correct spot,
            # out of bounds, or a duplicate of its target spot.
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Correct index for nums[i] is nums[i] - 1
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # 2. Find the first index where the value does not match expectations
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 3. If 1 through n are all present, the missing number is n + 1
        return n + 1

        