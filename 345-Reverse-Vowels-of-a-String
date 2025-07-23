class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowel_list = 'aeiouAEIOU'
        l = 0
        r = len(s)-1
        while l < r:
            if s[l] not in vowel_list:
                l+=1

            elif s[r] not in vowel_list:
                r-=1

            else:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
                
        answer = ''.join(s)
        return answer
