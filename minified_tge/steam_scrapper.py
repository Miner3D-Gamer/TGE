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
def get_game_name(session,game_id):
	'\n    Fetches the name of a game from Steam\'s website using its game ID.\n\n    This function uses the provided session to make an HTTP GET request to the Steam Community\n    page of the game with the given game ID. It then parses the HTML content of the page to\n    extract the game\'s name.\n\n    Args:\n        session (requests.Session): A requests session object for making HTTP requests.\n        game_id (int): The ID of the game on Steam.\n\n    Returns:\n        str or None: The name of the game if successfully retrieved, or None if an error occurred.\n\n    Raises:\n        None\n\n    Note:\n        The function handles potential network errors using requests.exceptions.RequestException\n        and returns None in case of any error during the request.\n\n    Example:\n        session = requests.Session()\n        game_id = 12345\n        game_name = get_game_name(session, game_id)\n        if game_name:\n            print(f"The name of the game is: {game_name}")\n        else:\n            print("Failed to retrieve the game name.")\n    ';D=f"https://steamcommunity.com/app/{game_id}/"
	try:
		A=session.get(D,timeout=20);A.raise_for_status();E=BeautifulSoup(A.content,_F);B=E.find('title')
		if B:
			C=B.get_text()
			if _G not in C:F=C.replace(' on Steam','').replace('Steam Community :: ','');return F
	except requests.exceptions.RequestException:pass
def check_game_ids_with_names(game_ids,results={}):
	"\n    Retrieves game names associated with the provided game IDs using multi-threading.\n    \n    This function takes a list of game IDs and optionally a dictionary of results. It uses multi-threading\n    to concurrently fetch the game names corresponding to the given game IDs by calling the 'get_game_name'\n    function. The fetched game names are stored in the 'results' dictionary under the corresponding game ID.\n    \n    Args:\n        game_ids (list): A list of game IDs for which to retrieve game names.\n        results (dict, optional): A dictionary to store the results. The keys are game IDs and the values\n            are dictionaries containing game information. If not provided, an empty dictionary is used.\n            \n    Returns:\n        dict: A dictionary containing the results of the operation. The keys are game IDs and the values are\n            dictionaries containing game information, including the fetched game name if available.\n    ";A=results
	with requests.Session()as E,concurrent.futures.ThreadPoolExecutor()as F:
		B={F.submit(get_game_name,E,A):A for A in game_ids}
		for C in concurrent.futures.as_completed(B):
			G=B[C]
			try:
				D=C.result()
				if D:A[G]['name']=D
			except Exception:pass
	return A
def get_valid_game_ids_with_names():"\n    Retrieves a list of valid game IDs along with their corresponding names from Steam.\n\n    This function fetches game data from Steam using the 'get_steam_games' function and then filters\n    out valid game IDs along with their names using the 'check_game_ids_with_names' function.\n\n    Returns:\n    list: A list of dictionaries, where each dictionary contains 'game_id' (unique identifier) and\n        'game_name' (name of the game) for valid games on Steam.\n    ";A,B=get_steam_games();C=check_game_ids_with_names(A,B);return C
def get_response(session,game_id):
	'\n    Retrieve the HTTP response content for a specific game on Steam Community.\n\n    This function takes a session object and a game ID as input and constructs a URL\n    to fetch information about the specified game from the Steam Community website.\n    It sends an HTTP GET request to the constructed URL and returns the content of\n    the response if the request is successful (HTTP status code 200). If there\'s any\n    error during the request, a \'None\' value is returned.\n\n    Args:\n        session (requests.Session): A requests session object to manage the HTTP connection.\n        game_id (int): The ID of the game on Steam.\n\n    Returns:\n        bytes or None: The content of the HTTP response, or \'None\' if an error occurs\n                    during the request.\n\n    Example:\n        session = requests.Session()\n        content = get_response(session, 12345)\n        if content is not None:\n            print(content.decode(\'utf-8\'))\n        else:\n            print("Failed to retrieve the game information.")\n    ';B=f"https://steamcommunity.com/app/{game_id}/"
	try:A=session.get(B,timeout=20);A.raise_for_status();return A.content
	except requests.exceptions.RequestException:return
def is_valid_game_id(session,game_id):
	'\n    Check the validity of a game ID by retrieving the response content\n    for the provided game ID using the given session object.\n\n    Parameters:\n    session (requests.Session): The session object to use for making HTTP requests.\n    game_id (str): The ID of the game to validate.\n\n    Returns:\n    bool: True if the game ID is valid and corresponds to an existing game,\n        False otherwise. A game ID is considered valid if a response is\n        obtained and the title of the page retrieved does not contain\n        the phrase "Welcome to Steam".\n    ';A=get_response(session,game_id)
	if A:
		C=BeautifulSoup(A,_F);B=C.find('title')
		if B:D=B.get_text();return _G not in D
	return _B
def check_game_ids(game_ids):
	"\n    Check the validity of a list of game IDs using multi-threading.\n    \n    This function takes a list of game IDs and utilizes a ThreadPoolExecutor to concurrently check the validity of each\n    game ID using the 'is_valid_game_id' function. The results are stored in a dictionary where keys are game IDs and\n    values indicate whether each game ID is valid or not.\n\n    Args:\n        game_ids (list): A list of game ID strings to be checked.\n\n    Returns:\n        dict: A dictionary containing game IDs as keys and their validity status (True, False, or None) as values.\n            - True: The game ID is valid.\n            - False: The game ID is invalid.\n            - None: An exception occurred while processing the game ID.\n    ";A={}
	with requests.Session()as E,concurrent.futures.ThreadPoolExecutor()as F:
		B={F.submit(is_valid_game_id,E,A):A for A in game_ids}
		for C in concurrent.futures.as_completed(B):
			D=B[C]
			try:G=C.result();A[D]=G
			except Exception:A[D]=None
	return A
