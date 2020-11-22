from typing import List
import heapq
from collections import deque


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        while counter != k:
            last = nums[-1]
            nums.pop()
            nums.insert(0, last)
            counter += 1
            print(nums)

    def rotate_modify_array(self, nums: List[int], k: int) -> None:
        counter = 0
        if nums:
            while counter != k:
                last = nums.pop()
                nums.insert(0, last)
                counter += 1
                print(nums)

            print(nums)


c = Solution()
c.rotate([1, 2, 3, 4, 5, 6, 7], 3)
c.rotate_modify_array([], 1)
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
