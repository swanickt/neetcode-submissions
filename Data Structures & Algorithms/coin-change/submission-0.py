class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        s = [-1] * (amount + 1)
        
        s[0] = 0
        for i in range(1, amount + 1):

            s[i] = amount + 1
            for coin in coins:
                if i - coin >= 0:
                    if s[i - coin] != -1:
                        s[i] = min(s[i], 1 + s[i - coin])
                    
            if s[i] == amount + 1:
                s[i] = -1
        
        return s[amount]
        