from _typeshed import Incomplete

__all__ = ['HjsonDecoder']

class HjsonDecoder:
    encoding: Incomplete
    object_hook: Incomplete
    object_pairs_hook: Incomplete
    parse_float: Incomplete
    parse_int: Incomplete
    strict: Incomplete
    parse_object: Incomplete
    parse_array: Incomplete
    parse_string: Incomplete
    parse_mlstring: Incomplete
    parse_tfnns: Incomplete
    memo: Incomplete
    def __init__(self, encoding: Incomplete | None = None, object_hook: Incomplete | None = None, parse_float: Incomplete | None = None, parse_int: Incomplete | None = None, strict: bool = True, object_pairs_hook: Incomplete | None = None) -> None: ...
    def decode(self, s, _PY3=...): ...
    def raw_decode(self, s, idx: int = 0, _PY3=...): ...
