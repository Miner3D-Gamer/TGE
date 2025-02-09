#type: ignore
from urllib.parse import urlparse,parse_qs
import os,re,urllib.request
_A=False
from.file_operations import create_missing_directory
__all__=['is_url','remove_html_tags','is_internet_connected','is_url_available','get_youtube_video_id','get_all_videos_from_youtube_playlist']
def is_url(url):A=re.compile('^(?:http|https)://(?:[\\w-]+\\.)*[\\w-]+(?:\\.[a-zA-Z]{2,})(?:/?|(?:/[^\\s]+)+)?$');return bool(re.match(A,url))
def remove_html_tags(string):return re.sub('<.*?>','',string)
def get_youtube_video_id(input_string):
 A=input_string;C='^[a-zA-Z0-9_-]{11}$';D=['(?:https?://)?(?:www\\.)?(?:youtube\\.com/watch\\?v=|youtu\\.be/|youtube\\.com/embed/|youtube\\.com/v/)([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[?&]v=([a-zA-Z0-9_-]{11})','(?:https?://)?(?:www\\.)?youtube\\.com/.*[&?]vi?=([a-zA-Z0-9_-]{11})']
 if re.match(C,A):return A
 for E in D:
  B=re.search(E,A)
  if B:return B.group(1)
 return''
def is_internet_connected(max_timeout=5,website='https://www.google.com'):
 try:urllib.request.urlopen(website,timeout=max_timeout);return True
 except Exception as A:return _A
def download_list_of_youtube_videos(urls,directory,preferred_format='mp3',preferred_quality='192'):
 A=directory;B=[]
 if not os.path.exists(A):os.makedirs(A)
 import yt_dlp as C;D={'format':'bestaudio/best','postprocessors':[{'key':'FFmpegExtractAudio','preferredcodec':preferred_format,'preferredquality':preferred_quality}],'outtmpl':os.path.join(A,'%(title)s.%(ext)s')}
 with C.YoutubeDL(D)as E:
  for F in urls:
   try:E.download([F]);B.append(None)
   except Exception as G:B.append(G)
 return B
def extract_youtube_info(link):
 C='/shorts/';A=link;D=urlparse(A);B=parse_qs(D.query)
 if A.__contains__(C):A=A.replace(C,'/watch?v=')
 E=B.get('v',[None])[0];F={A:B[0]for(A,B)in B.items()if A!='v'};return{'video_id':E,'params':F}
def is_url_available(url,check_url=True):
 A=check_url
 if A:A=not is_url(url)
 if not A:return _A
 import requests as B
 try:
  C=B.get(url)
  if C.status_code==200:return True
  else:return _A
 except(B.exceptions.ConnectionError,B.exceptions.ConnectTimeout):return
def get_all_videos_from_youtube_playlist(playlist_url):
 import pytube as A
 try:B=A.Playlist(playlist_url);return[A for A in B.video_urls]
 except Exception as C:return C