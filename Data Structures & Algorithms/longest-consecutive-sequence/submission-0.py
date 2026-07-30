class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maximum = 0

        for num in numSet:
            if num - 1 not in numSet:
                localMaximum = 1
                current = num
                while current + 1 in numSet:
                    current += 1
                    localMaximum += 1
                if localMaximum > maximum:
                    maximum = localMaximum

        return maximum
        