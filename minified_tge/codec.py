_z='&#140;'
_y='&oslash;'
_x='&Oslash;'
_w='&ouml;'
_v='&otilde;'
_u='&ocirc;'
_t='&oacute;'
_s='&ograve;'
_r='&Ouml;'
_q='&Otilde;'
_p='&Ocirc;'
_o='&Oacute;'
_n='&Ograve;'
_m='&ntilde;'
_l='&Ntilde;'
_k='&iuml;'
_j='&icirc;'
_i='&iacute;'
_h='&igrave;'
_g='&Iuml;'
_f='&Icirc;'
_e='&Iacute;'
_d='&Igrave;'
_c='&#131;'
_b='&euml;'
_a='&ecirc;'
_Z='&eacute;'
_Y='&egrave;'
_X='&Euml;'
_W='&Ecirc;'
_V='&Eacute;'
_U='&Egrave;'
_T='&ccedil;'
_S='&Ccedil;'
_R='&szlig;'
_Q='&aelig;'
_P='&AElig;'
_O=' &aring;'
_N='&auml;'
_M='&atilde;'
_L='&acirc;'
_K='&aacute;'
_J='&agrave;'
_I='&Aring;'
_H='&Auml;'
_G='&Atilde;'
_F='&Acirc;'
_E='&Aacute;'
_D='&Agrave;'
_C='latin-1'
_B='.-..-.'
_A='.-.-.'
from base64 import b64encode,b64decode
from binascii import hexlify,unhexlify,Error as BinasciiError
from typing import List,Union,Tuple,Any
import re
class msy:
	def _parse_msy(D):
		C={};B=None;E=D.split('\n')
		for A in E:
			A=A.strip()
			if A.startswith('#'):B=A[1:].strip();C[B]=[]
			elif A:
				if B is not None:C[B].append(A)
				else:raise ValueError('Data format error: Item found before list name.')
		return C
	def _format_msy(B):
		A=''
		for(C,D)in B.items():
			A+=f"#{C}\n"
			for E in D:A+=f"{E}\n"
			A+='\n'
		return A
	def load(A):return msy._parse_msy(data=A)
	def format(dict):return msy._parse_msy(data=dict)
def encode(x):
	try:x=b64encode(bytes(x,_C));x=hexlify(x).decode(_C);return x
	except:return''
def decode(data):
	C=False;B=data
	try:B=unhexlify(B);D=b64decode(B);return D.decode(_C),True
	except BinasciiError as A:return f"Error decoding string (BinasciiError): {A}",C
	except UnicodeError as A:return f"Error decoding string (UnicodeError): {A}",C
	except Exception as A:return f"Unknown error decoding string (UnknownError): {A}",C
def encode_base64(string):return b64encode(string.encode()).decode()
def decode_base64(string):return b64decode(string.encode()).decode()
def decode_html_character(text):
	A=text;C=[_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N,_O,_P,_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b,_c,_d,_e,_f,_g,_h,_i,_j,_k,_l,_m,_n,_o,_p,_q,_r,_s,_t,_u,_v,_w,_x,_y,_z,'&#156;','&#138;','&#154;','&Ugrave;','&Uacute;','&Ucirc;','&Uuml;','&ugrave;','&uacute;','&ucirc;','&uuml;','&#181;','&#215;','&Yacute;','&#159;','&yacute;','&yuml;','&#176;','&#134;','&#135;','&lt;','&gt;','&#177;','&#171;','&#187;','&#191;','&#161;','&#183;','&#149;','&#153;','&copy;','&reg;','&#167;','&#182;'];D=['À','Á','Â','Ã','Ä','Å','à','á','â','ã','ä','å','Æ','æ','ß','Ç','ç','È','É','Ê','Ë','è','é','ê','ë','ƒ','Ì','Í','Î','Ï','ì','í','î','ï','Ñ','ñ','Ò','Ó','Ô','Õ','Ö','ò','ó','ô','õ','ö','Ø','ø','Œ','œ','Š','š','Ù','Ú','Û','Ü','ù','ú','û','ü','µ','×','Ý','Ÿ','ý','ÿ','°','†','‡','<','>','±','«','»','¿','¡','·','•','™','©','®','§','¶'];E=re.findall('&\\w+;',A)
	for B in E:
		if B in C:F=C.index(B);G=D[F];A=A.replace(B,G)
	return A
