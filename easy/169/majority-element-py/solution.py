from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        # sorted_counts = sorted(counts, key=counts.get, reverse=True)
        return max(counts, key=counts.get)


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))