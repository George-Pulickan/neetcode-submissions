class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        counts = [0] * 26          # frequency of each letter in the window
        n = len(s)

        # O(26 * n) = O(n)
        for r in range(n):
            counts[ord(s[r]) - ord('A')] += 1

            # replacements needed = window size - count of most common char
            while (r - l + 1) - max(counts) > k:
                counts[ord(s[l]) - ord('A')] -= 1
                l += 1

            w = (r - l) + 1
            longest = max(longest, w)

        return longest

        