# Last updated: 01/04/2026, 20:43:36
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        up = 0
        left = 0
        down = 0
        right = 0
        maxVal = grid[0][0]
        for elem in grid:
            down += sum(elem)
            right += sum(elem)
            maxVal = max(elem + [maxVal])
        if len(grid) > 2 and len(grid[0]) > 2:
            y = 0
            for elem in grid:
                up += sum(elem)
                down -= sum(elem)
                if up == down:
                    return True
                if up > down:
                    if up - maxVal > down:
                        break
                    if y > 0:
                        for elem in grid[:y + 1]:
                            for subElem in elem:
                                if up - subElem == down:
                                    return True
                    else:
                        if up - grid[0][0] == down or up - grid[0][len(grid[0]) - 1] == down:
                            return True
                else:
                    if down - maxVal <= up:
                        if y < len(grid) - 1:
                            for elem in grid[y + 1:]:
                                for subElem in elem:
                                    if down - subElem == up:
                                        return True
                        else:
                            if down - grid[len(grid) - 1][0] == up or down - grid[len(grid) - 1][len(grid[0]) - 1] == up:
                                return True
                y += 1
            x = 0
            while x < len(grid[0]):
                y = 0
                while y < len(grid):
                    left += grid[y][x]
                    right -= grid[y][x]
                    y += 1
                if left == right:
                    return True
                if left > right:
                    if left - maxVal > right:
                        break
                    if x > 0:
                        xind = 0
                        while xind <= x:
                            yind = 0
                            while yind < len(grid):
                                if left - grid[yind][xind] == right:
                                    return True
                                yind += 1
                            xind += 1
                    else:
                        if left - grid[0][0] == right or left - grid[len(grid) - 1][0] == right:
                            return True
                else:
                    if right - maxVal <= left:
                        if x < len(grid[0]) - 1:
                            xind = x + 1
                            while xind < len(grid[0]):
                                yind = 0
                                while yind < len(grid):
                                    if right - grid[yind][xind] == left:
                                        return True
                                    yind += 1
                                xind += 1
                        else:
                            if right - grid[0][len(grid[0]) - 1] == left or right - grid[len(grid) - 1][len(grid[0]) - 1] == left:
                                return True
                x += 1
        elif len(grid) > 1 and len(grid[0]) > 1:
            y = 0
            for elem in grid:
                up += sum(elem)
                down -= sum(elem)
                if up == down:
                    return True
                if up > down:
                    if up - maxVal > down:
                        break
                    if up - grid[0][0] == down or up - grid[0][len(grid[0]) - 1] == down:
                                return True
                else:
                    if down - maxVal <= up:
                        if down - grid[len(grid) - 1][0] == up or down - grid[len(grid) - 1][len(grid[0]) - 1] == up:
                            return True
                y += 1
            x = 0
            while x < len(grid[0]):
                y = 0
                while y < len(grid):
                    left += grid[y][x]
                    right -= grid[y][x]
                    y += 1
                if left == right:
                    return True
                if left > right:
                    if left - maxVal > right:
                        break
                    if left - grid[0][0] == right or left - grid[len(grid) - 1][0] == right:
                        return True
                else:
                    if right - maxVal <= left:
                        if right - grid[0][len(grid[0]) - 1] == left or right - grid[len(grid) - 1][len(grid[0]) - 1] == left:
                            return True
                x += 1
        else:
            for elem in grid:
                up += sum(elem)
                down -= sum(elem)
                if up == down:
                    return True
                if up > down:
                    if up - maxVal > down:
                        break
                    if up - grid[0][0] == down or up - grid[0][len(grid[0]) - 1] == down or up - elem[0] == down:
                                return True
                else:
                    if down - maxVal <= up:
                        if down - grid[len(grid) - 1][0] == up or down - grid[len(grid) - 1][len(grid[0]) - 1] == up:
                            return True
            x = 0
            while x < len(grid[0]):
                y = 0
                while y < len(grid):
                    left += grid[y][x]
                    right -= grid[y][x]
                    y += 1
                if left == right:
                    return True
                if left > right:
                    if left - maxVal > right:
                        break
                    if left - grid[0][0] == right or left - grid[len(grid) - 1][0] == right or left - grid[y - 1][x] == right:
                        return True
                else:
                    if right - maxVal <= left:
                        if right - grid[0][len(grid[0]) - 1] == left or right - grid[len(grid) - 1][len(grid[0]) - 1] == left:
                            return True
                x += 1
        return False