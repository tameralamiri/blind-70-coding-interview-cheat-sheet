# Python Data Structures
## `str` (Strings)
| Operation    | Syntax / Example                  |
| ------------ | --------------------------------- |
| Length       | `len(s)`                          |
| Slicing      | `s[start:end]`                    |
| Reverse      | `s[::-1]`                         |
| Join list    | `"".join(chars)`                  |
| Split        | `s.split(delimiter)`              |
| Check prefix | `s.startswith("pre")`             |
| Check suffix | `s.endswith("post")`              |
| Find index   | `s.find("a")` → `-1` if not found |
| Replace      | `s.replace("a", "b")`             |
| Count        | `s.count("x")`                    |
| ASCII tricks | `ord('a')` → 97, `chr(97)` → 'a'  |

## `list` (Dynamic Arrays)
| Operation          | Syntax / Example           |
| ------------------ | -------------------------- |
| Append             | `arr.append(x)`            |
| Insert at index    | `arr.insert(i, x)`         |
| Pop from end/index | `arr.pop()` / `arr.pop(i)` |
| Remove first value | `arr.remove(x)`            |
| Index of value     | `arr.index(x)`             |
| Sort in place      | `arr.sort()`               |
| Return sorted copy | `sorted(arr)`              |
| Reverse in place   | `arr.reverse()`            |
| Reverse copy       | `arr[::-1]`                |
| Slice/replace      | `arr[1:3] = [7, 8]`        |

## `tuple` and `collections.namedtuple`
* Immutable, hashable, can be used as dict/set keys.
```
pair = (x, y)
```
* `namedtuple` same as `tuple` in addition to:
    * more readable than tuples.
    * Acts like a lightweight class without methods.
```
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x  # 3
p.y  # 4
```

## `dict` and `collections.defaultdict`
| Operation        | Syntax / Example         |
| ---------------- | ------------------------ |
| Get / Set        | `d[key] = value`         |
| Get with default | `d.get(key, default)`    |
| Keys / Values    | `d.keys()`, `d.values()` |
| Remove           | `del d[key]`             |
| Iteration        | `for k, v in d.items()`  |
| Key existence    | `if k in d:`             |

* `defaultdict`
    * Automatically initializes missing keys.
    * Default types: int, list, set, etc.
```
from collections import defaultdict
d = defaultdict(list)
d["a"].append(1)
```

## `set`
| Operation         | Syntax / Example |                      |
| ----------------- | ---------------- | -------------------- |
| Add element       | `s.add(x)`       |                      |
| Remove (KeyError) | `s.remove(x)`    |                      |
| Remove (safe)     | `s.discard(x)`   |                      |
| Check existence   | `x in s`         |                      |
| Set union         | \`s1             | s2`or`s1.union(s2)\` |
| Set intersection  | `s1 & s2`        |                      |
| Set difference    | `s1 - s2`        |                      |
| Convert from list | `set(arr)`       |                      |

## `heapq` (Min-Heap)
* Python heaps are min-heaps.
* Use (-x) for max-heap simulation.
```
import heapq

heapq.heappush(heap, x)
heapq.heappop(heap)
heapq.heapify(arr)       # turns list into a heap
heapq.heappushpop(h, x)  # push then pop (more efficient)
heapq.nlargest(k, arr)   # top K max
heapq.nsmallest(k, arr)  # top K min
```

## `Counter` (from collections)
* Best for frequency maps, mode, majority element.
```
from collections import Counter
freq = Counter("banana")  # {'a':3, 'b':1, 'n':2}
freq['a'] += 1
freq.most_common(2)       # [('a', 4), ('n', 2)]
```

## `range`
* Efficient sequence for loops.
```
range(1, 10, 2)  # start, stop, step
```

## `enumerate()`
* Best way to iterate with index and value.
```
for i, val in enumerate(arr):
    ...
```

## `zip(iterable1, iterable2, ...)`
* Combines multiple iterables element-wise
* Returns a tuple for each group
* Useful for iterating pairs, indexing, combining keys and values
```
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))  # [(1, 'a'), (2, 'b'), (3, 'c')]

for x, y in zip(a, b):
    print(x, y)

```

## `map(function, iterable)`
* Applies a function to **each item** in an iterable
* Returns a lazy `map` object → wrap in `list()` or `set()`
```
words = ["hello", "world"]
caps = list(map(str.upper, words)) # ['HELLO', 'WORLD']
list(map(int, ["1", "2"]))         # [1, 2]
squared = list(map(lambda x: x ** 2, [1, 2, 3, 4])) # [1, 4, 9, 16]

```

## `filter(function, iterable)`
* Applies a function to every item in the iterable
* Keeps only items where the function returns True
* Returns a filter object (lazy iterator) — usually wrapped in list()
* Use filter() when you:
    * Want to select elements that satisfy a condition
    * Don't need to transform the data (use map() for that)
    * Prefer concise functional style over a for loop with if

```
list(filter(lambda x: x > 0, [-3, 3, -1, 1])) # [3, 1]
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) # [2, 4, 6]
list(filter(None, ["apple", "", "banana", "", "cherry"])) # ['apple', 'banana', 'cherry']
```