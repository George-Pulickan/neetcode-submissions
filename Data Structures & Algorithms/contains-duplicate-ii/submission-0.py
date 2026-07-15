class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        
        for i, num in enumerate(nums):
            # 1. If the number is already in our window, we found a nearby duplicate
            if num in window:
                return True
                
            # 2. Add the current number to the window
            window.add(num)
            
            # 3. Maintain window size: remove the element that fell out of range k
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False
