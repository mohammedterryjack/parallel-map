from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Generator, Iterable

def parallel_map(process: callable, iterable: Iterable) -> Generator[Any, None, None]:
    with ThreadPoolExecutor(max_workers=8) as executor:
        results = []
        for item in iterable:
            results.append(executor.submit(process, item))
        for completed_result in as_completed(results):
            yield completed_result.result()
