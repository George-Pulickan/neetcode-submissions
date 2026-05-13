class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        dict_1 = {}
        dict_2 = {}

        for i in range(len(s)):
            if s[i] not in dict_1:
                dict_1[s[i]] = 1
            else:
                dict_1[s[i]] += 1
            
            if t[i] not in dict_2:
                dict_2[t[i]] = 1
            else:
                dict_2[t[i]] += 1
        
        if dict_1 == dict_2:
            return True
        else:
            return False

        