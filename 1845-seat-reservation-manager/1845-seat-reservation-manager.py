import heapq

class SeatManager:
    def __init__(self, n: int):
        self.available= [i for i in range(1, n + 1)]  
        heapq.heapify(self.available)  

    def reserve(self) -> int:
        if self.available:
            return heapq.heappop(self.available)
        else:
            return -1 

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.available, seatNumber)