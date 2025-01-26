from _typeshed import Incomplete

__all__ = ['HjsonDecodeError']

class HjsonDecodeError(ValueError):
    msg: Incomplete
    doc: Incomplete
    pos: Incomplete
    end: Incomplete
    def __init__(self, msg, doc, pos, end: Incomplete | None = None) -> None: ...
    def __reduce__(self): ...
