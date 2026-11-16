class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        s = [0] * (amount + 1)

        s[0] = 1

        for coin in coins:
            for i in range(1, amount+1):
                if i - coin >= 0:
                    s[i] += s[i-coin]
        
        return s[-1]

        
        # [1, 1, 2, 3, 0] (combo: (1, 2))
        # coins = [1, 2, 3]