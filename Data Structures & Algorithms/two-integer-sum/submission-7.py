class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        solution = []

        for i in range(len(nums) - 1):
            for j in range(1, len(nums) - i):
                if (nums[i] + nums[i+j] == target):
                    solution.append(i)
                    solution.append(i+j)
                    return solution
        
        