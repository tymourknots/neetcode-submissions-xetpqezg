class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visit = set()
        res = 0

        def dfs(i):
            for j in adj[i]:
                if j not in visit:
                    visit.add(j)
                    dfs(j)
        
        for i in range(n):
            if i not in visit:
                visit.add(i)
                dfs(i)
                res += 1
        return res
