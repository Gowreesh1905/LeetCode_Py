class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        l=0
        r=0
        c=0
        n=len(nums)
        ans=0

        mapp=[1 for i in range(n)]

        for i in range(n):
            if nums[i]==0:
                mapp[i]=1

            else:
                mapp[i]=0

        mapp=nums
        z=0 
        while r<n:
            if mapp[r]==1:
                z+=1

           
            while z>k:
                if mapp[l]==1:
                    z-=1
                l+=1

            ans+=(r-l+1)
            r+=1

        if k==0:
            return ans
        r=0
        l=0
        z=0
        while r<n:
            if mapp[r]==1:
                z+=1 

            while z>(k-1):
                if mapp[l]==1:
                    z-=1
                l+=1

                
               
            c+=(r-l+1)
            r+=1
            
            

        return ans-c
        