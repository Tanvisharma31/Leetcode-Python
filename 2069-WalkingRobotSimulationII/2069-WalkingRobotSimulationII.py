# Last updated: 01/05/2026, 11:52:23
class Robot:

    def __init__(self, width: int, height: int):
        self.steps = 0
        self.width = width
        self.height = height
        self.tot = 2*(width + height-2)

    def step(self, num: int) -> None:
        self.steps += num

    def getPos(self) -> List[int]:
        width, height = self.width, self.height
        temp = (self.steps) % self.tot
        if temp < width: 
            return (temp, 0)
        if temp < width + height - 1: 
            return (width-1, temp - (width - 1))
        if temp < 2*width + height - 2:
            return (width-(temp-(width+height-3)), height-1)
        return (0, height-(temp-(2*width+height-4)))

    def getDir(self) -> str:
        x, y = self.getPos()
        if (x, y) == (0, 0) and self.steps > 0: return 'South'
        if y == 0: return 'East'
        if x == self.width-1: return 'North'
        if y == self.height-1: return 'West'
        return 'South'


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()