def get_steam_folders():
	"\n    Retrieves a list of Steam library folders from the configuration file.\n\n    This function reads the 'libraryfolders.vdf' configuration file of the Steam client\n    located at 'C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf'. It extracts\n    the paths of additional library folders where Steam games can be stored.\n\n    Returns:\n        list: A list of paths to Steam library folders.\n            The paths use forward slashes (/) as separators.\n    ";B=[]
	try:
		with open('C:\\Program Files (x86)\\Steam\\config\\libraryfolders.vdf','r')as D:E=D.read()
	except:return B
	F=E.split(_C)
	for A in F:
		A=A.strip()
		if A.startswith('"path"'):C=A.split('"')[3];C=C.replace('\\\\','/');B.append(C)
	return B
def get_steam_accounts():
	"\n    Retrieves Steam account information from the 'loginusers.vdf' file located in the Steam configuration directory.\n\n    This function reads the 'loginusers.vdf' file, which contains information about Steam accounts that have logged into\n    the Steam client. It extracts relevant information such as account IDs, usernames, remember login status, and more.\n\n    Returns:\n    dict: A dictionary containing information about the Steam account, where the keys represent various attributes\n        such as 'id', 'AccountName', 'PersonaName', 'RememberPassword', and 'mostrecent'.\n    "
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
	'\n    Retrieves Steam game information from the localconfig.vdf file.\n\n    This function reads the Steam configuration file located at the specified path\n    and extracts relevant game information including playtime, cloud save details,\n    and last played timestamps.\n\n    Args:\n        result (dict, optional): A dictionary to store the extracted game information.\n            Defaults to an empty dictionary.\n\n    Returns:\n        tuple: A tuple containing two elements - a list of game IDs and a dictionary\n        containing extracted game information. The dictionary structure is as follows:\n        {\n            "game_id": {\n                "last_played": ["YYYY", "MM", "DD", "HH", "MM", "SS"],\n                "Playtime2wks": int,\n                "playtime": int,\n                "BadgeData": int,\n                "cloud": {\n                    "state": str,\n                    "quota_bytes": int,\n                    "quota_files": int,\n                    "used_bytes": int,\n                    "used_files": int,\n                    "lastlaunch": ["YYYY", "MM", "DD", "HH", "MM", "SS"],\n                    "lastexit": ["YYYY", "MM", "DD", "HH", "MM", "SS"]\n                }\n            },\n            ...\n        }\n    ';V='BadgeData';U='Playtime2wks';T='last_played';S='lastexit';R='lastlaunch';P='playtime';O=' ';N='%Y %m %d %H %M %S';G='cloud';A=result;W=_H
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
	"\n    Retrieve Steam friends and groups information from the localconfig.vdf file.\n\n    This function reads the localconfig.vdf file located at the specified Steam\n    configuration path to extract information about a user's Steam friends and groups.\n    It parses the file to extract friend and group data and returns two dictionaries:\n    one for the friends and another for the groups the user belongs to.\n\n    Returns:\n        tuple: A tuple containing two dictionaries.\n            - The first dictionary represents the user's Steam friends. The keys are\n            friend usernames, and the values are dictionaries containing various\n            attributes of each friend.\n            - The second dictionary contains information about the Steam groups the\n            user is a part of. The keys are group usernames, and the values are the\n            corresponding attributes of each group.\n\n        If there is any issue reading the file or parsing the data, two empty\n        dictionaries are returned.\n    ";K=_H
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
def get_steam_data():"\n    Retrieve Steam-related data for folders, accounts, games, and social connections.\n\n    This function gathers information about the user's Steam setup, including folders,\n    linked accounts, game IDs and names, as well as friends and groups in the social network.\n\n    Returns:\n        dict: A dictionary containing the following keys:\n            - 'folders' (list): A list of Steam folders on the system.\n            - 'accounts' (list): A list of linked Steam accounts.\n            - 'games' (dict): A dictionary of valid game IDs mapped to their names.\n            - 'social' (dict): A sub-dictionary containing social connections:\n                - 'friends' (list): A list of Steam friends.\n                - 'groups' (list): A list of Steam groups.\n    ";B='social';A={};A['folders']=get_steam_folders();A['accounts']=get_steam_accounts();A['games']=get_valid_game_ids_with_names();A[B]={};A[B][_I],A[B]['groups']=get_steam_friends();return A
def convert_to_datetime(timestamp):'\n    Converts a Unix timestamp to a datetime object.\n\n    This function takes a Unix timestamp as input and returns a corresponding\n    datetime object in the local time zone. The Unix timestamp represents the\n    number of seconds that have elapsed since January 1, 1970 (UTC).\n\n    Parameters:\n    timestamp (float or int): The Unix timestamp to be converted.\n\n    Returns:\n    datetime.datetime: A datetime object representing the date and time\n    corresponding to the provided Unix timestamp in the local time zone.\n    ';return datetime.datetime.fromtimestamp(timestamp)
if __name__==_E:
	print(f"Initialized in {time.time()-very_start}");start=time.time();steam_data=get_steam_data()
	for i in steam_data:print(steam_data[i])
	print(f"Finished in {time.time()-start}")