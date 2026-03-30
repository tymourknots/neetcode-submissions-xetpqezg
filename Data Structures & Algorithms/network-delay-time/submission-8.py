class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in times:
            edges[u].append([v, t])
        
        visit = set()
        minHeap = [(0, k)]
        res = 0

        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
            
            visit.add(v1)
            res = t1

            for v2, t2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (t1 + t2, v2))
        
        return res if len(visit) == n else -1

# {u : [[v, t]]}
# [(t, v)]