class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = l + len(s1)
        counts = [0] * 26
        checker = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            checker[ord(s1[i]) - ord('a')] += 1
            counts[ord(s2[i]) - ord('a')] += 1

        if checker == counts:
            return True


        l = 0
        for r in range(len(s1), len(s2)):
            # Add the new character on the right
            counts[ord(s2[r]) - ord('a')] += 1
            # Remove the old character on the left
            counts[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
            # Check if the frequencies match
            if checker == counts:
                return True
                
        return False



        