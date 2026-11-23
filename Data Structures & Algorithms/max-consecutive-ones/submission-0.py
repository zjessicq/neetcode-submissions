class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0
        for n in nums: # go through nums one at a time and let n be that element
            if n == 1:
                current += 1
            else:
                current = 0
            best = max(current, best)
        return best