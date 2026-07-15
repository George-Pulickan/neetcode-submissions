from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. Sort the list to easily avoid duplicates
        ans = []
        n = len(nums)
        
        # 2. Iterate up to n-2 because we need at least 3 elements
        for i in range(n - 2):
            # If the anchor is greater than 0, no remaining numbers can sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l = i + 1
            r = n - 1
            
            while l < r:
                total_sum = nums[i] + nums[l] + nums[r]
                
                if total_sum < 0:
                    l += 1  # Need a larger value
                elif total_sum > 0:
                    r -= 1  # Need a smaller value
                else:
                    # Found a valid triplet! Create a new inline list instance
                    ans.append([nums[i], nums[l], nums[r]])
                    
                    # Skip duplicate values for the left pointer
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicate values for the right pointer
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                        
                    # Move both pointers to look for more pairs with nums[i]
                    l += 1
                    r -= 1
                    
        return ans
