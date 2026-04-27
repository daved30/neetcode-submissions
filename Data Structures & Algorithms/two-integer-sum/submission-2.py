class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            if num in count:
                return [count[num], i]
            count[diff] = i
        return [0, 0]