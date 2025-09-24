class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        if numerator*denominator >0:
            neg=False

        else:
            neg=True

        num=abs(numerator)
        den=abs(denominator)
        if neg:
            res='-'

        else:
            res=''

        res+=str(num//den)
        res+='.'

        arr=set()
        lst=[]
        s=''
        while True:
            rem=num%den
            num=rem*10
            q=num//den
            if rem==0:
                break

            if (num,q) in arr:
                ind=lst.index((num,q))
                s=s[0:ind]+f'({s[ind:]})'
                break

            else:
                arr.add((num,q))
                lst.append((num,q))
                s+=str(q)

        res+=s
        res=res.rstrip(".")

        return res
