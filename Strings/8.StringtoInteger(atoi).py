class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=''
        sgn=''
        s=s.lstrip(" ")
        print(s)
        chk=0
        count=0
        for i in s:
            if i=='+' or i=='-':
                if chk==1:
                    break

                if count==1:
                    return 0
                sgn=i
                count+=1
                continue

            if i.isdigit():
                num+=i
                chk=1

            else:
                break

        num=num.lstrip('0')

        if not num:
            return 0

        print(num)
        num=int(num)

        if sgn=='-':
            res=-(num)

        else:
            res=num

        if res<-(2**31):
            return -(2**31)

        elif res>((2**31)-1) :
            return (2**31)-1

        return res
        
        