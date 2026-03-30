class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        edges = defaultdict(list)
        res = 0

        for u, v, t in times:
            edges[u].append((v, t))
        
        minHeap = [(0, k)]
        while minHeap:
            t1, v1 = heapq.heappop(minHeap)
            if v1 in visit:
                continue
                
            visit.add(v1)
            res = max(res, t1)

            for v2, t2 in edges[v1]:
                if v2 not in visit:
                    heapq.heappush(minHeap, (res + t2, v2))
        
        return res if len(visit) == n else -1
# [1, 2, 1]
# [2, 3, 1]
# [1, 4, 4]
# [3, 4, 1]

# t = 0
# visit = (1, 2, 3, 4)
# edges = {1 : [[2, 1], [4, 4]], 2 : [3, 1], 3 : [4, 1]}
# minHeap = [(0, 1)]

# w1, n1 = 0, 1 
# visit.add(n1)
# t = max(0, 0) = 0
# n2, w2 = 2, 1
# visit does not have n2 (2)
# minHeap = [(0 + 1, 2)]

# w1, n1 = 1, 2
# visit.add(n1)
# t = max(0, 1) = 1
# n2, w2 = 3, 1
# n2 not in visit
# minHeap = [(1 + 1, 3)]

# w1, n1 = 2, 3
# visit.add(n1) 
# t = max(1, 2) = 2
# n2, w2 = 4, 1
# minHeap = [(2 + 1, 4)]

# w1, n1 = 3, 4
# visit.add(n1)
# t = max(2, 3) = 3
# n2, w2 = does not exist break loop

# len(visit) == n = 4 == 4 
# t = 3
