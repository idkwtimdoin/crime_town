import time


class Stopwatch:
    def __init__(self) -> None:
        self.total_time = 0

    def __enter__(self) -> 'Stopwatch':
        self._start_time = time.perf_counter()
        return self

    def __exit__(self, _type, _value, _traceback) -> None:
        self._total_time = time.perf_counter() - self._start_time
