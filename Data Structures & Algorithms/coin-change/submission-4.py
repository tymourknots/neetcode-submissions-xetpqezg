class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {} # {remaining amount : min coins to get to that amount}

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
        
        minCoins = dfs(amount)
        return minCoins if minCoins != float('inf') else -1