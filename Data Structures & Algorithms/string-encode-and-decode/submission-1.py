class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""

        for item in strs:
            encoded_string += "‽" + item
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
       decoded_words = s.split("‽")
       decoded_words.remove("")

       return decoded_words
