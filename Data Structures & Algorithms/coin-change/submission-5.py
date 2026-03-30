class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in cache:
                return cache[amount]
            
            minCoins = float('inf')
            for coin in coins:
                if amount - coin >= 0:
                    minCoins = min(minCoins, 1 + dfs(amount - coin))
            
            cache[amount] = minCoins
            return cache[amount]
        
        res = dfs(amount)
        return res if res != float('inf') else -1