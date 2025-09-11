class Solution:
    def sortVowels(self, s: str) -> str:
        vowels=['a', 'e', 'i', 'o','u']
        
        n=len(s)
        temp=[]
        for i in range(n):
            
            if s[i].lower() in vowels:
                temp.append(s[i])

        temp.sort()
        res=''
        c=0
        for i in s:
            if i.lower() in vowels:
                res+=temp[c]
                c+=1

            else:
                res+=i
                

        return res
            
