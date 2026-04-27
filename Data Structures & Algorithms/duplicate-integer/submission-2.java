class Solution {
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 1) {
            return false;
        }
        HashSet<Integer> hs = new HashSet<>();
        for (int i: nums) {
            if (hs.contains(i)) {
                return true;
            }
            hs.add(i);
        }
        return false;
    }
}