class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        if s == "":
            return True
        while (j < len(t) and i < len(s)):
            if s[i] == t[j]:
                i+=1
                j+=1
            else:
                j+=1

        return len(s) == i
