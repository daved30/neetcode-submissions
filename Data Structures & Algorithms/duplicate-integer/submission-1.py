class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hs = set()
        n = len(nums)
        if n == 1:
            return False
        for i in nums:
            if i in hs:
                return True
            else:
                hs.add(i)
        return False