class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {} # {amount : min number of coins to make}

        def dfs(remaining):
            if remaining == 0:
                return 0
            
            if remaining < 0:
                return float('inf')

            if remaining in cache:
                return cache[remaining]
            
            minCoins = float('inf')
            for coin in coins:
                minCoins = min(minCoins, dfs(remaining - coin) + 1)

            cache[remaining] = minCoins
            return cache[remaining]
        
        res = dfs(amount)
        if res == float('inf'):
            return -1
        else:
            return res