# Last updated: 01/05/2026, 11:51:45
1# Added using AI
2class Robot:
3    def __init__(self, width: int, height: int):
4        self.x = 0
5        self.y = 0
6        self.dir = "East"
7        self.width = width
8        self.height = height
9
10    def step(self, num: int) -> None:
11        perim = 2 * (self.width - 1) + 2 * (self.height - 1)
12        num %= perim
13        if num == 0:
14            num = perim
15
16        while num > 0:
17            if self.dir == "East":
18                maxX = min(self.x + num, self.width - 1)
19                rem  = num - (maxX - self.x)
20                num  = rem
21                if rem == 0: self.x = maxX
22                else:        self.x = maxX; self.dir = "North"
23            elif self.dir == "West":
24                minX = max(self.x - num, 0)
25                rem  = num - (self.x - minX)
26                num  = rem
27                if rem == 0: self.x = minX
28                else:        self.x = minX; self.dir = "South"
29            elif self.dir == "North":
30                maxY = min(self.y + num, self.height - 1)
31                rem  = num - (maxY - self.y)
32                num  = rem
33                if rem == 0: self.y = maxY
34                else:        self.y = maxY; self.dir = "West"
35            elif self.dir == "South":
36                minY = max(self.y - num, 0)
37                rem  = num - (self.y - minY)
38                num  = rem
39                if rem == 0: self.y = minY
40                else:        self.y = minY; self.dir = "East"
41
42    def getPos(self): return [self.x, self.y]
43    def getDir(self): return self.dir