# Python Built-in Libraries for DS&A

## `collections` — Enhanced Data Structures:
1. `deque`
* Why: Faster append/popleft for queues and sliding windows
* Use in: BFS, sliding window max/min
```
from collections import deque
queue = deque()
queue.append(1)
queue.popleft()
```

2. `Counter`
* Why: Quickly count elements, like a frequency map
* Use in: Anagram checks, top K frequent elements
```
from collections import Counter
freq = Counter("hello")
freq['l']  # returns 2
```

3. `defaultdict`
* Why: Dictionary with default value, no need for key checks
* Use in: Graphs (adjacency list), frequency/grouping problems
```
from collections import defaultdict
graph = defaultdict(list)
graph[0].append(1)
```

4. `OrderedDict`
* Why: Maintains insertion order (Python 3.6+ does this by default, but still useful)
* Use in: LRU cache design (or use functools.lru_cache)
```
from collections import OrderedDict
od = OrderedDict()
od['a'] = 1
```

5. `namedtuple` — Lightweight Structs
* Why: Define simple classes/records with named fields for clarity
* Use in: Graphs, geometry, simulation, improving readability
```
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(3, 4)
print(p.x, p.y)  # 3 4
```

## `heapq` — Heap / Priority Queue
* Why: Efficient min-heaps, use -x for max-heap behavior
* Use in: Top K elements, merge sorted arrays/lists, Dijkstra
```
import heapq
heap = []
heapq.heappush(heap, 3)
heapq.heappop(heap)
heapq.nlargest(3, [1,8,3,5])  # returns top 3
```

## `sort()` and `sorted()` — Built-in Sorting
* Why: Fast and stable Timsort algorithm (O(n log n)); key and reverse allow custom sorts
* Use in: Greedy problems, sorting intervals, sorting by frequency
```
nums = [4, 1, 3, 2]
nums.sort()                    # modifies in place
sorted_nums = sorted(nums)    # returns new list

# Sort by second element
pairs = [(1, 3), (2, 2), (3, 1)]
pairs.sort(key=lambda x: x[1])  # [(3, 1), (2, 2), (1, 3)]
```
## `map()` — Functional Mapping
* Why: Apply a function to each element of an iterable, more readable than loops
* Use in: Data transformation, preprocessing
```
nums = ["1", "2", "3"]
ints = list(map(int, nums))  # [1, 2, 3]
```
## `zip()` — Combine Iterables
* Why: Pair elements from multiple lists — useful for pairing indices and values
* Use in: Matrix manipulations, custom sorting
```
a = [1, 2, 3]
b = ['a', 'b', 'c']
z = list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]
```

## `bisect` — Binary Search Helpers
* Why: Binary search over sorted lists
* Use in: Insertion while maintaining sort order
```
import bisect
arr = [1, 3, 4, 6]
i = bisect.bisect_left(arr, 4)  # returns 2
bisect.insort(arr, 5)  # inserts 5 in sorted position
```

## `itertools` — Powerful Iterators
* Why: Tools for permutations, combinations, product, infinite iterators
* Use in: Backtracking, combinatorics
```
from itertools import permutations, combinations, product
list(permutations([1,2,3]))      # all perms
list(combinations([1,2,3], 2))   # all 2-combs
```

## `functools` — Functional Tools
1. `lru_cache`
* Why: Built-in memoization for recursive DP
```
from functools import lru_cache

@lru_cache(None)
def fib(n):
    if n <= 1: return n
    return fib(n-1) + fib(n-2)
```
2. `reduce(function, iterable)`
* Why: Applies a function cumulatively to the items (e.g., sum, product)
* Reduces the iterable to a single value
```
from functools import reduce
reduce(lambda x, y: x + y, [1, 2, 3])  # returns 6

import operator
nums = [1, 2, 3, 4]
product = reduce(operator.mul, nums)  # 24, same as ((((1 * 2) * 3) * 4))
```

## `math` — Mathematical Utilities
* Why: Fast math operations, avoids reinventing
```
import math
math.gcd(48, 18)
math.sqrt(16)
math.factorial(5)
math.ceil(2.1)
```
## `operator` — Fast, Readable Operators
* Why: Functional equivalents of operators
```
from operator import itemgetter
sorted(list_of_tuples, key=itemgetter(1))  # sort by 2nd item
```
## `string` — String Constants
* Why: Clean access to ascii_letters, digits, etc.
```
import string
string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.digits           # '0123456789'
```
## `time`
* Why: Benchmarking performance
```
import time
start = time.time()
# code
print(time.time() - start)
```

## `random`
* Why: Useful in randomized algorithms, testing
```
import random
random.shuffle(arr)
random.randint(1, 10)
```

## `datetime`
```
from datetime import datetime, timedelta, date
# Get Current Time
now = datetime.now()         # current date and time
today = date.today()         # current date only

# Parse String to datetime
dt = datetime.strptime("2025-05-26 14:00", "%Y-%m-%d %H:%M")

# Format datetime to String
formatted = dt.strftime("%B %d, %Y at %I:%M %p")  # 'May 26, 2025 at 02:00 PM'

# Difference Between Dates / Times
start = datetime.strptime("2025-05-26 08:00", "%Y-%m-%d %H:%M")
end = datetime.strptime("2025-05-26 12:30", "%Y-%m-%d %H:%M")
delta = end - start          # timedelta object

delta.total_seconds()        # 16200.0 (seconds)
delta.days                  # 0
delta.seconds               # 16200

# Add / Subtract Time
future = now + timedelta(days=7)         # 7 days from now
past = now - timedelta(hours=2)          # 2 hours ago

# Create a datetime Object Manually
custom = datetime(2025, 5, 26, 14, 30)    # May 26, 2025, 2:30 PM

# Extract Components
dt.year, dt.month, dt.day                # 2025, 5, 26
dt.hour, dt.minute, dt.second            # 14, 30, 0
dt.weekday()                             # 0 = Monday, 6 = Sunday
```