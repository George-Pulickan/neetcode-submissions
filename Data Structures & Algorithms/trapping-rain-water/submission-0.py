class Solution:
    def trap(self, height):
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        total = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                total += left_max - height[l]
                l += 1
            else:
                total += right_max - height[r]
                r -= 1

        return total
    