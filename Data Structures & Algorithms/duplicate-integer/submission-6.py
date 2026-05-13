class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()
        for item in nums:
            if item in unique_vals:
                return True

            unique_vals.add(item)

        return False
        