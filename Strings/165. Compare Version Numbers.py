class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1=version1.split(".")
        v2=version2.split(".")
        
        l=min(len(v1),len(v2))

        for i in range(l):
            a=(v1[i].lstrip("0"))
            if a:
                a=int(a)

            else:
                a=0
      
            b=(v2[i].lstrip("0"))

            if b:
                b=int(b)

            else:
                b=0   
           
            
            if a>b:
                return 1

            if b>a:
                return -1

        if len(v1)>len(v2):
            s=''
            for i in range(l,len(v1)):
                s+=v1[i]

            s=s.rstrip("0")

            if s:
                return 1

        elif len(v1)<len(v2):
            s=''
            for i in range(l,len(v2)):
                s+=v2[i]

            s=s.rstrip("0")

            if s:
                return -1
            

        return 0