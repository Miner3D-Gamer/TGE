from typing import Any

class WaveObject:
    @classmethod
    def from_wave_file(cls, filename: str) -> "WaveObject": ...
    def play(self) -> "PlayObject": ...
    @classmethod
    def play_buffer(
        cls, buffer: bytes, num_channels: int, bytes_per_sample: int, sample_rate: int
    ) -> "PlayObject": ...

class PlayObject:
    def is_playing(self) -> bool: ...
    def stop(self) -> None: ...
    @property
    def buffer(self) -> Any: ...