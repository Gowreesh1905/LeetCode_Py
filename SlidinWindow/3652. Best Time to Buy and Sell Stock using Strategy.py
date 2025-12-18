class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        pref = 0
        ppref = 0
        mapp = {-1: 0}
        p_mapp = {-1: 0}

        n = len(prices)

        for i in range(n):
            pref += prices[i] * strategy[i]
            ppref += prices[i]
            mapp[i] = pref
            p_mapp[i] = ppref
        
        total_profit = pref 
        ans = 0 

        for j in range(0, n - k + 1):
            l = j
            r = j + k - 1

            curr = mapp[r] - mapp[l-1]
            
            d = k // 2
            new = p_mapp[r] - p_mapp[l + d - 1]

            diff = new - curr

            ans = max(ans, diff)

        return total_profit + ans