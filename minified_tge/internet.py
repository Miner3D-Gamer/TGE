_C=False
_B=None
_A=True
import re,pytube,os,re,pytube,ffmpeg,requests,urllib.request
from.file_operations import make_legal_filename
def download_youtube_playlist(url,dir,quality,audio_type=_B):
 B=pytube.Playlist(url)
 for A in B.videos:download_youtube_video(A.watch_url,dir,make_legal_filename(A.title),quality,audio_type)
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
 try:urllib.request.urlopen(website,timeout=max_timeout);return _A
 except Exception as A:return _C
def download_youtube_video(url_or_id,save_path,file_name,quality,audio_type=_B):
 J='.mp3';H='audio';E=save_path;C=audio_type;B=quality;A=file_name;id=get_youtube_video_id(url_or_id)
 if not re.search('\\..+',A):K=J if B==H else'.mp4';A+=K
 try:
  D=pytube.YouTube(id)
  if B==H:
   if C is _B:C='mp4'
   L=D.streams.filter(only_audio=_A,file_extension=C).first();F=os.path.join(E,A);L.download(output_path=E,filename=A)
   if C!='mp3':I=os.path.splitext(F)[0]+J;ffmpeg.input(F).output(I).run();os.remove(F);A=os.path.basename(I)
  elif B=='highest':G=D.streams.get_highest_resolution()
  elif B=='lowest':G=D.streams.get_lowest_resolution()
  else:G=D.streams.get_by_resolution(B)
  if B!=H:G.download(output_path=E,filename=A)
  return _A,'Download successful'
 except Exception as M:return _C,str(M)
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
def is_url_available(url,check_url=_A):
 A=check_url
 if A:A=not is_url(url)
 if not A:return _C
 try:
  B=requests.get(url)
  if B.status_code==200:return _A
  else:return _C
 except requests.exceptions.ConnectionError or requests.exceptions.ConnectTimeout:return
def get_youtube_playlist_links(playlist_url):
 try:A=pytube.Playlist(playlist_url);B=A.video_urls;return B
 except Exception as C:print(f"An error occurred: {C}");return[]