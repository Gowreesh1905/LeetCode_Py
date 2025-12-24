class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])

        ans=0
        arr=['' for k in range(n)]
        for i in range(m):
            s=arr[0]+strs[0][i]
            chk=0
            for j in range(1,n):
                if arr[j]+strs[j][i]<s:
                    ans+=1
                    chk=1
                    print(i)
                    break

                s=arr[j]+strs[j][i]

            if chk==0:
                for k in range(n):
                    arr[k]+=strs[k][i]


        return ans
