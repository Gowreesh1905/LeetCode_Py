class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        l=0
        r=0
        mapp={}
      
        for i in range(256):
            c=chr(i)
            mapp[c]=-1
        maxi=0
        
        while r<n:
            if mapp[s[r]]>=l:
                l=mapp[s[r]]+1

            maxi=max(maxi,r-l+1)
            mapp[s[r]]=r
            r+=1
            


        return maxi