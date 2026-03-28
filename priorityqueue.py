import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def pop(self):
        if not self.heap:
            return "Empty"
        return heapq.heappop(self.heap)[1]

    def display(self):
        print(self.heap)
    
pq=PriorityQueue()
pq.push(5,'C')
pq.push(8,'A')
print(pq.display())