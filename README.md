# parallel-map
a threaded version of the inbuilt map() function (for parallel loops)

---

```python
list(map(str,range(10)))
```
>[0,1,2,3,4,5,6,7,8,9]

```python
from pmap import parallel_map

list(parallel_map(str,range(10)))
```
> [2,0,4,1,6,4,9,8,7,5]
