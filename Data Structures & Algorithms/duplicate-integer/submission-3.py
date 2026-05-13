class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = []
        for item in nums:
            if item not in unique_vals:
                unique_vals.append(item)
            else:
                return True

        return False
        