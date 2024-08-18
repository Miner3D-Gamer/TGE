import os
from . import SYSTEM_NAME
from gtts import gTTS
from pydub import AudioSegment
from simpleaudio import play_buffer

class AudioPlayer:
    def __init__(self, file_path: str) -> None:
        """
        Initializes the AudioPlayer with an audio file.

        Args:
            file_path (str): Path to the audio file.
        """
        self.audio: AudioSegment = AudioSegment.from_file(file_path)
        self.samples = self.audio.raw_data
        self.sample_rate = self.audio.frame_rate
        self.num_channels = self.audio.channels
        self.bytes_per_sample = self.audio.sample_width
        self.current_position = 0
        self.play_obj = None
        self.is_playing = False

    def play(self) -> None:
        """
        Starts or resumes playback from the current position.
        """
        if not self.is_playing:
            self.play_obj = play_buffer(
                self.audio[self.current_position :].raw_data,
                self.num_channels,
                self.bytes_per_sample,
                self.sample_rate,
            )
            self.is_playing = True

    def pause(self) -> None:
        """
        Pauses the playback and updates the current position.
        """
        if self.is_playing:
            self.current_position += len(self.play_obj.buffer) // (
                self.bytes_per_sample * self.num_channels
            )
            self.play_obj.stop()
            self.is_playing = False

    def resume(self) -> None:
        """
        Resumes playback from the current position if paused.
        """
        if not self.is_playing:
            self.play()

    def stop(self) -> None:
        """
        Stops playback, resets the current position to the start, and sets playback state to stopped.
        """
        if self.is_playing:
            self.play_obj.stop()
            self.is_playing = False
            self.current_position = 0

    def get_position(self) -> int:
        """
        Returns the current playback position in milliseconds.

        Returns:
            int: The current position in milliseconds.
        """
        return self.current_position + len(self.play_obj.buffer) // (
            self.bytes_per_sample * self.num_channels
        )

    def set_position(self, position: int) -> None:
        """
        Sets the playback position to a specified value.

        Args:
            position (int): The position to set in milliseconds.

        Raises:
            ValueError: If the position is out of the valid range.
        """
        if self.is_playing:
            self.pause()

        if position < 0 or position > len(self.audio):
            raise ValueError("Position out of range")

        self.current_position = position

        self.play()


def save_text_to_speech(text: str, name: str, dir: str, language="en") -> None:
    """
    Convert the provided text into speech using the Google Text-to-Speech (gTTS) API
    and save it as an audio file.

    Args:
        text (str): The text to be converted to speech.
        name (str): The desired name of the output audio file.
        dir (str): The directory path where the audio file should be saved.
                If dir is an empty string, the current directory will be used.

    Returns:
        None
    """
    if not os.path.exists(dir):
        raise FileNotFoundError("Directory %s was not found" % dir)
    tts = gTTS(text=text, lang=language)
    
    tts.save(f"{dir}/{name}")




