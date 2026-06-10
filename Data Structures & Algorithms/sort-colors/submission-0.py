class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0,0,0]

        for item in nums:
            count[item] += 1

        i = 0
        for n in range(len(count)):
            for j in range(count[n]):
                nums[i] = n
                i += 1
        
        return nums
        