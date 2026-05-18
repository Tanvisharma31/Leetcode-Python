# Last updated: 5/18/2026, 5:01:10 PM
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:

                # Sum rows of the grid or its transpose and 
                # determine whether the equal partition exists
        def partitionExists(arr: list, sm = 0)-> bool:

            for row in arr:
                sm+= sum(row)
                if sm == halfSum: return True
                if sm >  halfSum: return False


                # Determine the target sum for each partition
                # and whether sum(grid) is odd
        halfSum, mod_ = divmod(sum(chain(*grid)), 2)
        if mod_ : return False

                # Check horizontal and vertical partitions
        return (partitionExists(grid) or 
                partitionExists(zip(*grid)))   