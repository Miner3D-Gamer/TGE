from typing import Any
class concurrent:
    class futures:
        class ThreadPoolExecutor:
            def __init__(self)->None:
                "..."
                pass
            def submit(self, *args: Any, **kwargs: Any)->Any:
                "..."
                pass
            def result(self, *args: Any, **kwargs: Any)->Any:
                "..."
                pass
        class TimeoutError(Exception):
            pass