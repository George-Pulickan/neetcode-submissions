class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []

        total = 1
        for item in nums:
            total *= item
            prefix.append(total)

        suffix = []
        total = 1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            suffix.append(total)
        
        suffix.reverse()

        output = []
        for i in range(n):
            output = []
        for i in range(n):
            # If at the far left, there is no prefix. Use 1.
            left = prefix[i - 1] if i > 0 else 1
            
            # If at the far right, there is no suffix. Use 1.
            right = suffix[i + 1] if i < n - 1 else 1
            
            output.append(left * right)
            
        return output
        
        
