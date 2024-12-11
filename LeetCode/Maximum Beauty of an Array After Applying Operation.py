from typing import List

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        max_beauty = 1

        left = 0
        for right in range(n):
            # Keep the range valid: nums[right] - nums[left] <= 2 * k
            while nums[right] - nums[left] > 2 * k:
                left += 1

            # Update the maximum size of the valid subarray
            max_beauty = max(max_beauty, right - left + 1)

        return max_beauty
