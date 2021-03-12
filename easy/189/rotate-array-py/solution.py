from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        nums_copy = nums.copy()

        for idx in range(0, len(nums_copy)):
            num_from_input = nums_copy[idx]
            new_idx_location = (k + idx) % len(nums_copy)
            nums[new_idx_location] = num_from_input

        return nums


c = Solution()

print(c.rotate([1, 2, 3, 4, 5, 6, 7], 1))
