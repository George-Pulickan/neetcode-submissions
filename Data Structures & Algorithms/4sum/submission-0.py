from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)
        
        # 1. First anchor loop (i)
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 2. Second anchor loop (j)
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                # 3. Two-pointer setup for the remaining two elements
                l = j + 1
                r = n - 1
                
                while l < r:
                    total_sum = nums[i] + nums[j] + nums[l] + nums[r]
                    
                    if total_sum < target:
                        l += 1  # Sum is too small, move left pointer right
                    elif total_sum > target:
                        r -= 1  # Sum is too large, move right pointer left
                    else:
                        # Found a valid quadruplet!
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        
                        # Skip duplicate values for the left pointer
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        # Skip duplicate values for the right pointer
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                            
                        # Move both pointers inward
                        l += 1
                        r -= 1
                        
        return ans

        