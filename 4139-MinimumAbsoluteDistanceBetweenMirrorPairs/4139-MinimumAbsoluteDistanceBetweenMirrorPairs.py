# Last updated: 5/18/2026, 5:00:37 PM


# Submitted by Samy Vilar <samy_vilar> on 02/14/2026

# Apply a scan-line approach while maintaining all possible
# "matchings" along w/ their corresponding offsets w/i
#  hash-table; For each new item we query our hashtable
# yielding some kind of -inf should there be no matches
# all the while updating our solution if some new lesser
# delta has being witnessed;
# Afterwhich we update our table w/ said current items
# reversed/rotated representation;

# Overall this would take O(n * log10(max(nums))) time w/ 
# O(n) additional-space contignent upon hashing;

# We can remove said contingency by generating all rotations
# then stably arg-sorting said rotations, then we apply
# binary-search, or we could also (stably) arg-sort nums and 
# merge then still regardless of which approach we take this 
# would take O(n * (log10(max(nums)) + log(n))) time 
# w/ O(n) additional-space;

# version 1.1

# version 1.1.1

import numpy

def minMirrorPairDistance(
    nums: List[int],
    indices=numpy.arange(100_000, dtype=numpy.uint64),
    items=numpy.empty(100_001, dtype=numpy.uint64)
) -> int:    
    rots = numpy.fromstring(
        repr(nums)[-2:0:-1], sep=',', dtype=numpy.uint64
    )[::-1]
    rots <<= 32
    rots += (indices := indices[:rots.size])    
    rots.sort()          

    items = items[:len(nums) + 1]
    items[:-1] = nums    
    items <<= 32
    items[:-1] += indices
    items[-1] = 0xFFFFFFFFFFFFFFFF
    items.sort()
    items = items[items.searchsorted(rots, side='right')]    
    items -= rots
    return items[items < 100_000]       \
        .min(initial=0xFFFFFFFFFFFFFFFF)\
        .view(numpy.int64)              \
        .item()
    
    # solution = 100_001
    # indices = {}
    # for at, item in enumerate(nums):        
    #     if (candidate := at - indices.get(item, -200_001)) < solution:
    #         solution = candidate        
    #     indices[int(str(item)[::-1])] = at
    # return solution if solution != 100_001 else -1

Solution = repeat(namedtuple('Solution', ('minMirrorPairDistance',))(
    minMirrorPairDistance
)).__next__
        