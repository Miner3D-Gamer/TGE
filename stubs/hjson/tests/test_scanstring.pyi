from hjson.compat import PY3 as PY3, b as b
from unittest import TestCase

class TestScanString(TestCase):
    def test_py_scanstring(self) -> None: ...
    def test_issue3623(self) -> None: ...
    def test_surrogates(self) -> None: ...
