class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = [(v, t) for v, t in self.cache[key]]

        left = 0
        right = len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] < timestamp:
                res = values[mid][0]
                left = mid + 1
            elif values[mid][1] == timestamp:
                res = self.cache[key][mid][0]
                return res
            else:
                right = mid - 1
        return res 
