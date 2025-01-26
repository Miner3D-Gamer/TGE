from .compat import PY3 as PY3, binary_type as binary_type, integer_types as integer_types, string_types as string_types, u as u, unichr as unichr
import sys
import struct
from .compat import fromhex
def _floatconstants():
    _BYTES = fromhex('7FF80000000000007FF0000000000000')
    # The struct module in Python 2.4 would get frexp() out of range here
    # when an endian is specified in the format string. Fixed in Python 2.5+
    if sys.byteorder != 'big':
        _BYTES = _BYTES[:8][::-1] + _BYTES[8:][::-1]
    nan, inf = struct.unpack('dd', _BYTES)
    return nan, inf, -inf

NaN, PosInf, NegInf = _floatconstants()
from _typeshed import Incomplete

ESCAPE: Incomplete
ESCAPE_ASCII: Incomplete
HAS_UTF8: Incomplete
ESCAPE_DCT: Incomplete
COMMONRANGE: str
NEEDSESCAPE: Incomplete
NEEDSQUOTES: Incomplete
NEEDSESCAPEML: Incomplete
WHITESPACE: str
STARTSWITHNUMBER: Incomplete
STARTSWITHKEYWORD: Incomplete
NEEDSESCAPENAME: Incomplete
FLOAT_REPR = repr

def encode_basestring(s, _PY3=..., _q=...): ...
def encode_basestring_ascii(s, _PY3=...): ...

class HjsonEncoder:
    skipkeys: Incomplete
    ensure_ascii: Incomplete
    check_circular: Incomplete
    sort_keys: Incomplete
    use_decimal: Incomplete
    namedtuple_as_object: Incomplete
    tuple_as_array: Incomplete
    bigint_as_string: Incomplete
    item_sort_key: Incomplete
    for_json: Incomplete
    int_as_string_bitcount: Incomplete
    indent: Incomplete
    encoding: Incomplete
    def __init__(self, skipkeys: bool = False, ensure_ascii: bool = True, check_circular: bool = True, sort_keys: bool = False, indent: str = '  ', encoding: str = 'utf-8', default: Incomplete | None = None, use_decimal: bool = True, namedtuple_as_object: bool = True, tuple_as_array: bool = True, bigint_as_string: bool = False, item_sort_key: Incomplete | None = None, for_json: bool = False, int_as_string_bitcount: Incomplete | None = None) -> None: ...
    def default(self, o) -> None: ...
    def encode(self, o): ...
    def iterencode(self, o, _one_shot: bool = False): ...
