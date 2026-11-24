class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    
        k = 0

        for n in nums:
            if n != val:
                nums[k] = n # take the value n and store it at position k in the list nums
                k += 1 # element is kept
    
        return k