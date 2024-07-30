_A=False
import os
from.import SYSTEM_NAME
from gtts import gTTS
from pydub import AudioSegment
from simpleaudio import play_buffer
class AudioPlayer:
 def __init__(A,file_path):A.audio=AudioSegment.from_file(file_path);A.samples=A.audio.raw_data;A.sample_rate=A.audio.frame_rate;A.num_channels=A.audio.channels;A.bytes_per_sample=A.audio.sample_width;A.current_position=0;A.play_obj=None;A.is_playing=_A
 def play(A):
  if not A.is_playing:A.play_obj=play_buffer(A.audio[A.current_position:].raw_data,A.num_channels,A.bytes_per_sample,A.sample_rate);A.is_playing=True
 def pause(A):
  if A.is_playing:A.current_position+=len(A.play_obj.buffer)//(A.bytes_per_sample*A.num_channels);A.play_obj.stop();A.is_playing=_A
 def resume(A):
  if not A.is_playing:A.play()
 def stop(A):
  if A.is_playing:A.play_obj.stop();A.is_playing=_A;A.current_position=0
 def get_position(A):return A.current_position+len(A.play_obj.buffer)//(A.bytes_per_sample*A.num_channels)
 def set_position(A,position):
  B=position
  if A.is_playing:A.pause()
  if B<0 or B>len(A.audio):raise ValueError('Position out of range')
  A.current_position=B;A.play()
def save_text_to_speech(text,name,dir,language='en'):
 if not os.path.exists(dir):raise FileNotFoundError('Directory %s was not found'%dir)
 A=gTTS(text=text,lang=language);A.save(f"{dir}/{name}")