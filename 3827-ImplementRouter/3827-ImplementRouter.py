# Last updated: 02/03/2026, 13:56:07
from collections import deque
import bisect

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.deque = deque()
        self.seen = set()
        self.dest_to_list = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.seen:
            return False
            
        self.seen.add(key)
        self.deque.append(key)
        
        if destination not in self.dest_to_list:
            self.dest_to_list[destination] = []
            
        bisect.insort(self.dest_to_list[destination], timestamp)
        
        if len(self.deque) > self.memoryLimit:
            old_key = self.deque.popleft()
            self.seen.remove(old_key)
            d_old = old_key[1]
            t_old = old_key[2]
            lst = self.dest_to_list[d_old]
            idx = bisect.bisect_left(lst, t_old)
            del lst[idx]
            
        return True

    def forwardPacket(self) -> list:
        if not self.deque:
            return []
        packet = self.deque.popleft()
        self.seen.remove(packet)
        d = packet[1]
        t = packet[2]
        lst = self.dest_to_list[d]
        idx = bisect.bisect_left(lst, t)
        del lst[idx]
        return [packet[0], packet[1], packet[2]]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_to_list:
            return 0
        arr = self.dest_to_list[destination]
        left = bisect.bisect_left(arr, startTime)
        right = bisect.bisect_right(arr, endTime)
        return right - left