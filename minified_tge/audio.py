_D='Directory cannot be empty'
_C='Name cannot be empty'
_B=True
_A=False
from pathlib import Path as pathlib_path
from typing import List,Union,Tuple,Any
from gtts import gTTS
from pygame import mixer as playsound
from.file_operations import get_file_extension,create_missing_directory,doesFileExist
def load_sound(name,dir):
	A=name
	if not not dir:
		if not not A:
			dir=dir.replace(f"{pathlib_path(__file__).resolve().parent}/",'');dir=dir.replace(f"{pathlib_path(__file__).resolve().parent}",'')
			if doesFileExist(f"{pathlib_path(__file__).resolve().parent}/{dir}/{A}"):B=playsound.Sound(f"{pathlib_path(__file__).resolve().parent}/{dir}/{A}");return B,_B
			else:return'File in Directory can not be found',_A
		else:return _C,_A
	else:return _D,_A
def play_sound(audio,volume,fadeout):
	C=fadeout;B=volume;A=audio
	if A!='':
		if B>=0:
			try:
				A.set_volume(B);A.play()
				if C>0:A.fadeout(C)
				return _B,'Playing sound'
			except:return _A,'Error loading sound, are you sure this is a sound file?'
		else:return _A,'Volume cannot be negative'
	else:return _A,_C
def stop_sound(audio):
	A=audio
	if A!='':A.stop();return _B
	else:playsound.stop();return _A
def pause_sound(audio):
	A=audio
	if A!='':A.pause();return _B
	else:playsound.pause();return _A
def unpause_sound(audio):
	A=audio
	if A!='':A.unpause();return _B
	else:playsound.unpause();return _A
def get_sound_status(audio,raw):
	A=audio
	try:
		if A!='':
			if not raw:return(A.get_volume(),A.get_length()),_B
			else:return A.get_raw(),_B
		else:return'No sound loaded',_A
	except:return'Error loading audio, are you sure this is an audio file?',_A
def sound_stats(name,dic):
	if name!='':
		if dic!='':A=playsound.Sound(f"{pathlib_path(__file__).resolve().parent}/{dic}/{name}");return(A.get_volume(),A.get_length()),_B
		else:return _D,_A
	else:return _C,_A
def save_text_to_speech(text,name,dir):
	A=name
	if dir=='':dir='.'
	B=gTTS(text=text,lang='en')
	if get_file_extension(A)=='':A=A.split('.')[0];A+='.mp3'
	create_missing_directory(dir)
	try:B.save(f"{dir}/{A}")
	except:pass