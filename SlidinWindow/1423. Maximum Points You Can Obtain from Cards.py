class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        n=len(cardPoints)
        l=0
        r=n-1

        
        lsum=0
        rsum=0
        
        for i in range(k):
            lsum+=cardPoints[i]
            
        l=k-1
        res=lsum
        print(res)
        while l>=0:
            lsum-=cardPoints[l]
            l-=1
            rsum+=cardPoints[r]
            r-=1

            res=max(res,lsum+rsum)

        return res
            