from hjson.compat import BytesIO as BytesIO, b as b, text_type as text_type, u as u, unichr as unichr
from unittest import TestCase

class TestUnicode(TestCase):
    def test_encoding1(self) -> None: ...
    def test_encoding2(self) -> None: ...
    def test_encoding3(self) -> None: ...
    def test_encoding4(self) -> None: ...
    def test_encoding5(self) -> None: ...
    def test_encoding6(self) -> None: ...
    def test_big_unicode_encode(self) -> None: ...
    def test_big_unicode_decode(self) -> None: ...
    def test_unicode_decode(self) -> None: ...
    def test_object_pairs_hook_with_unicode(self): ...
    def test_default_encoding(self) -> None: ...
    def test_unicode_preservation(self) -> None: ...
    def test_ensure_ascii_false_returns_unicode(self) -> None: ...
    def test_ensure_ascii_false_bytestring_encoding(self) -> None: ...
    def test_ensure_ascii_linebreak_encoding(self) -> None: ...
    def test_invalid_escape_sequences(self) -> None: ...
    def test_ensure_ascii_still_works(self) -> None: ...
    def test_strip_bom(self) -> None: ...
