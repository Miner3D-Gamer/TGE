import unittest
from hjson.compat import StringIO as StringIO

class TestTuples(unittest.TestCase):
    def test_tuple_array_dumps(self) -> None: ...
    def test_tuple_array_dump(self) -> None: ...

class TestNamedTuple(unittest.TestCase):
    def test_namedtuple_dump(self) -> None: ...
