class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #hasmap containing count of each char
        res=0

        maxFreqChar=0
        l=0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0)+1
            maxFreqChar = max(maxFreqChar, count[s[r]])

            while (r-l+1) - maxFreqChar > k:
                count[s[l]] -= 1
                l+=1
            res = max(res, r-l +1)

        return res



        