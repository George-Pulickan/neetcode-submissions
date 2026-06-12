class Solution:


    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        
        longest = []
        count = 1

        values = set(nums)

        for item in values:
            i = item
            while True:
                if (i + 1) in values:
                    count += 1
                    i += 1
                else:
                    longest.append(count)
                    count = 1
                    break
        
        return max(longest)


        



        