def encode_html_character(text):
	A=text;B=[_D,_E,_F,_G,_H,_I,_J,_K,_L,_M,_N,_O,_P,_Q,_R,_S,_T,_U,_V,_W,_X,_Y,_Z,_a,_b,_c,_d,_e,_f,_g,_h,_i,_j,_k,_l,_m,_n,_o,_p,_q,_r,_s,_t,_u,_v,_w,_x,_y,_z,'&#156;','&#138;','&#154;','&Ugrave;','&Uacute;','&Ucirc;','&Uuml;','&ugrave;','&uacute;','&ucirc;','&uuml;','&#181;','&#215;','&Yacute;','&#159;','&yacute;','&yuml;','&#176;','&#134;','&#135;','&lt;','&gt;','&#177;','&#171;','&#187;','&#191;','&#161;','&#183;','&#149;','&#153;','&copy;','&reg;','&#167;','&#182;'];C=['À','Á','Â','Ã','Ä','Å','à','á','â','ã','ä','å','Æ','æ','ß','Ç','ç','È','É','Ê','Ë','è','é','ê','ë','ƒ','Ì','Í','Î','Ï','ì','í','î','ï','Ñ','ñ','Ò','Ó','Ô','Õ','Ö','ò','ó','ô','õ','ö','Ø','ø','Œ','œ','Š','š','Ù','Ú','Û','Ü','ù','ú','û','ü','µ','×','Ý','Ÿ','ý','ÿ','°','†','‡','<','>','±','«','»','¿','¡','·','•','™','©','®','§','¶']
	for(D,E)in zip(B,C):A=A.replace(E,D)
	return A
def encode_morse_code(message):A={'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','/':'-..-.','-':'-....-','(':'-.--.',')':'-.--.-','&':'.-...','@':'.--.-.','!':'-.-.--','$':'...-..-','%':_A,'=':'-...-','+':_A,'_':'..--.-','"':_B,'<':'.-.-','>':_B,':':'---...',';':'-.-.-.',' ':'/'};return''.join([A[B]for B in message.lower()])
def decode_morse_code(message):A=message;B={'.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f','--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l','--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r','...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x','-.--':'y','--..':'z','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9','-----':'0','--..--':',','.-.-.-':'.','..--..':'?','-..-.':'/','-....-':'-','-.--.':'(','-.--.-':')','.-...':'&','.--.-.':'@','-.-.--':'!','...-..-':'$',_A:'%','-...-':'=',_A:'+','..--.-':'_',_B:'"','.-.-':'<',_B:'>','---...':':','-.-.-.':';','/':' '};A=A.replace(' ','/').replace('_','/');return''.join([B[A]for A in A.lower()])
def ascii_to_standard_galactic_alphabet(text):B={'a':'ᔑ','b':'ܠ','c':'i','d':'↸','e':'ᒷ','f':'⎓','g':'├','h':'₸','i':'╎','j':'⋮','k':'ꖌ','l':'|:','m':'٦','n':'リ','o':'フ','p':'¡ǃ','q':'ᑖ','r':'∴','s':'߆','t':'ℸ ̣','u':'⚍','v':'⍊','w':'∷','x':'˙̸ ','y':'॥','z':'⋂','1':'⥍','2':'∠','3':'>','4':'⊐','5':'ⵎ','6':'X','7':'Δ','8':'⎕','9':'┌┐','0':'└┘'};return''.join(B.get(A,A)for A in text)
def standard_galactic_alphabet_to_ascii(text):B={'ᔑ':'a','ܠ':'b','i':'c','↸':'d','ᒷ':'e','⎓':'f','├':'g','₸':'h','╎':'i','⋮':'j','ꖌ':'k','|:':'l','٦':'m','リ':'n','フ':'o','¡ǃ':'p','ᑖ':'q','∴':'r','߆':'s','ℸ ̣':'t','⚍':'u','⍊':'v','∷':'w','˙̸ ':'x','॥':'y','⋂':'z','⥍':'1','∠':'2','>':'3','⊐':'4','ⵎ':'5','X':'6','Δ':'7','⎕':'8','┌┐':'9','└┘':'0'};return''.join(B.get(A,A)for A in text)