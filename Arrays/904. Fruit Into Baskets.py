class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        l=0
        r=0
        res=0
        n=len(fruits)
        mapp=[-1 for i in range(max(fruits)+1)]
        two=[]

        while r<n:
            mapp[fruits[r]]=r
            if len(two)<2:
                if fruits[r] not in two:
                    two.append(fruits[r])
                


            else:
                if fruits[r] not in two:
                    l=min(mapp[two[0]],mapp[two[1]])
                    two.remove(fruits[l])
                    two.append(fruits[r])

                    l+=1

                
                    
            res=max(res,r-l+1)

            
            
            r+=1
        
        return res



            
        