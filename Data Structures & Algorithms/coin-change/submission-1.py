class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # s[i] = fewest number of cons to make amount i

        # s[0] = 0

        # s[i] = min{s[i-coin] for coin in coins: i-coin is possible}
        #        or -1 if not possible

        # answer: s[n]

        s = [0]

        for i in range(1, amount + 1):
            fewest = amount + 1
            for coin in coins:
                if i - coin >= 0 and s[i - coin] != -1:
                    fewest = min(fewest, 1 + s[i - coin])
            
            if fewest == amount + 1:
                s.append(-1)
            
            else:
                s.append(fewest)
        
        return s[amount]

        

        