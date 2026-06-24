class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""

        for i in range(min(len(word1), len(word2))):
            new_string += word1[i] + word2[i]


        if len(word1) > len(word2):
            new_string += word1[min(len(word1), len(word2)):]
        elif len(word1) < len(word2):
            new_string += word2[min(len(word1), len(word2)):]


        return new_string
        