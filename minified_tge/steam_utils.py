_I='friends'
_H='C:\\Program Files (x86)\\Steam\\userdata\\1093663613\\config\\localconfig.vdf'
_G='Welcome to Steam'
_F='html.parser'
_E='__main__'
_D=True
_C='\n'
_B=False
_A='\t'
if __name__==_E:import time;very_start=time.time()
import requests
from bs4 import BeautifulSoup
import concurrent.futures,datetime
from collections.abc import Iterable
def get_game_name(session,game_id):
	D=f"https://steamcommunity.com/app/{game_id}/"
	try:
		A=session.get(D,timeout=20);A.raise_for_status();E=BeautifulSoup(A.content,_F);B=E.find('title')
		if B:
			C=B.get_text()
			if _G not in C:F=C.replace(' on Steam','').replace('Steam Community :: ','');return F
	except requests.exceptions.RequestException:pass
def check_game_ids_with_names(game_ids,results={}):
	A=results
	with requests.Session()as E,concurrent.futures.ThreadPoolExecutor()as F:
		B={F.submit(get_game_name,E,A):A for A in game_ids}
		for C in concurrent.futures.as_completed(B):
			G=B[C]
			try:
				D=C.result()
				if D:A[G]['name']=D
			except Exception:pass
	return A
def get_valid_game_ids_with_names():A,B=get_steam_games();C=check_game_ids_with_names(A,B);return C
def get_response(session,game_id):
	B=f"https://steamcommunity.com/app/{game_id}/"
	try:A=session.get(B,timeout=20);A.raise_for_status();return A.content
	except requests.exceptions.RequestException:return
def is_valid_game_id(session,game_id):
	A=get_response(session,game_id)
	if A:
		C=BeautifulSoup(A,_F);B=C.find('title')
		if B:D=B.get_text();return _G not in D
	return _B
def check_game_ids(game_ids):
	A={}
	with requests.Session()as E,concurrent.futures.ThreadPoolExecutor()as F:
		B={F.submit(is_valid_game_id,E,A):A for A in game_ids}
		for C in concurrent.futures.as_completed(B):
			D=B[C]
			try:G=C.result();A[D]=G
			except Exception:A[D]=None
	return A
def get_steam_folders():
	B=[]
	try:
		with open('C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf','r')as D:E=D.read()
	except:return B
	F=E.split(_C)
	for A in F:
		A=A.strip()
		if A.startswith('"path"'):C=A.split('"')[3];C=C.replace('\\\\','/');B.append(C)
	return B
def get_steam_accounts():
	try:
		with open('C:/Program Files (x86)/Steam/config/loginusers.vdf')as G:H=G.read()
	except:return{}
	D=H[8:-1];D=D.split(_C);B=0;E={}
	for A in D:
		A=A.lstrip(_A)
		if A=='{':B+=1
		elif A=='}':B-=1
		elif B==0:break
		elif B==1:E['id']=A.strip('"')
		elif B==2:
			C=A.split('"')
			if C[3]=='1':F=_D
			elif C[3]=='0':F=_B
			else:F=C[3]
			E[C[1]]=F
	return E
def get_steam_games(result={}):
	V='BadgeData';U='Playtime2wks';T='last_played';S='lastexit';R='lastlaunch';P='playtime';O=' ';N='%Y %m %d %H %M %S';G='cloud';A=result;W=_H
	try:
		with open(W,'r',encoding='utf-8')as X:Y=X.read()
	except:return A
	Z=Y.split(_C);H=0;a=0;L=_B;Q=_B;M=_B;K=[]
	for F in Z:
		F=F.lstrip(_A)
		if F=='{':H+=1
		elif F=='}':H-=1
		else:
			if H==7:
				if L:
					I=F.split(_A);C,E=I[0][1:-1],I[-1][1:-1]
					if B not in A:A[B]={}
					if G not in A[B]:A[B][G]={}
					if C=='last_sync_state':A[B][G]['state']=E;L=_B
					else:
						b=['quota_bytes','quota_files','used_bytes','used_files']
						if C in b:A[B][G][C]=E
						else:print(C,'Cloud');quit()
				elif Q:
					if G not in A[B]:A[B][G]={}
					I=F.split(_A);C,E=I[0][1:-1],I[-1][1:-1]
					if C==R:D=datetime.datetime.fromtimestamp(E);D=D.strftime(N);D=D.split(O);A[B][G][R]=D
					elif C==S:D=datetime.datetime.fromtimestamp(E);D=D.strftime(N);D=D.split(O);A[B][G][S]=D;Q=_B
					else:print(C,'AutoCloud');quit()
			if not _A in F:
				if H==4:
					J=F[1:-1]
					if not M:
						if J=='apps':M=_D
					else:break
				elif M:
					if H==5:
						J=F[1:-1]
						if len(J)>0:K.append(J);B=J
					elif H==6:
						J=F[1:-1]
						if J==G:L=_D
			elif H==6:
				I=F.split(_A);C,E=I[0][1:-1],int(I[-1][1:-1]);A[B]={};A[B][T]=[];A[B][U]=0;A[B][P]=0;A[B][V]=0;c=[P,U,V]
				if C=='LastPlayed':E=datetime.datetime.fromtimestamp(E);E=E.strftime(N);D=E.split(O);A[B][T]=D
				elif C in c:A[B][P]=E
				elif'_eula_'in C:0
				else:print(C,'Nope');quit()
			a=H
	d=check_game_ids(K);K=[A for A in K if d[A]]
	try:K.remove('0')
	except:pass
	return K,A
def get_steam_friends():
	K=_H
	try:
		with open(K,'r',encoding='utf-8')as L:M=L.read()
	except:return{},{}
	N=M.split(_C);C=0;J=_B;B={}
	for A in N:
		A=A.lstrip(_A)
		if A=='{':C+=1
		elif A=='}':C-=1
		elif not J:
			if C==1:
				if not A.__contains__(_A):
					E=A[1:-1]
					if E==_I:J=_D
		else:
			if C==1:break
			if C==2:
				if not A.__contains__(_A):F=A[1:-1];B[F]={}
			elif C==3:
				if A.__contains__(_A):A=A.split(_A);G,H=A[0][1:-1],A[-1][1:-1];B[F][G]=H
				else:E=A[1:-1];B[F][E]={}
			elif C==4:A=A.split(_A);G,H=A[0][1:-1],A[-1][1:-1];B[F][E][G]=H
	I={}
	for D in B:
		try:B[D]['tag'];I[D]=B[D]
		except:pass
	for D in I:del B[D]
	return B,I
def get_steam_data():B='social';A={};A['folders']=get_steam_folders();A['accounts']=get_steam_accounts();A['games']=get_valid_game_ids_with_names();A[B]={};A[B][_I],A[B]['groups']=get_steam_friends();return A
def convert_to_datetime(timestamp):return datetime.datetime.fromtimestamp(timestamp)
if __name__==_E:
	print(f"Initialized in {time.time()-very_start}");start=time.time();steam_data=get_steam_data()
	for i in steam_data:print(steam_data[i])
	print(f"Finished in {time.time()-start}")