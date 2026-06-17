class Solution:


    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0

        starting_vals = []
        nums = set(nums)

        for item in nums:
            if (item - 1) not in nums:
                starting_vals.append(item)
        
        current_streak = 1
        longest_streak = 1

        
        for item in starting_vals:
            i = 1
            while True: 
             if (item + i) in nums:
                current_streak += 1
                i += 1
             else:
                if current_streak > longest_streak:
                    longest_streak = current_streak 
                current_streak = 1
                break

        return longest_streak




        



        