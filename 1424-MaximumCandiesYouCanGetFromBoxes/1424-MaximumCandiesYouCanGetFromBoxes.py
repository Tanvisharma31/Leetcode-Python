# Last updated: 02/03/2026, 14:00:38
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        toOpen = []
        availBoxes = []
        availKeys = []
        maxCandies = 0
        for box in initialBoxes:
            availKeys.extend(keys[box])
            if status[box] == 1:
                toOpen.append(box)
            elif status[box] == 0 and box in availKeys:
                toOpen.append(box)
            else:
                availBoxes.append(box)

        
        while len(toOpen):
            box = toOpen.pop(0)
            maxCandies += candies[box]
            availBoxes.extend(containedBoxes[box])
            availKeys.extend(keys[box])
            for newBox in availBoxes:
                if status[newBox] == 1:
                    toOpen.append(newBox)
                    availBoxes.remove(newBox)
                elif status[newBox] == 0 and newBox in availKeys:
                    toOpen.append(newBox)
                    availBoxes.remove(newBox)
        
        return maxCandies
