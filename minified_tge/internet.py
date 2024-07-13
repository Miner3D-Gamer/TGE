_C=False
_B=None
_A=True
from typing import List,Union,Tuple,Any,Tuple,Dict,Optional
import re,pytube
def remove_html_tags(string):return re.sub('<.*?>','',string)
def get_youtube_video_id(input_string):
	A=input_string;C='^[a-zA-Z0-9_-]{11}$';D=['(?:https?://)?(?:www\\.)?(?:youtube\\.com/watch\\?v=|youtu\\.be/|youtube\\.com/embed/|youtube\\.com/v/)([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[?&]v=([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[&?]vi?=([a-zA-Z0-9_-]{11})']
	if re.match(C,A):return A
	for E in D:
		B=re.search(E,A)
		if B:return B.group(1)
	return''
import urllib.request
def is_internet_connected(max_timeout=5,website='https://www.google.com'):
	try:urllib.request.urlopen(website,timeout=max_timeout);return _A
	except Exception as A:return _C
def download_youtube_video(url_or_id,save_path,file_name,quality,audio_type=_B):
	E=audio_type;D=file_name;A=quality;id=get_youtube_video_id(url_or_id)
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
	A=avatar_url;B={'content':message_content,'username':name,'tts':activate_voice,'allowed_mentions':{'parse':[]}if mention else{}}
	if A is not _B:B['avatar_url']=A
	C=requests.post(webhook,json=B);return C.status_code,C.content
from urllib.parse import urlparse,parse_qs
def extract_youtube_info(link):
	C='/shorts/';A=link;D=urlparse(A);B=parse_qs(D.query)
	if A.__contains__(C):A=A.replace(C,'/watch?v=')
	E=B.get('v',[_B])[0];F={A:B[0]for(A,B)in B.items()if A!='v'};return{'video_id':E,'params':F}
from.file_operations import create_missing_directory
def download_from_url_to_dir(url,dir,create):
	C='utf-8';A=requests.get(url)
	try:
		if create:
			create_missing_directory(dir)
			with open(dir+A.url.split('/')[-1],'wb',encoding=C)as B:B.write(A.content)
			return _A
		else:
			with open(dir+A.url.split('/')[-1],'wb',encoding=C)as B:B.write(A.content)
			return _A
	except:return _C