class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i : [] for i in range(N)} # {i : [[cost, target], [cost2, target2]]}
        

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        minHeap = [(0, 0)] # [(cost, target)]
        visit = set()

        while len(visit) < N:
            cost, target = heapq.heappop(minHeap)
            if target in visit:
                continue
            
            visit.add(target)
            res += cost
            for neiCost, nei in adj[target]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiCost, nei))
        return res