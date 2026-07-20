class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.cap = capacity
        self.cache = dq = deque([])
        self.size = 0
        

    def get(self, key: int) -> int:
        print(self.mapping)
        return -1 if key not in self.mapping else self.mapping[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.mapping:
            self.size += 1
        self.mapping[key] = value
        self.cache.append(key)
        
        # in case of overflow:
        while self.size > self.cap:
            value = self.cache.popleft()
            if value in self.mapping:
                self.mapping.pop(value)
                self.size -= 1
            else: 
                continue



        
        
