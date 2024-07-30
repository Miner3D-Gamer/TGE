from typing import List, Union, Tuple, Any
import os
from . import SYSTEM_NAME
from gtts import gTTS
from pydub import AudioSegment
from simpleaudio import play_buffer
import subprocess
import urllib.request
import sys

class AudioPlayer:
    def __init__(self, file_path: str) -> None:
        self.audio: AudioSegment = AudioSegment.from_file(file_path)
        self.samples = self.audio.raw_data
        self.sample_rate = self.audio.frame_rate
        self.num_channels = self.audio.channels
        self.bytes_per_sample = self.audio.sample_width
        self.current_position = 0
        self.play_obj = None
        self.is_playing = False

    def play(self) -> None:
        if not self.is_playing:
            self.play_obj = play_buffer(
                self.audio[self.current_position :].raw_data,
                self.num_channels,
                self.bytes_per_sample,
                self.sample_rate,
            )
            self.is_playing = True

    def pause(self) -> None:
        if self.is_playing:
            self.current_position += len(self.play_obj.buffer) // (
                self.bytes_per_sample * self.num_channels
            )
            self.play_obj.stop()
            self.is_playing = False

    def resume(self) -> None:
        if not self.is_playing:
            self.play()

    def stop(self) -> None:
        if self.is_playing:
            self.play_obj.stop()
            self.is_playing = False
            self.current_position = 0

    def get_position(self) -> int:
        "Returns the position in milliseconds"
        return self.current_position + len(self.play_obj.buffer) // (
            self.bytes_per_sample * self.num_channels
        )

    def set_position(self, position: int) -> None:
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





def install_ffmpeg():
    if SYSTEM_NAME == "Windows":
        # Define URLs and paths for Windows
        ffmpeg_url = "https://ffmpeg.org/releases/ffmpeg-release-full.7z"
        download_path = "ffmpeg.7z"
        extract_path = "ffmpeg"

        # Download FFmpeg
        urllib.request.urlretrieve(ffmpeg_url, download_path)

        # Extract the downloaded file
        import py7zr

        with py7zr.SevenZipFile(download_path, mode="r") as archive:
            archive.extractall(path=extract_path)

        # Add FFmpeg to PATH
        ffmpeg_bin = os.path.join(extract_path, "ffmpeg-*/bin")
        os.environ["PATH"] += os.pathsep + ffmpeg_bin

    elif SYSTEM_NAME == "Darwin":
        # Install FFmpeg using Homebrew on macOS
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "brew"])
            subprocess.check_call(["brew", "install", "ffmpeg"])
        except subprocess.CalledProcessError as e:
            raise BaseException(f"Error installing FFmpeg: {e}")

    elif SYSTEM_NAME == "Linux":
        # Install FFmpeg using apt-get on Ubuntu/Debian
        try:
            subprocess.check_call(["sudo", "apt-get", "update"])
            subprocess.check_call(["sudo", "apt-get", "install", "-y", "ffmpeg"])
        except subprocess.CalledProcessError as e:
            raise BaseException(f"Error installing FFmpeg: {e}")
    else:
        raise BaseException(f"Unsupported operating system: {SYSTEM_NAME}")

    print("FFmpeg installation complete.")
