class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        count = {}
        sol = []

        for number in nums:
            if number not in count:
                count[number] = 1
            else:
                count[number] += 1

        for item in count:
            if count.get(item) > (len(nums) // 3):
                sol.append(item)

        return sol
        