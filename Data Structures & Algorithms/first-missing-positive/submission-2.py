class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):

            # filters out for at least 1 and at most n while its place is not taken by the same number
            
            while 0 < nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # index where nums[i] is
                correct = nums[i] - 1
                
                # swap nums[i] with nums[correct], so the number lands at its correct index
                temp = nums[i]
                nums[i] = nums[correct]
                nums[correct] = temp
        
        # find the first index where the wrong number is, that index + 1 is the missing number
        for j in range(n):
            if nums[j] != j + 1:
                return j + 1
        # first missing num returned
        return n + 1