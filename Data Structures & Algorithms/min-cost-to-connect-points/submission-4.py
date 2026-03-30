class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build edges
        N = len(points)

        edges = defaultdict(list) # {i : [[dist, target]]}

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges[i].append([dist, j])
                edges[j].append([dist, i])
        
        minHeap = [(0, 0)] # [(dist, target)]
        visit = set()
        cost = 0

        while len(visit) < N:
            dist, target = heapq.heappop(minHeap)
            if target in visit:
                continue

            visit.add(target)
            cost += dist

            for neiCost, nei in edges[target]:
                if nei not in visit:
                    heapq.heappush(minHeap, (neiCost, nei))
        
        return cost