# Last updated: 02/03/2026, 13:55:51
from collections import deque
class RideSharingSystem:

    def __init__(self):
        self.rider_queue=deque()
        self.driver_queue=deque()
        self.a_r=set()
    def addRider(self, riderId: int) -> None:
        self.rider_queue.append(riderId)
        self.a_r.add(riderId)

    def addDriver(self, driverId: int) -> None:
        self.driver_queue.append(driverId)

    def matchDriverWithRider(self) -> List[int]:
        if not self.driver_queue:
            return [-1,-1]
        while self.rider_queue:
            r_id=self.rider_queue[0]
            if r_id in self.a_r:
                d_id=self.driver_queue.popleft()
                self.rider_queue.popleft()
                self.a_r.remove(r_id)
                return [d_id,r_id]
            else:
                self.rider_queue.popleft()
        return [-1,-1]

    def cancelRider(self, riderId: int) -> None:
        if riderId in self.a_r:
            self.a_r.remove(riderId)


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)