class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> hs = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int diff = target - num;
            if (hs.containsKey(diff)) {
                return new int[] {hs.get(diff), i};
            }
            hs.put(num, i);
        }
        return new int[] {0, 0};
    }
}
