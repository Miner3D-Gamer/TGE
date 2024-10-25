from typing import Any

class AudioSegment:
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...

    def export(self, out_f: str, format: str = None, **kwargs: Any) -> None: ...

    @classmethod
    def from_file(cls, file: str, format: str = None) -> 'AudioSegment': ...

    def __add__(self, other: 'AudioSegment') -> 'AudioSegment': ...

    def __getitem__(self, index: int | slice) -> int | 'AudioSegment':...  # Support for both int and slice
    
    def __len__(self) -> int: ... # Length of AudioSegment

    @property
    def raw_data(self) -> bytes: ...  # Property to get raw audio data

    @property
    def frame_rate(self) -> int: ...  # Property to get the frame rate

    @property
    def channels(self) -> int: ...  # Property to get the number of channels

    @property
    def sample_width(self) -> int: ...  # Property to get the sample width