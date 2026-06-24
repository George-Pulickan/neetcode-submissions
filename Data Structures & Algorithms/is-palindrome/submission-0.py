class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return False

        cleaned = "".join(char for char in s if char.isalnum()).lower()

        return cleaned == cleaned[::-1]
        