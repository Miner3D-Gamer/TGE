_C=False
_B=None
_A=True
from typing import List,Union,Tuple,Any,Tuple,Dict,Optional
import re,pytube
def remove_html_tags(string):"\n        Removes HTML tags from the given string.\n\n        Args:\n            string (str): The input string containing HTML tags.\n\n        Returns:\n            str: The modified string with HTML tags removed.\n\n        Examples:\n            >>> remove_html_tags('<p>Hello, <b>world!</b></p>')\n            'Hello, world!'\n            >>> remove_html_tags('<h1>Title</h1>')\n            'Title'\n        ";return re.sub('<.*?>','',string)
def get_youtube_video_id(input_string):
	A=input_string;C='^[a-zA-Z0-9_-]{11}$';D=['(?:https?://)?(?:www\\.)?(?:youtube\\.com/watch\\?v=|youtu\\.be/|youtube\\.com/embed/|youtube\\.com/v/)([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[?&]v=([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[&?]vi?=([a-zA-Z0-9_-]{11})']
	if re.match(C,A):return A
	for E in D:
		B=re.search(E,A)
		if B:return B.group(1)
	return''
import urllib.request
def is_internet_connected(max_timeout=5,website='https://www.google.com'):
	'\n    The internet connectivity tester.\n    \n    Input:\n        >>> max_timeout = int(seconds)\n        >>> website = str("Website to test for")\n    '
	try:urllib.request.urlopen(website,timeout=max_timeout);return _A
	except Exception as A:return _C
def download_youtube_video(url_or_id,save_path,file_name,quality,audio_type=_B):
	'\n        Download a YouTube video as audio from the given URL and save it to the specified location.\n\n        Args:\n            url_or_id (str): The YouTube video URL or video ID. If a video ID is provided, it should be exactly 11 characters long.\n                    If a URL is provided, the function handles short URLs and non-standard formats.\n            save_path (str): The directory path where the downloaded video will be saved.\n            file_name (str): The desired name for the downloaded video file. If no file extension is provided, \'.mp4\' will be added.\n\n        Returns:\n            Tuple[bool, str]: A tuple containing a boolean indicating the success of the download (True for success, False for failure)\n                            and a string describing the outcome.\n\n        Note:\n            The function uses the \'pytube\' library to download YouTube videos. It attempts to download the audio-only stream,\n            but you can modify the stream selection based on your preferences.\n\n        Example:\n            success, message = download_youtube_video("https://www.youtube.com/watch?v=VIDEO_ID", "/path/to/save", "my_audio")\n            if success:\n                print("Download successful")\n            else:\n                print("Download failed:", message)\n        ';E=audio_type;D=file_name;A=quality;id=get_youtube_video_id(url_or_id)
	if not re.search('.\\..',D):D+='.mp4'
	try:
		B=pytube.YouTube(id)
		if A[-1]=='p':C=B.streams.get_by_resolution(A)
		elif A=='audio':
			if E==_B:E='mp4'
			C=B.streams.get_audio_only(E)
		elif A=='highest':C=B.streams.get_highest_resolution()
		elif A=='lowest':C=B.streams.get_lowest_resolution()
		C.download(output_path=save_path,filename=D);return _A,'True'
	except Exception as F:return _C,str(F)
import requests
def post_to_discord_webhook(message_content,webhook,name,avatar_url=_B,mention=_A,activate_voice=_C):
	'\n        Posts a message to a Discord webhook. Returns the response code and the content of the message.\n        ';A=avatar_url;B={'content':message_content,'username':name,'tts':activate_voice,'allowed_mentions':{'parse':[]}if mention else{}}
	if A is not _B:B['avatar_url']=A
	C=requests.post(webhook,json=B);return C.status_code,C.content
from urllib.parse import urlparse,parse_qs
def extract_youtube_info(link):
	'\n    Extracts information from a YouTube video link.\n\n    This function takes a YouTube video link as input and parses it to extract relevant information,\n    including the video ID and other query parameters. The parsed information is returned as a dictionary.\n\n    Args:\n        link (str): The YouTube video link to be parsed.\n\n    Returns:\n        Dict[str, Optional[str]]: A dictionary containing extracted information.\n            - \'video_id\' (str): The unique ID of the YouTube video.\n            - \'params\' (dict): Other query parameters present in the URL, excluding the video ID.\n                            The keys are parameter names, and the values are parameter values.\n\n    Example:\n        link = "https://www.youtube.com/watch?v=s7LS5lh0dLQ&feature=share"\n        result = extract_youtube_info(link)\n        # Result:\n        # {\n        #     \'video_id\': \'s7LS5lh0dLQ\',\n        #     \'params\': {\'feature\': \'share\'}\n        # }\n    ';C='/shorts/';A=link;D=urlparse(A);B=parse_qs(D.query)
	if A.__contains__(C):A=A.replace(C,'/watch?v=')
	E=B.get('v',[_B])[0];F={A:B[0]for(A,B)in B.items()if A!='v'};return{'video_id':E,'params':F}
from.file_operations import create_missing_directory
def download_from_url_to_dir(url,dir,create):
	"\n    Downloads a file from the given URL and saves it to the specified directory.\n\n    Args:\n        url (str): The URL of the file to be downloaded.\n        dir (str): The directory where the downloaded file will be saved.\n        create (bool): If True, creates the directory if it doesn't exist.\n\n    Returns:\n        None\n\n    Raises:\n        Any exceptions raised during the download and file write process are caught,\n        and the function returns False if an exception occurs.\n\n    Note:\n        This function uses the 'requests' library to download the file. If 'create' is\n        set to True, it creates the missing directory structure before saving the file.\n        The file is saved with the same name as the last part of the URL.\n\n    Example:\n        download_from_url_to_dir(\n            'https://example.com/file.txt', '/path/to/directory/', create=True\n        )\n    ";C='utf-8';A=requests.get(url)
	try:
		if create:
			create_missing_directory(dir)
			with open(dir+A.url.split('/')[-1],'wb',encoding=C)as B:B.write(A.content)
			return _A
		else:
			with open(dir+A.url.split('/')[-1],'wb',encoding=C)as B:B.write(A.content)
			return _A
	except:return _C