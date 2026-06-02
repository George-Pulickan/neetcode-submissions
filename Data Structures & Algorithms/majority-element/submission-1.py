class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        num_counter = {}

        for item in nums:
            if item not in num_counter:
                num_counter[item] = 1
            else:
                num_counter[item] += 1

        return max(num_counter, key=lambda k: num_counter[k])
        