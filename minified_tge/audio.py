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
	'\n    Loads a sound from a directory\n\n    Args:\n    - name (str): name of the sound file\n    - dir (str): directory containing the sound file\n\n    Returns:\n    - audio (playsound.Sound): sound\n    o\n    - error (str): error message\n    ';A=name
	if not not dir:
		if not not A:
			dir=dir.replace(f"{pathlib_path(__file__).resolve().parent}/",'');dir=dir.replace(f"{pathlib_path(__file__).resolve().parent}",'')
			if doesFileExist(f"{pathlib_path(__file__).resolve().parent}/{dir}/{A}"):B=playsound.Sound(f"{pathlib_path(__file__).resolve().parent}/{dir}/{A}");return B,_B
			else:return'File in Directory can not be found',_A
		else:return _C,_A
	else:return _D,_A
def play_sound(audio,volume,fadeout):
	'\n    Plays a sound file with the given attributes.\n\n    Args:\n        audio (str): The name of the audio file to be played.\n        volume (int): The volume at which to play the audio file (0-100).\n        fadeout (int): The time (in milliseconds) it takes for the audio to fade out.\n\n    Returns:\n        Tuple[bool, str]: A tuple containing a boolean indicating whether or not the \n        audio played successfully, and a string message explaining the result. \n        If the audio played successfully, the boolean will be True and the message will \n        be "Playing sound". If the audio failed to play for any reason, the boolean will \n        be False and the message will provide an explanation for the failure.\n\n    Raises:\n        None.\n\n    ';C=fadeout;B=volume;A=audio
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
	'\n    Stop the audio playback.\n\n    Args:\n    audio (str or object): The audio to stop playback for. Can be a string representing a file path\n    or an object representing an ongoing audio playback.\n\n    Returns:\n    bool: True if the audio playback was stopped successfully, False if not.\n\n    Note:\n    - If audio is a string representing a file path, the function stops playback of the audio file\n    associated with that path.\n    - If audio is an object representing an ongoing audio playback, the function stops that playback.\n    - If audio is an empty string, the function attempts to stop playback of the most recently played audio.\n    ';A=audio
	if A!='':A.stop();return _B
	else:playsound.stop();return _A
def pause_sound(audio):
	'\n    Pause the audio playback.\n\n    Args:\n        audio (Audio): The audio object to pause.\n\n    Returns:\n        bool: True if the audio was paused, False if there was no audio to pause.\n    ';A=audio
	if A!='':A.pause();return _B
	else:playsound.pause();return _A
def unpause_sound(audio):
	'\n    Unpauses the given audio object or the default sound if audio is not provided.\n\n    Args:\n        audio: an instance of a sound object to unpause\n\n    Returns:\n        True if the sound was successfully unpaused, False otherwise.\n    ';A=audio
	if A!='':A.unpause();return _B
	else:playsound.unpause();return _A
def get_sound_status(audio,raw):
	'\n    Returns the status of the sound.\n\n    Parameters:\n    audio : The sound object to get the status of.\n    raw (bool): Whether to return the raw audio data or not.\n\n    Returns:\n    tuple: A tuple containing a boolean indicating whether the audio is loaded or not,\n        and either the volume and length of the audio (if `raw` is False), or the\n        raw audio data (if `raw` is True).\n\n    Raises:\n    Exception: If there was an error loading the audio file.\n    ';A=audio
	try:
		if A!='':
			if not raw:return(A.get_volume(),A.get_length()),_B
			else:return A.get_raw(),_B
		else:return'No sound loaded',_A
	except:return'Error loading audio, are you sure this is an audio file?',_A
def sound_stats(name,dic):
	'\n    Returns a tuple containing the volume and length of a sound file.\n\n    Args:\n    - name (str): the name of the sound file.\n    - dic (str): the directory where the sound file is located.\n\n    Returns:\n    - A tuple containing:\n        - True if the sound file was successfully loaded, False otherwise.\n        - A tuple containing the volume (in dB) and length (in seconds) of the sound file.\n\n    If either \'name\' or \'dic\' are empty strings, the function returns (False, "Name cannot be empty")\n    or (False, "Directory cannot be empty"), respectively.\n    '
	if name!='':
		if dic!='':A=playsound.Sound(f"{pathlib_path(__file__).resolve().parent}/{dic}/{name}");return(A.get_volume(),A.get_length()),_B
		else:return _D,_A
	else:return _C,_A
def save_text_to_speech(text,name,dir):
	'\n    Convert the provided text into speech using the Google Text-to-Speech (gTTS) API\n    and save it as an audio file.\n\n    Args:\n        text (str): The text to be converted to speech.\n        name (str): The desired name of the output audio file.\n        dir (str): The directory path where the audio file should be saved.\n                If dir is an empty string, the current directory will be used.\n\n    Returns:\n        None\n\n    Note:\n        If the provided \'name\' does not have a valid file extension, \'.mp3\' will be appended.\n        The function attempts to create any missing directories in the specified \'dir\' path.\n        If successful, the generated audio file is saved in the format \'dir/name\'.\n        If an exception occurs during the saving process, the function returns None.\n\n    Example:\n        save_text_to_speech("Hello, how are you?", "greeting", "output_audio")\n        # Converts the text to speech and saves it as \'output_audio/greeting.mp3\'\n\n    ';A=name
	if dir=='':dir='.'
	B=gTTS(text=text,lang='en')
	if get_file_extension(A)=='':A=A.split('.')[0];A+='.mp3'
	create_missing_directory(dir)
	try:B.save(f"{dir}/{A}")
	except:pass