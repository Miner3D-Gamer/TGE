_D='2003Server'
_C='Vista'
_B='win32'
_A=None
import itertools,os,sys,functools,collections,re
_uname_cache=_A
_ver_output=re.compile('(?:([\\w ]+) ([\\w.]+) .*\\[.* ([\\d.]+)\\])')
_WIN32_SERVER_RELEASES={(5,2):_D,(6,0):'2008Server',(6,1):'2008ServerR2',(6,2):'2012Server',(6,3):'2012ServerR2',(6,_A):'post2012ServerR2'}
_WIN32_CLIENT_RELEASES={(5,0):'2000',(5,1):'XP',(5,2):_D,(5,_A):'post2003',(6,0):_C,(6,1):'7',(6,2):'8',(6,3):'8.1',(6,_A):'post8.1',(10,0):'10',(10,_A):'post10'}
def system():return uname().system
def _unknown_as_blank(val):return''if val=='unknown'else val
def _node(default=''):
	A=default
	try:import socket as B
	except ImportError:return A
	try:return B.gethostname()
	except OSError:return A
def _syscmd_ver(system='',release='',version='',supported_platforms=(_B,'win16','dos')):
	C=system;B=release;A=version
	if sys.platform not in supported_platforms:return C,B,A
	import subprocess as D
	for G in('ver','command /c ver','cmd /c ver'):
		try:E=D.check_output(G,stdin=D.DEVNULL,stderr=D.DEVNULL,text=True,encoding='locale',shell=True)
		except(OSError,D.CalledProcessError)as H:continue
		else:break
	else:return C,B,A
	E=E.strip();F=_ver_output.match(E)
	if F is not _A:
		C,B,A=F.groups()
		if B[-1]=='.':B=B[:-1]
		if A[-1]=='.':A=A[:-1]
		A=_norm_version(A)
	return C,B,A
def _norm_version(version,build=''):
	C=build;A=version;B=A.split('.')
	if C:B.append(C)
	try:D=list(map(str,map(int,B)))
	except ValueError:D=B
	A='.'.join(D[:3]);return A
def java_ver(release='',vendor='',vminfo=('','',''),osinfo=('','','')):
	D=osinfo;C=vminfo;B=vendor;A=release
	try:import java.lang
	except ImportError:return A,B,C,D
	B=_java_getprop('java.vendor',B);A=_java_getprop('java.version',A);E,F,G=C;E=_java_getprop('java.vm.name',E);G=_java_getprop('java.vm.vendor',G);F=_java_getprop('java.vm.version',F);C=E,F,G;H,I,J=D;J=_java_getprop('java.os.arch',J);H=_java_getprop('java.os.name',H);I=_java_getprop('java.os.version',I);D=H,I,J;return A,B,C,D
def win32_ver(release='',version='',csd='',ptype=''):
	H=ptype;G=version;C=csd;B=release
	try:from sys import getwindowsversion as J
	except ImportError:return B,G,C,H
	D=J()
	try:A,E,I=map(int,_syscmd_ver()[2].split('.'))
	except ValueError:A,E,I=D.platform_version or D[:3]
	G='{0}.{1}.{2}'.format(A,E,I);B=_WIN32_CLIENT_RELEASES.get((A,E))or _WIN32_CLIENT_RELEASES.get((A,_A))or B
	if D[:2]==(A,E):
		try:C='SP{}'.format(D.service_pack_major)
		except AttributeError:
			if C[:13]=='Service Pack ':C='SP'+C[13:]
	if getattr(D,'product_type',_A)==3:B=_WIN32_SERVER_RELEASES.get((A,E))or _WIN32_SERVER_RELEASES.get((A,_A))or B
	try:
		try:import winreg as F
		except ImportError:import _winreg as F
	except ImportError:pass
	else:
		try:
			K='SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion'
			with F.OpenKeyEx(F.HKEY_LOCAL_MACHINE,K)as L:H=F.QueryValueEx(L,'CurrentType')[0]
		except OSError:pass
	return B,G,C,H
def _java_getprop(name,default):
	A=default;from java.lang import System as C
	try:
		B=C.getProperty(name)
		if B is _A:return A
		return B
	except AttributeError:return A
def uname():
	H='Microsoft';D='Windows';global _uname_cache
	if _uname_cache is not _A:return _uname_cache
	try:A,F,B,C,E=G=os.uname()
	except AttributeError:A=sys.platform;F=_node();B=C=E='';G=()
	if not any(G):
		if A==_B:B,C,L,M=win32_ver();E=E or _get_machine_win32()
		if not(B and C):
			A,B,C=_syscmd_ver(A)
			if A=='Microsoft Windows':A=D
			elif A==H and B==D:
				A=D
				if'6.0'==C[:3]:B=_C
				else:B=''
		if A in(_B,'win16'):
			if not C:
				if A==_B:C='32bit'
				else:C='16bit'
			A=D
		elif A[:4]=='java':
			B,I,J,N=java_ver();A='Java';C=', '.join(J)
			if not C:C=I
	if A=='OpenVMS':
		if not B or B=='0':B=C;C=''
	if A==H and B==D:A=D;B=_C
	K=A,F,B,C,E;_uname_cache=uname_result(*map(_unknown_as_blank,K));return _uname_cache
class uname_result(collections.namedtuple('uname_result_base','system node release version machine')):
	_fields='system','node','release','version','machine','processor'
	@functools.cached_property
	def processor(self):return _unknown_as_blank(_Processor.get())
	def __iter__(A):return itertools.chain(super().__iter__(),(A.processor,))
	@classmethod
	def _make(A,iterable):
		C=len(A._fields)-1;B=A.__new__(A,*iterable)
		if len(B)!=C+1:D=f"Expected {C} arguments, got {len(B)}";raise TypeError(D)
		return B
	def __getitem__(A,key):return tuple(A)[key]
	def __len__(A):return len(tuple(iter(A)))
	def __reduce__(A):return uname_result,tuple(A)[:len(A._fields)-1]
class _Processor:
	@classmethod
	def get(A):B=getattr(A,f"get_{sys.platform}",A.from_subprocess);return B()or''
	def from_subprocess():
		try:import subprocess as A
		except ImportError:return
		try:return A.check_output(['uname','-p'],stderr=A.DEVNULL,text=True,encoding='utf8').strip()
		except(OSError,A.CalledProcessError):pass
def _get_machine_win32():return os.environ.get('PROCESSOR_ARCHITEW6432','')or os.environ.get('PROCESSOR_ARCHITECTURE','')