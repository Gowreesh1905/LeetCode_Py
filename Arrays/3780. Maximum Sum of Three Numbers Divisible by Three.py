class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapp={0:[],1:[],2:[]}

        n=len(nums)

        for i in range(n):
            num=nums[i]
            mapp[num%3].append(num)

        if (mapp[0]==[] or mapp[1]==[] or mapp[2]==[]) and (len(mapp[0])<3 and len(mapp[1])<3 and len(mapp[2])<3):
            return 0

        
        max1=0
        max2=0

        if (mapp[0]==[] or mapp[1]==[] or mapp[2]==[]):
            pass
            

        else:
            for key in mapp:
                lst=mapp[key]

                max1+=max(lst)

        for key in mapp:
            if len(mapp[key])>=3:
                lst=mapp[key]
                lst.sort(reverse=True)
                summ=lst[0]+lst[1]+lst[2]
                max2=max(max2,summ)
        print(max1,max2)
        return max(max1,max2)

        
