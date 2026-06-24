class Solution:
    def validPalindrome(self, s: str) -> bool:
        cleaned = "".join(char for char in s if char.isalnum()).lower()

        if cleaned == cleaned[::-1]:
            return True


        for item in cleaned:
            store_val = cleaned
            store_val = store_val.replace(item,"")
            if store_val == store_val[::-1]:
                return True
        
        return False