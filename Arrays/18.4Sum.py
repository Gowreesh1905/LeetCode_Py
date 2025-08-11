class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        nums.sort()
        st=[]

        for l in range(n):
            if(l>0 and nums[l]==nums[l-1]):
                    continue
            for i in range(l+1,n):
                if(i>l+1 and nums[i]==nums[i-1]):
                    continue
                j=i+1
                k=n-1

                while j<k:
                    s=nums[i]+nums[j]+nums[k]+nums[l]
                    if s==target:
                        st.append([nums[l],nums[i],nums[j],nums[k]])
                        j+=1
                        k-=1
                        while(j<k and nums[j]==nums[j-1]):
                            j+=1

                        while(j<k and nums[k]==nums[k+1]):
                            k-=1

                        

                    elif s<target:
                        j+=1

                    else:
                        k-=1
                
        return st
        