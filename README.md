# parallel-map
a threaded version of the inbuilt map() function (for parallel loops)

---
example
```python
from time import sleep, time

def do_something_that_takes_ages(value:int) -> int:
    sleep(value)
    print(value)
    return value
    
```

> normal loop:

```python
start = time()
list(map(do_something_that_takes_ages,range(5,0,-1)))
end = time()
print(f"duration = {end-start}")
```
5 <br />
4 <br />
3 <br />
2 <br />
1 <br />
[5,4,3,2,1] <br />
duration = 15.025775909423828

> parallel loop:

```python
from pmap import parallel_map

start = time()
list(parallel_map(do_something_that_takes_ages,range(5,0,-1)))
end = time()
print(f"duration = {end-start}")
```
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
[1, 2, 3, 4, 5] <br />
duration = 5.005711078643799
