import math

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n=len(complexity)
        mod=10**9+7
        n0=complexity[0]
        for i in range(1,n):
            if complexity[i]<=n0:
                return 0

        ans=math.factorial(n-1)%mod

        return ans