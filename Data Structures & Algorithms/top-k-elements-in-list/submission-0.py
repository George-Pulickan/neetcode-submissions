class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for item in nums:
            if item not in count:
                count[item] = 1
            else:
                count[item] += 1

        vals = []

        for i in range(k):
           vals.append(max(count, key=count.get))
           del count[max(count, key=count.get)]

        return vals


        