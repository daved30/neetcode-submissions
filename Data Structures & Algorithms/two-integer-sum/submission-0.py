class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hs = dict()
        for i in range(n):
            num = nums[i]
            diff = target - num
            if diff in hs.keys():
                return [hs.get(diff), i]
            hs[num] = i
        return [0, 0]