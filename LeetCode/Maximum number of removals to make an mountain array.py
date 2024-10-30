from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    left[i] = max(left[i], left[j] + 1)

        right = [1] * n
        for i in range(n-2, -1, -1):
            for j in range(n-1, i, -1):
                if nums[i] > nums[j]:
                    right[i] = max(right[i], right[j] + 1)

        max_mountain_len = 0
        for i in range(1, n-1):
            if left[i] > 1 and right[i] > 1:
                max_mountain_len = max(max_mountain_len, left[i] + right[i] - 1)

        return n - max_mountain_len

s = Solution()
print(s.minimumMountainRemovals([2,1,1,5,6,2,3,1]))