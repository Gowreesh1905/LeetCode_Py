class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        mapp={}

        for i in nums:
            mapp[i]=-1

        l=0
        r=0
        n=len(nums)
        k=len(mapp)
        uniq=[]
        res1=0
        while r<n:
            mapp[nums[r]]=r
            
            if nums[r] not in uniq:
                uniq.append(nums[r])

            if len(uniq)>k:
                l=min(mapp[i] for i in uniq)
                uniq.remove(nums[l])
                l+=1

            res1+=(r-l+1)

            r+=1

        l=0
        r=0
        n=len(nums)
        k=len(mapp)-1
        uniq=[]
        res2=0

        for i in nums:
            mapp[i]=-1


        while r<n:
            mapp[nums[r]]=r
            
            if nums[r] not in uniq:
                uniq.append(nums[r])

            if len(uniq)>k:
                l=min(mapp[i] for i in uniq)
                uniq.remove(nums[l])
                l+=1

            res2+=(r-l+1)

            r+=1
        print(res1)
        print(res2)
        return res1-res2
