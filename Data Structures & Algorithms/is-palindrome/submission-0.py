class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n == 0:
            return False
        start, last = 0, n - 1
        while start <= last:
            a, b = s[start], s[last]
            if not a.isalnum():
                start += 1
            elif not b.isalnum():
                last -= 1
            else:
                if a.lower() != b.lower():
                    return False
                start += 1
                last -= 1
        return True