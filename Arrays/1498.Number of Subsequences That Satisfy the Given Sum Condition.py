class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        temp=0
        while l<=r:
            if nums[l]+nums[r]<=target:
                temp+=2**(r-l)
                l+=1
                

            else:
                r-=1

        return (temp)%(10**9+7)





