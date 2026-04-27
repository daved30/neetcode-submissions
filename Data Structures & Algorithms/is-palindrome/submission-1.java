class Solution {
    public boolean isPalindrome(String s) {
        int n = s.length();
        if (n == 0) return false;
        int start = 0;
        int last = n - 1;
        while (start <= last) {
            char a = s.charAt(start);
            char b = s.charAt(last);
            if (!Character.isLetterOrDigit(a)) {
                start++;
            } else if (!Character.isLetterOrDigit(b)) {
                last--;
            } else {
                if (Character.toLowerCase(a) != Character.toLowerCase(b)) {
                    return false;
                }
                start++;
                last--;
            }
        }
        return true;
    }
}
