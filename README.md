# parallel-map
a threaded version of the inbuilt map() function (for parallel loops)

---

```python
from pmap import parallel_map

list(parallel_map(str,range(10)))
```
>> [2,0,4,1,6,4,9,8,7,5]
