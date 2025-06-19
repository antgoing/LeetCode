class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        Solution = ""
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                Solution = Solution + word1[i]
                print(i)
            if i < len(word2):
                Solution = Solution + word2[i]
                print(i)
            else:
                continue
            
        return Solution

word = Solution()
print(word.mergeAlternately("abcd", "pq"))