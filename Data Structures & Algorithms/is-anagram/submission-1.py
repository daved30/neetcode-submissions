class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ha, hb = dict(), dict()
        for i in s:
            if i in ha.keys():
                ha[i] += 1
            else:
                ha[i] = 1
        for j in t:
            if j in hb.keys():
                hb[j] += 1
            else:
                hb[j] = 1
        if ha == hb:
            return True
        return False