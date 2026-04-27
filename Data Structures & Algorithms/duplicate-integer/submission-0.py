class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return False
        hs = set()
        for i in nums:
            hs.add(i)
        if len(nums) == len(hs):
            return False
        return True