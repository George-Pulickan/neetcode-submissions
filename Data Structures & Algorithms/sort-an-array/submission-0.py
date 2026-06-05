class Solution:
    def sortArray(self, arr: List[int]) -> List[int]:
         if len(arr) <= 1:
            return arr

    # Step 1: Divide the array into two halves
         mid = len(arr) // 2
         left_half = arr[:mid]
         right_half = arr[mid:]

    # Step 2: Conquer (Recursively sort both halves)
         self.sortArray(left_half)
         self.sortArray(right_half)

    # Step 3: Combine (Merge the sorted halves back into the original array)
         i = j = k = 0

    # Copy data to temporary arrays left_half[] and right_half[]
         while i < len(left_half) and j < len(right_half):
          if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
          else:
            arr[k] = right_half[j]
            j += 1
          k += 1

    # Checking if any elements were left in the left_half
         while i < len(left_half):
           arr[k] = left_half[i]
           i += 1
           k += 1

    # Checking if any elements were left in the right_half
         while j < len(right_half):
           arr[k] = right_half[j]
           j += 1
           k += 1
        
         return arr