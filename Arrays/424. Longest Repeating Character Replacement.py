class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mapp={}

        for i in s:
            
            mapp[i]=0

        
        res=0
        n=len(s)
        
        for i in mapp:
            l=0
            r=0
            c=0

            while r<n:
                
                if s[r]!=i:
                    c+=1
                    
                while c>k:
                    if s[l]!=i:
                        c-=1

                    l+=1

                res=max(res,r-l+1)
                r+=1

        return res





        



        
        