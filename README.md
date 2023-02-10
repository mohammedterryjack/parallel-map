# parallel-map
a threaded version of the inbuilt map() function (for parallel loops)

---
example
```python
from time import sleep

def do_something_that_takes_ages(value:int) -> int:
    sleep(value)
    print(value)
    return value

example_values = range(5,0,-1)
```

> normal loop:

```python
result = map(do_something_that_takes_ages,example_values)
list(result)
```
5 <br />
4 <br />
3 <br />
2 <br />
1 <br />
[5,4,3,2,1] <br />
(duration = 15s)

> parallel loop:

```python
from pmap import parallel_map

result =parallel_map(do_something_that_takes_ages,example_values)
list(result)
```
1 <br />
2 <br />
3 <br />
4 <br />
5 <br />
[1, 2, 3, 4, 5] <br />
(duration = 5s)
