class Solution:

    def checker(self, s, t):
        if len(s) != len(t):
            return False

        dict_1 = {}
        dict_2 = {}

        for i in range(len(s)):
            dict_1[s[i]] = dict_1.get(s[i], 0) + 1
            dict_2[t[i]] = dict_2.get(t[i], 0) + 1

        return dict_1 == dict_2


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = []
        visited = set()

        for i in range(len(strs)):

            if i in visited:
                continue

            subset = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(strs)):
                if j not in visited and self.checker(strs[i], strs[j]):
                    subset.append(strs[j])
                    visited.add(j)

            anagrams.append(subset)

        return anagrams