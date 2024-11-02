from typing import Any, Callable, Optional, Tuple, Union, Mapping, Iterable

def dumps(
    obj: Any,
    *,
    skipkeys: bool = False,
    ensure_ascii: bool = True,
    check_circular: bool = True,
    allow_nan: bool = True,
    cls: None = None,
    indent: Optional[Union[int, str]] = None,
    separators: Optional[Tuple[str, str]] = None,
    default: Optional[Callable[[Any], Any]] = None,
    sort_keys: bool = False,
    quote_keys: bool = False,
    trailing_commas: bool = True,
    allow_duplicate_keys: bool = True,
    **kwargs: Any,
) -> str: ...
def loads(
    s: str,
    *,
    encoding: Optional[str] = None,
    cls: None = None,
    object_hook: Optional[Callable[[Mapping[str, Any]], Any]] = None,
    parse_float: Optional[Callable[[str], Any]] = None,
    parse_int: Optional[Callable[[str], Any]] = None,
    parse_constant: Optional[Callable[[str], Any]] = None,
    object_pairs_hook: Optional[Callable[[Iterable[Tuple[str, Any]]], Any]] = None,
    allow_duplicate_keys: bool = True,
) -> Any: ...