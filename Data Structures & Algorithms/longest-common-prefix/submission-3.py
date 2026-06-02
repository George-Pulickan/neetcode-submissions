class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for i in range (1,len(strs)):
            if len(strs[i]) < min_len:
                min_len = len(strs[i])
        
        for item in strs:
            if item == "":
                return ""

        for i in range(1,min_len+1):
            prefix = strs[0][:i]
            for item in strs:
                if item[:i] == prefix:
                    continue
                else:
                    return strs[0][:i-1]
        for item in strs:
            if prefix == item:
                return prefix

        