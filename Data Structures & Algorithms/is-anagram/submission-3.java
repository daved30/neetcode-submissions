class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> first = new HashMap<>();
        HashMap<Character, Integer> second = new HashMap<>();
        for (Character cFirst : s.toCharArray()) {
            first.put(cFirst, first.getOrDefault(cFirst, 0) + 1);
        }
        System.out.println("First: " + first);
        for (Character cSecond : t.toCharArray()) {
            second.put(cSecond, second.getOrDefault(cSecond, 0) + 1);
        }
        System.out.println("Second: " + second);
        return first.equals(second);
    }
}
