_Q='octal escape value %s outside of range 0-0o377'
_P='undefined character name %r'
_O='character name'
_N='missing {'
_M='bad character in group name %r'
_L='invalid group reference %d'
_K='cannot refer to an open group'
_J='MAXREPEAT'
_I='bad escape %s'
_H='  '
_G='\\'
_F='incomplete escape %s'
_E='-'
_D=')'
_C=False
_B=True
_A=None
import enum
MAGIC=20220615
from _sre import MAXREPEAT,MAXGROUPS
import _sre
class error(Exception):
 __module__='re'
 def __init__(self,msg,pattern=_A,pos=_A):
  self.msg=msg;self.pattern=pattern;self.pos=pos
  if pattern is not _A and pos is not _A:
   msg='%s at position %d'%(msg,pos)
   if isinstance(pattern,str):newline='\n'
   else:newline=b'\n'
   self.lineno=pattern.count(newline,0,pos)+1;self.colno=pos-pattern.rfind(newline,0,pos)
   if newline in pattern:msg='%s (line %d, column %d)'%(msg,self.lineno,self.colno)
  else:self.lineno=self.colno=_A
  super().__init__(msg)
class _NamedIntConstant(int):
 def __new__(cls,value,name):self=super(_NamedIntConstant,cls).__new__(cls,value);self.name=name;return self
 def __repr__(self):return self.name
 __reduce__=_A
MAXREPEAT=_NamedIntConstant(MAXREPEAT,_J)
def _makecodes(*names):items=[_NamedIntConstant(i,name)for(i,name)in enumerate(names)];globals().update({item.name:item for item in items});return items
OPCODES=_makecodes('FAILURE','SUCCESS','ANY','ANY_ALL','ASSERT','ASSERT_NOT','AT','BRANCH','CATEGORY','CHARSET','BIGCHARSET','GROUPREF','GROUPREF_EXISTS','IN','INFO','JUMP','LITERAL','MARK','MAX_UNTIL','MIN_UNTIL','NOT_LITERAL','NEGATE','RANGE','REPEAT','REPEAT_ONE','SUBPATTERN','MIN_REPEAT_ONE','ATOMIC_GROUP','POSSESSIVE_REPEAT','POSSESSIVE_REPEAT_ONE','GROUPREF_IGNORE','IN_IGNORE','LITERAL_IGNORE','NOT_LITERAL_IGNORE','GROUPREF_LOC_IGNORE','IN_LOC_IGNORE','LITERAL_LOC_IGNORE','NOT_LITERAL_LOC_IGNORE','GROUPREF_UNI_IGNORE','IN_UNI_IGNORE','LITERAL_UNI_IGNORE','NOT_LITERAL_UNI_IGNORE','RANGE_UNI_IGNORE','MIN_REPEAT','MAX_REPEAT')
del OPCODES[-2:]
ATCODES=_makecodes('AT_BEGINNING','AT_BEGINNING_LINE','AT_BEGINNING_STRING','AT_BOUNDARY','AT_NON_BOUNDARY','AT_END','AT_END_LINE','AT_END_STRING','AT_LOC_BOUNDARY','AT_LOC_NON_BOUNDARY','AT_UNI_BOUNDARY','AT_UNI_NON_BOUNDARY')
CHCODES=_makecodes('CATEGORY_DIGIT','CATEGORY_NOT_DIGIT','CATEGORY_SPACE','CATEGORY_NOT_SPACE','CATEGORY_WORD','CATEGORY_NOT_WORD','CATEGORY_LINEBREAK','CATEGORY_NOT_LINEBREAK','CATEGORY_LOC_WORD','CATEGORY_LOC_NOT_WORD','CATEGORY_UNI_DIGIT','CATEGORY_UNI_NOT_DIGIT','CATEGORY_UNI_SPACE','CATEGORY_UNI_NOT_SPACE','CATEGORY_UNI_WORD','CATEGORY_UNI_NOT_WORD','CATEGORY_UNI_LINEBREAK','CATEGORY_UNI_NOT_LINEBREAK')
OP_IGNORE={LITERAL:LITERAL_IGNORE,NOT_LITERAL:NOT_LITERAL_IGNORE}
OP_LOCALE_IGNORE={LITERAL:LITERAL_LOC_IGNORE,NOT_LITERAL:NOT_LITERAL_LOC_IGNORE}
OP_UNICODE_IGNORE={LITERAL:LITERAL_UNI_IGNORE,NOT_LITERAL:NOT_LITERAL_UNI_IGNORE}
AT_MULTILINE={AT_BEGINNING:AT_BEGINNING_LINE,AT_END:AT_END_LINE}
AT_LOCALE={AT_BOUNDARY:AT_LOC_BOUNDARY,AT_NON_BOUNDARY:AT_LOC_NON_BOUNDARY}
AT_UNICODE={AT_BOUNDARY:AT_UNI_BOUNDARY,AT_NON_BOUNDARY:AT_UNI_NON_BOUNDARY}
CH_LOCALE={CATEGORY_DIGIT:CATEGORY_DIGIT,CATEGORY_NOT_DIGIT:CATEGORY_NOT_DIGIT,CATEGORY_SPACE:CATEGORY_SPACE,CATEGORY_NOT_SPACE:CATEGORY_NOT_SPACE,CATEGORY_WORD:CATEGORY_LOC_WORD,CATEGORY_NOT_WORD:CATEGORY_LOC_NOT_WORD,CATEGORY_LINEBREAK:CATEGORY_LINEBREAK,CATEGORY_NOT_LINEBREAK:CATEGORY_NOT_LINEBREAK}
CH_UNICODE={CATEGORY_DIGIT:CATEGORY_UNI_DIGIT,CATEGORY_NOT_DIGIT:CATEGORY_UNI_NOT_DIGIT,CATEGORY_SPACE:CATEGORY_UNI_SPACE,CATEGORY_NOT_SPACE:CATEGORY_UNI_NOT_SPACE,CATEGORY_WORD:CATEGORY_UNI_WORD,CATEGORY_NOT_WORD:CATEGORY_UNI_NOT_WORD,CATEGORY_LINEBREAK:CATEGORY_UNI_LINEBREAK,CATEGORY_NOT_LINEBREAK:CATEGORY_UNI_NOT_LINEBREAK}
SRE_FLAG_TEMPLATE=1
SRE_FLAG_IGNORECASE=2
SRE_FLAG_LOCALE=4
SRE_FLAG_MULTILINE=8
SRE_FLAG_DOTALL=16
SRE_FLAG_UNICODE=32
SRE_FLAG_VERBOSE=64
SRE_FLAG_DEBUG=128
SRE_FLAG_ASCII=256
SRE_INFO_PREFIX=1
SRE_INFO_LITERAL=2
SRE_INFO_CHARSET=4
SPECIAL_CHARS='.\\[{()*+?^$|'
REPEAT_CHARS='*+?{'
DIGITS=frozenset('0123456789')
OCTDIGITS=frozenset('01234567')
HEXDIGITS=frozenset('0123456789abcdefABCDEF')
ASCIILETTERS=frozenset('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
WHITESPACE=frozenset(' \t\n\r\x0b\x0c')
_REPEATCODES=frozenset({MIN_REPEAT,MAX_REPEAT,POSSESSIVE_REPEAT})
_UNITCODES=frozenset({ANY,RANGE,IN,LITERAL,NOT_LITERAL,CATEGORY})
ESCAPES={'\\a':(LITERAL,ord('\x07')),'\\b':(LITERAL,ord('\x08')),'\\f':(LITERAL,ord('\x0c')),'\\n':(LITERAL,ord('\n')),'\\r':(LITERAL,ord('\r')),'\\t':(LITERAL,ord('\t')),'\\v':(LITERAL,ord('\x0b')),'\\\\':(LITERAL,ord(_G))}
CATEGORIES={'\\A':(AT,AT_BEGINNING_STRING),'\\b':(AT,AT_BOUNDARY),'\\B':(AT,AT_NON_BOUNDARY),'\\d':(IN,[(CATEGORY,CATEGORY_DIGIT)]),'\\D':(IN,[(CATEGORY,CATEGORY_NOT_DIGIT)]),'\\s':(IN,[(CATEGORY,CATEGORY_SPACE)]),'\\S':(IN,[(CATEGORY,CATEGORY_NOT_SPACE)]),'\\w':(IN,[(CATEGORY,CATEGORY_WORD)]),'\\W':(IN,[(CATEGORY,CATEGORY_NOT_WORD)]),'\\Z':(AT,AT_END_STRING)}
FLAGS={'i':SRE_FLAG_IGNORECASE,'L':SRE_FLAG_LOCALE,'m':SRE_FLAG_MULTILINE,'s':SRE_FLAG_DOTALL,'x':SRE_FLAG_VERBOSE,'a':SRE_FLAG_ASCII,'t':SRE_FLAG_TEMPLATE,'u':SRE_FLAG_UNICODE}
TYPE_FLAGS=SRE_FLAG_ASCII|SRE_FLAG_LOCALE|SRE_FLAG_UNICODE
GLOBAL_FLAGS=SRE_FLAG_DEBUG|SRE_FLAG_TEMPLATE
class State:
 def __init__(self):self.flags=0;self.groupdict={};self.groupwidths=[_A];self.lookbehindgroups=_A;self.grouprefpos={}
 @property
 def groups(self):return len(self.groupwidths)
 def opengroup(self,name=_A):
  gid=self.groups;self.groupwidths.append(_A)
  if self.groups>MAXGROUPS:raise error('too many groups')
  if name is not _A:
   ogid=self.groupdict.get(name,_A)
   if ogid is not _A:raise error('redefinition of group name %r as group %d; was group %d'%(name,gid,ogid))
   self.groupdict[name]=gid
  return gid
 def closegroup(self,gid,p):self.groupwidths[gid]=p.getwidth()
 def checkgroup(self,gid):return gid<self.groups and self.groupwidths[gid]is not _A
 def checklookbehindgroup(self,gid,source):
  if self.lookbehindgroups is not _A:
   if not self.checkgroup(gid):raise source.error(_K)
   if gid>=self.lookbehindgroups:raise source.error('cannot refer to group defined in the same lookbehind subpattern')
class SubPattern:
 def __init__(self,state,data=_A):
  self.state=state
  if data is _A:data=[]
  self.data=data;self.width=_A
 def dump(self,level=0):
  nl=_B;seqtypes=tuple,list
  for(op,av)in self.data:
   print(level*_H+str(op),end='')
   if op is IN:
    print()
    for(op,a)in av:print((level+1)*_H+str(op),a)
   elif op is BRANCH:
    print()
    for(i,a)in enumerate(av[1]):
     if i:print(level*_H+'OR')
     a.dump(level+1)
   elif op is GROUPREF_EXISTS:
    condgroup,item_yes,item_no=av;print('',condgroup);item_yes.dump(level+1)
    if item_no:print(level*_H+'ELSE');item_no.dump(level+1)
   elif isinstance(av,seqtypes):
    nl=_C
    for a in av:
     if isinstance(a,SubPattern):
      if not nl:print()
      a.dump(level+1);nl=_B
     else:
      if not nl:print(' ',end='')
      print(a,end='');nl=_C
    if not nl:print()
   else:print('',av)
 def __repr__(self):return repr(self.data)
 def __len__(self):return len(self.data)
 def __delitem__(self,index):del self.data[index]
 def __getitem__(self,index):
  if isinstance(index,slice):return SubPattern(self.state,self.data[index])
  return self.data[index]
 def __setitem__(self,index,code):self.data[index]=code
 def insert(self,index,code):self.data.insert(index,code)
 def append(self,code):self.data.append(code)
 def getwidth(self):
  if self.width is not _A:return self.width
  lo=hi=0
  for(op,av)in self.data:
   if op is BRANCH:
    i=MAXREPEAT-1;j=0
    for av in av[1]:l,h=av.getwidth();i=min(i,l);j=max(j,h)
    lo=lo+i;hi=hi+j
   elif op is ATOMIC_GROUP:i,j=av.getwidth();lo=lo+i;hi=hi+j
   elif op is SUBPATTERN:i,j=av[-1].getwidth();lo=lo+i;hi=hi+j
   elif op in _REPEATCODES:i,j=av[2].getwidth();lo=lo+i*av[0];hi=hi+j*av[1]
   elif op in _UNITCODES:lo=lo+1;hi=hi+1
   elif op is GROUPREF:i,j=self.state.groupwidths[av];lo=lo+i;hi=hi+j
   elif op is GROUPREF_EXISTS:
    i,j=av[1].getwidth()
    if av[2]is not _A:l,h=av[2].getwidth();i=min(i,l);j=max(j,h)
    else:i=0
    lo=lo+i;hi=hi+j
   elif op is SUCCESS:break
  self.width=min(lo,MAXREPEAT-1),min(hi,MAXREPEAT);return self.width
class Tokenizer:
 def __init__(self,string):
  self.istext=isinstance(string,str);self.string=string
  if not self.istext:string=str(string,'latin1')
  self.decoded_string=string;self.index=0;self.next=_A;self.__next()
 def __next(self):
  index=self.index
  try:char=self.decoded_string[index]
  except IndexError:self.next=_A;return
  if char==_G:
   index+=1
   try:char+=self.decoded_string[index]
   except IndexError:raise error('bad escape (end of pattern)',self.string,len(self.string)-1)from _A
  self.index=index+1;self.next=char
 def match(self,char):
  if char==self.next:self.__next();return _B
  return _C
 def get(self):this=self.next;self.__next();return this
 def getwhile(self,n,charset):
  result=''
  for _ in range(n):
   c=self.next
   if c not in charset:break
   result+=c;self.__next()
  return result
 def getuntil(self,terminator,name):
  A='missing ';result=''
  while _B:
   c=self.next;self.__next()
   if c is _A:
    if not result:raise self.error(A+name)
    raise self.error('missing %s, unterminated name'%terminator,len(result))
   if c==terminator:
    if not result:raise self.error(A+name,1)
    break
   result+=c
  return result
 @property
 def pos(self):return self.index-len(self.next or'')
 def tell(self):return self.index-len(self.next or'')
 def seek(self,index):self.index=index;self.__next()
 def error(self,msg,offset=0):
  A='ascii'
  if not self.istext:msg=msg.encode(A,'backslashreplace').decode(A)
  return error(msg,self.string,self.tell()-offset)
 def checkgroupname(self,name,offset,nested):
  if not name.isidentifier():msg=_M%name;raise self.error(msg,len(name)+offset)
  if not(self.istext or name.isascii()):import warnings;warnings.warn('bad character in group name %a at position %d'%(name,self.tell()-len(name)-offset),DeprecationWarning,stacklevel=nested+7)
def _class_escape(source,escape):
 code=ESCAPES.get(escape)
 if code:return code
 code=CATEGORIES.get(escape)
 if code and code[0]is IN:return code
 try:
  c=escape[1:2]
  if c=='x':
   escape+=source.getwhile(2,HEXDIGITS)
   if len(escape)!=4:raise source.error(_F%escape,len(escape))
   return LITERAL,int(escape[2:],16)
  elif c=='u'and source.istext:
   escape+=source.getwhile(4,HEXDIGITS)
   if len(escape)!=6:raise source.error(_F%escape,len(escape))
   return LITERAL,int(escape[2:],16)
  elif c=='U'and source.istext:
   escape+=source.getwhile(8,HEXDIGITS)
   if len(escape)!=10:raise source.error(_F%escape,len(escape))
   c=int(escape[2:],16);chr(c);return LITERAL,c
  elif c=='N'and source.istext:
   import unicodedata
   if not source.match('{'):raise source.error(_N)
   charname=source.getuntil('}',_O)
   try:c=ord(unicodedata.lookup(charname))
   except(KeyError,TypeError):raise source.error(_P%charname,len(charname)+len('\\N{}'))from _A
   return LITERAL,c
  elif c in OCTDIGITS:
   escape+=source.getwhile(2,OCTDIGITS);c=int(escape[1:],8)
   if c>255:raise source.error(_Q%escape,len(escape))
   return LITERAL,c
  elif c in DIGITS:raise ValueError
  if len(escape)==2:
   if c in ASCIILETTERS:raise source.error(_I%escape,len(escape))
   return LITERAL,ord(escape[1])
 except ValueError:pass
 raise source.error(_I%escape,len(escape))
def _escape(source,escape,state):
 code=CATEGORIES.get(escape)
 if code:return code
 code=ESCAPES.get(escape)
 if code:return code
 try:
  c=escape[1:2]
  if c=='x':
   escape+=source.getwhile(2,HEXDIGITS)
   if len(escape)!=4:raise source.error(_F%escape,len(escape))
   return LITERAL,int(escape[2:],16)
  elif c=='u'and source.istext:
   escape+=source.getwhile(4,HEXDIGITS)
   if len(escape)!=6:raise source.error(_F%escape,len(escape))
   return LITERAL,int(escape[2:],16)
  elif c=='U'and source.istext:
   escape+=source.getwhile(8,HEXDIGITS)
   if len(escape)!=10:raise source.error(_F%escape,len(escape))
   c=int(escape[2:],16);chr(c);return LITERAL,c
  elif c=='N'and source.istext:
   import unicodedata
   if not source.match('{'):raise source.error(_N)
   charname=source.getuntil('}',_O)
   try:c=ord(unicodedata.lookup(charname))
   except(KeyError,TypeError):raise source.error(_P%charname,len(charname)+len('\\N{}'))from _A
   return LITERAL,c
  elif c=='0':escape+=source.getwhile(2,OCTDIGITS);return LITERAL,int(escape[1:],8)
  elif c in DIGITS:
   if source.next in DIGITS:
    escape+=source.get()
    if escape[1]in OCTDIGITS and escape[2]in OCTDIGITS and source.next in OCTDIGITS:
     escape+=source.get();c=int(escape[1:],8)
     if c>255:raise source.error(_Q%escape,len(escape))
     return LITERAL,c
   group=int(escape[1:])
   if group<state.groups:
    if not state.checkgroup(group):raise source.error(_K,len(escape))
    state.checklookbehindgroup(group,source);return GROUPREF,group
   raise source.error(_L%group,len(escape)-1)
  if len(escape)==2:
   if c in ASCIILETTERS:raise source.error(_I%escape,len(escape))
   return LITERAL,ord(escape[1])
 except ValueError:pass
 raise source.error(_I%escape,len(escape))
def _uniq(items):return list(dict.fromkeys(items))
def _parse_sub(source,state,verbose,nested):
 items=[];itemsappend=items.append;sourcematch=source.match;start=source.tell()
 while _B:
  itemsappend(_parse(source,state,verbose,nested+1,not nested and not items))
  if not sourcematch('|'):break
  if not nested:verbose=state.flags&SRE_FLAG_VERBOSE
 if len(items)==1:return items[0]
 subpattern=SubPattern(state)
 while _B:
  prefix=_A
  for item in items:
   if not item:break
   if prefix is _A:prefix=item[0]
   elif item[0]!=prefix:break
  else:
   for item in items:del item[0]
   subpattern.append(prefix);continue
  break
 set=[]
 for item in items:
  if len(item)!=1:break
  op,av=item[0]
  if op is LITERAL:set.append((op,av))
  elif op is IN and av[0][0]is not NEGATE:set.extend(av)
  else:break
 else:subpattern.append((IN,_uniq(set)));return subpattern
 subpattern.append((BRANCH,(_A,items)));return subpattern
def _parse(source,state,verbose,nested,first=_C):
 H='unknown group name %r';G='the repetition number is too large';F='bad character range %s-%s';E='unterminated character set';D='missing ), unterminated subpattern';C='group name';B='unexpected end of pattern';A='?';subpattern=SubPattern(state);subpatternappend=subpattern.append;sourceget=source.get;sourcematch=source.match;_len=len;_ord=ord
 while _B:
  this=source.next
  if this is _A:break
  if this in'|)':break
  sourceget()
  if verbose:
   if this in WHITESPACE:continue
   if this=='#':
    while _B:
     this=sourceget()
     if this is _A or this=='\n':break
    continue
  if this[0]==_G:code=_escape(source,this,state);subpatternappend(code)
  elif this not in SPECIAL_CHARS:subpatternappend((LITERAL,_ord(this)))
  elif this=='[':
   here=source.tell()-1;set=[];setappend=set.append
   if source.next=='[':import warnings;warnings.warn('Possible nested set at position %d'%source.tell(),FutureWarning,stacklevel=nested+6)
   negate=sourcematch('^')
   while _B:
    this=sourceget()
    if this is _A:raise source.error(E,source.tell()-here)
    if this==']'and set:break
    elif this[0]==_G:code1=_class_escape(source,this)
    else:
     if set and this in'-&~|'and source.next==this:import warnings;warnings.warn('Possible set %s at position %d'%('difference'if this==_E else'intersection'if this=='&'else'symmetric difference'if this=='~'else'union',source.tell()-1),FutureWarning,stacklevel=nested+6)
     code1=LITERAL,_ord(this)
    if sourcematch(_E):
     that=sourceget()
     if that is _A:raise source.error(E,source.tell()-here)
     if that==']':
      if code1[0]is IN:code1=code1[1][0]
      setappend(code1);setappend((LITERAL,_ord(_E)));break
     if that[0]==_G:code2=_class_escape(source,that)
     else:
      if that==_E:import warnings;warnings.warn('Possible set difference at position %d'%(source.tell()-2),FutureWarning,stacklevel=nested+6)
      code2=LITERAL,_ord(that)
     if code1[0]!=LITERAL or code2[0]!=LITERAL:msg=F%(this,that);raise source.error(msg,len(this)+1+len(that))
     lo=code1[1];hi=code2[1]
     if hi<lo:msg=F%(this,that);raise source.error(msg,len(this)+1+len(that))
     setappend((RANGE,(lo,hi)))
    else:
     if code1[0]is IN:code1=code1[1][0]
     setappend(code1)
   set=_uniq(set)
   if _len(set)==1 and set[0][0]is LITERAL:
    if negate:subpatternappend((NOT_LITERAL,set[0][1]))
    else:subpatternappend(set[0])
   else:
    if negate:set.insert(0,(NEGATE,_A))
    subpatternappend((IN,set))
  elif this in REPEAT_CHARS:
   here=source.tell()
   if this==A:min,max=0,1
   elif this=='*':min,max=0,MAXREPEAT
   elif this=='+':min,max=1,MAXREPEAT
   elif this=='{':
    if source.next=='}':subpatternappend((LITERAL,_ord(this)));continue
    min,max=0,MAXREPEAT;lo=hi=''
    while source.next in DIGITS:lo+=sourceget()
    if sourcematch(','):
     while source.next in DIGITS:hi+=sourceget()
    else:hi=lo
    if not sourcematch('}'):subpatternappend((LITERAL,_ord(this)));source.seek(here);continue
    if lo:
     min=int(lo)
     if min>=MAXREPEAT:raise OverflowError(G)
    if hi:
     max=int(hi)
     if max>=MAXREPEAT:raise OverflowError(G)
     if max<min:raise source.error('min repeat greater than max repeat',source.tell()-here)
   else:raise AssertionError('unsupported quantifier %r'%(char,))
   if subpattern:item=subpattern[-1:]
   else:item=_A
   if not item or item[0][0]is AT:raise source.error('nothing to repeat',source.tell()-here+len(this))
   if item[0][0]in _REPEATCODES:raise source.error('multiple repeat',source.tell()-here+len(this))
   if item[0][0]is SUBPATTERN:
    group,add_flags,del_flags,p=item[0][1]
    if group is _A and not add_flags and not del_flags:item=p
   if sourcematch(A):subpattern[-1]=MIN_REPEAT,(min,max,item)
   elif sourcematch('+'):subpattern[-1]=POSSESSIVE_REPEAT,(min,max,item)
   else:subpattern[-1]=MAX_REPEAT,(min,max,item)
  elif this=='.':subpatternappend((ANY,_A))
  elif this=='(':
   start=source.tell()-1;capture=_B;atomic=_C;name=_A;add_flags=0;del_flags=0
   if sourcematch(A):
    char=sourceget()
    if char is _A:raise source.error(B)
    if char=='P':
     if sourcematch('<'):name=source.getuntil('>',C);source.checkgroupname(name,1,nested)
     elif sourcematch('='):
      name=source.getuntil(_D,C);source.checkgroupname(name,1,nested);gid=state.groupdict.get(name)
      if gid is _A:msg=H%name;raise source.error(msg,len(name)+1)
      if not state.checkgroup(gid):raise source.error(_K,len(name)+1)
      state.checklookbehindgroup(gid,source);subpatternappend((GROUPREF,gid));continue
     else:
      char=sourceget()
      if char is _A:raise source.error(B)
      raise source.error('unknown extension ?P'+char,len(char)+2)
    elif char==':':capture=_C
    elif char=='#':
     while _B:
      if source.next is _A:raise source.error('missing ), unterminated comment',source.tell()-start)
      if sourceget()==_D:break
     continue
    elif char in'=!<':
     dir=1
     if char=='<':
      char=sourceget()
      if char is _A:raise source.error(B)
      if char not in'=!':raise source.error('unknown extension ?<'+char,len(char)+2)
      dir=-1;lookbehindgroups=state.lookbehindgroups
      if lookbehindgroups is _A:state.lookbehindgroups=state.groups
     p=_parse_sub(source,state,verbose,nested+1)
     if dir<0:
      if lookbehindgroups is _A:state.lookbehindgroups=_A
     if not sourcematch(_D):raise source.error(D,source.tell()-start)
     if char=='=':subpatternappend((ASSERT,(dir,p)))
     else:subpatternappend((ASSERT_NOT,(dir,p)))
     continue
    elif char=='(':
     condname=source.getuntil(_D,C)
     if condname.isidentifier():
      source.checkgroupname(condname,1,nested);condgroup=state.groupdict.get(condname)
      if condgroup is _A:msg=H%condname;raise source.error(msg,len(condname)+1)
     else:
      try:
       condgroup=int(condname)
       if condgroup<0:raise ValueError
      except ValueError:msg=_M%condname;raise source.error(msg,len(condname)+1)from _A
      if not condgroup:raise source.error('bad group number',len(condname)+1)
      if condgroup>=MAXGROUPS:msg=_L%condgroup;raise source.error(msg,len(condname)+1)
      if condgroup not in state.grouprefpos:state.grouprefpos[condgroup]=source.tell()-len(condname)-1
      if not(condname.isdecimal()and condname.isascii()):import warnings;warnings.warn('bad character in group name %s at position %d'%(repr(condname)if source.istext else ascii(condname),source.tell()-len(condname)-1),DeprecationWarning,stacklevel=nested+6)
     state.checklookbehindgroup(condgroup,source);item_yes=_parse(source,state,verbose,nested+1)
     if source.match('|'):
      item_no=_parse(source,state,verbose,nested+1)
      if source.next=='|':raise source.error('conditional backref with more than two branches')
     else:item_no=_A
     if not source.match(_D):raise source.error(D,source.tell()-start)
     subpatternappend((GROUPREF_EXISTS,(condgroup,item_yes,item_no)));continue
    elif char=='>':capture=_C;atomic=_B
    elif char in FLAGS or char==_E:
     flags=_parse_flags(source,state,char)
     if flags is _A:
      if not first or subpattern:raise source.error('global flags not at the start of the expression',source.tell()-start)
      verbose=state.flags&SRE_FLAG_VERBOSE;continue
     add_flags,del_flags=flags;capture=_C
    else:raise source.error('unknown extension ?'+char,len(char)+1)
   if capture:
    try:group=state.opengroup(name)
    except error as err:raise source.error(err.msg,len(name)+1)from _A
   else:group=_A
   sub_verbose=(verbose or add_flags&SRE_FLAG_VERBOSE)and not del_flags&SRE_FLAG_VERBOSE;p=_parse_sub(source,state,sub_verbose,nested+1)
   if not source.match(_D):raise source.error(D,source.tell()-start)
   if group is not _A:state.closegroup(group,p)
   if atomic:assert group is _A;subpatternappend((ATOMIC_GROUP,p))
   else:subpatternappend((SUBPATTERN,(group,add_flags,del_flags,p)))
  elif this=='^':subpatternappend((AT,AT_BEGINNING))
  elif this=='$':subpatternappend((AT,AT_END))
  else:raise AssertionError('unsupported special character %r'%(char,))
 for i in range(len(subpattern))[::-1]:
  op,av=subpattern[i]
  if op is SUBPATTERN:
   group,add_flags,del_flags,p=av
   if group is _A and not add_flags and not del_flags:subpattern[i:i+1]=p
 return subpattern
def _parse_flags(source,state,char):
 D='missing :';C='missing flag';B='missing -, : or )';A='unknown flag';sourceget=source.get;add_flags=0;del_flags=0
 if char!=_E:
  while _B:
   flag=FLAGS[char]
   if source.istext:
    if char=='L':msg="bad inline flags: cannot use 'L' flag with a str pattern";raise source.error(msg)
   elif char=='u':msg="bad inline flags: cannot use 'u' flag with a bytes pattern";raise source.error(msg)
   add_flags|=flag
   if flag&TYPE_FLAGS and add_flags&TYPE_FLAGS!=flag:msg="bad inline flags: flags 'a', 'u' and 'L' are incompatible";raise source.error(msg)
   char=sourceget()
   if char is _A:raise source.error(B)
   if char in')-:':break
   if char not in FLAGS:msg=A if char.isalpha()else B;raise source.error(msg,len(char))
 if char==_D:state.flags|=add_flags;return
 if add_flags&GLOBAL_FLAGS:raise source.error('bad inline flags: cannot turn on global flag',1)
 if char==_E:
  char=sourceget()
  if char is _A:raise source.error(C)
  if char not in FLAGS:msg=A if char.isalpha()else C;raise source.error(msg,len(char))
  while _B:
   flag=FLAGS[char]
   if flag&TYPE_FLAGS:msg="bad inline flags: cannot turn off flags 'a', 'u' and 'L'";raise source.error(msg)
   del_flags|=flag;char=sourceget()
   if char is _A:raise source.error(D)
   if char==':':break
   if char not in FLAGS:msg=A if char.isalpha()else D;raise source.error(msg,len(char))
 assert char==':'
 if del_flags&GLOBAL_FLAGS:raise source.error('bad inline flags: cannot turn off global flag',1)
 if add_flags&del_flags:raise source.error('bad inline flags: flag turned on and off',1)
 return add_flags,del_flags
def fix_flags(src,flags):
 if isinstance(src,str):
  if flags&SRE_FLAG_LOCALE:raise ValueError('cannot use LOCALE flag with a str pattern')
  if not flags&SRE_FLAG_ASCII:flags|=SRE_FLAG_UNICODE
  elif flags&SRE_FLAG_UNICODE:raise ValueError('ASCII and UNICODE flags are incompatible')
 else:
  if flags&SRE_FLAG_UNICODE:raise ValueError('cannot use UNICODE flag with a bytes pattern')
  if flags&SRE_FLAG_LOCALE and flags&SRE_FLAG_ASCII:raise ValueError('ASCII and LOCALE flags are incompatible')
 return flags
def parse(str,flags=0,state=_A):
 source=Tokenizer(str)
 if state is _A:state=State()
 state.flags=flags;state.str=str;p=_parse_sub(source,state,flags&SRE_FLAG_VERBOSE,0);p.state.flags=fix_flags(str,p.state.flags)
 if source.next is not _A:assert source.next==_D;raise source.error('unbalanced parenthesis')
 for g in p.state.grouprefpos:
  if g>=p.state.groups:msg=_L%g;raise error(msg,str,p.state.grouprefpos[g])
 if flags&SRE_FLAG_DEBUG:p.dump()
 return p
_EXTRA_CASES={105:(305,),115:(383,),181:(956,),305:(105,),383:(115,),837:(953,8126),912:(8147,),944:(8163,),946:(976,),949:(1013,),952:(977,),953:(837,8126),954:(1008,),956:(181,),960:(982,),961:(1009,),962:(963,),963:(962,),966:(981,),976:(946,),977:(952,),981:(966,),982:(960,),1008:(954,),1009:(961,),1013:(949,),1074:(7296,),1076:(7297,),1086:(7298,),1089:(7299,),1090:(7300,7301),1098:(7302,),1123:(7303,),7296:(1074,),7297:(1076,),7298:(1086,),7299:(1089,),7300:(1090,7301),7301:(1090,7300),7302:(1098,),7303:(1123,),7304:(42571,),7777:(7835,),7835:(7777,),8126:(837,953),8147:(912,),8163:(944,),42571:(7304,),64261:(64262,),64262:(64261,)}
assert _sre.MAGIC==MAGIC,'SRE module mismatch'
_LITERAL_CODES={LITERAL,NOT_LITERAL}
_SUCCESS_CODES={SUCCESS,FAILURE}
_ASSERT_CODES={ASSERT,ASSERT_NOT}
_UNIT_CODES=_LITERAL_CODES|{ANY,IN}
_REPEATING_CODES={MIN_REPEAT:(REPEAT,MIN_UNTIL,MIN_REPEAT_ONE),MAX_REPEAT:(REPEAT,MAX_UNTIL,REPEAT_ONE),POSSESSIVE_REPEAT:(POSSESSIVE_REPEAT,SUCCESS,POSSESSIVE_REPEAT_ONE)}
def _combine_flags(flags,add_flags,del_flags,TYPE_FLAGS=TYPE_FLAGS):
 if add_flags&TYPE_FLAGS:flags&=~TYPE_FLAGS
 return(flags|add_flags)&~del_flags
def _compile2(code,pattern,flags):
 emit=code.append;_len=len;LITERAL_CODES=_LITERAL_CODES;REPEATING_CODES=_REPEATING_CODES;SUCCESS_CODES=_SUCCESS_CODES;ASSERT_CODES=_ASSERT_CODES;iscased=_A;tolower=_A;fixes=_A
 if flags&SRE_FLAG_IGNORECASE and not flags&SRE_FLAG_LOCALE:
  if flags&SRE_FLAG_UNICODE:iscased=_sre.unicode_iscased;tolower=_sre.unicode_tolower;fixes=_EXTRA_CASES
  else:iscased=_sre.ascii_iscased;tolower=_sre.ascii_tolower
 for(op,av)in pattern:
  if op in LITERAL_CODES:
   if not flags&SRE_FLAG_IGNORECASE:emit(op);emit(av)
   elif flags&SRE_FLAG_LOCALE:emit(OP_LOCALE_IGNORE[op]);emit(av)
   elif not iscased(av):emit(op);emit(av)
   else:
    lo=tolower(av)
    if not fixes:emit(OP_IGNORE[op]);emit(lo)
    elif lo not in fixes:emit(OP_UNICODE_IGNORE[op]);emit(lo)
    else:
     emit(IN_UNI_IGNORE);skip=_len(code);emit(0)
     if op is NOT_LITERAL:emit(NEGATE)
     for k in(lo,)+fixes[lo]:emit(LITERAL);emit(k)
     emit(FAILURE);code[skip]=_len(code)-skip
  elif op is IN:
   charset,hascased=_optimize_charset(av,iscased,tolower,fixes)
   if flags&SRE_FLAG_IGNORECASE and flags&SRE_FLAG_LOCALE:emit(IN_LOC_IGNORE)
   elif not hascased:emit(IN)
   elif not fixes:emit(IN_IGNORE)
   else:emit(IN_UNI_IGNORE)
   skip=_len(code);emit(0);_compile_charset(charset,flags,code);code[skip]=_len(code)-skip
  elif op is ANY:
   if flags&SRE_FLAG_DOTALL:emit(ANY_ALL)
   else:emit(ANY)
  elif op in REPEATING_CODES:
   if flags&SRE_FLAG_TEMPLATE:raise error('internal: unsupported template operator %r'%(op,))
   if _simple(av[2]):emit(REPEATING_CODES[op][2]);skip=_len(code);emit(0);emit(av[0]);emit(av[1]);_compile2(code,av[2],flags);emit(SUCCESS);code[skip]=_len(code)-skip
   else:emit(REPEATING_CODES[op][0]);skip=_len(code);emit(0);emit(av[0]);emit(av[1]);_compile2(code,av[2],flags);code[skip]=_len(code)-skip;emit(REPEATING_CODES[op][1])
  elif op is SUBPATTERN:
   group,add_flags,del_flags,p=av
   if group:emit(MARK);emit((group-1)*2)
   _compile2(code,p,_combine_flags(flags,add_flags,del_flags))
   if group:emit(MARK);emit((group-1)*2+1)
  elif op is ATOMIC_GROUP:emit(ATOMIC_GROUP);skip=_len(code);emit(0);_compile2(code,av,flags);emit(SUCCESS);code[skip]=_len(code)-skip
  elif op in SUCCESS_CODES:emit(op)
  elif op in ASSERT_CODES:
   emit(op);skip=_len(code);emit(0)
   if av[0]>=0:emit(0)
   else:
    lo,hi=av[1].getwidth()
    if lo!=hi:raise error('look-behind requires fixed-width pattern')
    emit(lo)
   _compile2(code,av[1],flags);emit(SUCCESS);code[skip]=_len(code)-skip
  elif op is AT:
   emit(op)
   if flags&SRE_FLAG_MULTILINE:av=AT_MULTILINE.get(av,av)
   if flags&SRE_FLAG_LOCALE:av=AT_LOCALE.get(av,av)
   elif flags&SRE_FLAG_UNICODE:av=AT_UNICODE.get(av,av)
   emit(av)
  elif op is BRANCH:
   emit(op);tail=[];tailappend=tail.append
   for av in av[1]:skip=_len(code);emit(0);_compile2(code,av,flags);emit(JUMP);tailappend(_len(code));emit(0);code[skip]=_len(code)-skip
   emit(FAILURE)
   for tail in tail:code[tail]=_len(code)-tail
  elif op is CATEGORY:
   emit(op)
   if flags&SRE_FLAG_LOCALE:av=CH_LOCALE[av]
   elif flags&SRE_FLAG_UNICODE:av=CH_UNICODE[av]
   emit(av)
  elif op is GROUPREF:
   if not flags&SRE_FLAG_IGNORECASE:emit(op)
   elif flags&SRE_FLAG_LOCALE:emit(GROUPREF_LOC_IGNORE)
   elif not fixes:emit(GROUPREF_IGNORE)
   else:emit(GROUPREF_UNI_IGNORE)
   emit(av-1)
  elif op is GROUPREF_EXISTS:
   emit(op);emit(av[0]-1);skipyes=_len(code);emit(0);_compile2(code,av[1],flags)
   if av[2]:emit(JUMP);skipno=_len(code);emit(0);code[skipyes]=_len(code)-skipyes+1;_compile2(code,av[2],flags);code[skipno]=_len(code)-skipno
   else:code[skipyes]=_len(code)-skipyes+1
  else:raise error('internal: unsupported operand type %r'%(op,))
def _compile_charset(charset,flags,code):
 emit=code.append
 for(op,av)in charset:
  emit(op)
  if op is NEGATE:0
  elif op is LITERAL:emit(av)
  elif op is RANGE or op is RANGE_UNI_IGNORE:emit(av[0]);emit(av[1])
  elif op is CHARSET:code.extend(av)
  elif op is BIGCHARSET:code.extend(av)
  elif op is CATEGORY:
   if flags&SRE_FLAG_LOCALE:emit(CH_LOCALE[av])
   elif flags&SRE_FLAG_UNICODE:emit(CH_UNICODE[av])
   else:emit(av)
  else:raise error('internal: unsupported set operator %r'%(op,))
 emit(FAILURE)
def _optimize_charset(charset,iscased=_A,fixup=_A,fixes=_A):
 out=[];tail=[];charmap=bytearray(256);hascased=_C
 for(op,av)in charset:
  while _B:
   try:
    if op is LITERAL:
     if fixup:
      lo=fixup(av);charmap[lo]=1
      if fixes and lo in fixes:
       for k in fixes[lo]:charmap[k]=1
      if not hascased and iscased(av):hascased=_B
     else:charmap[av]=1
    elif op is RANGE:
     r=range(av[0],av[1]+1)
     if fixup:
      if fixes:
       for i in map(fixup,r):
        charmap[i]=1
        if i in fixes:
         for k in fixes[i]:charmap[k]=1
      else:
       for i in map(fixup,r):charmap[i]=1
      if not hascased:hascased=any(map(iscased,r))
     else:
      for i in r:charmap[i]=1
    elif op is NEGATE:out.append((op,av))
    else:tail.append((op,av))
   except IndexError:
    if len(charmap)==256:charmap+=b'\x00'*65280;continue
    if fixup:
     hascased=_B
     if op is RANGE:op=RANGE_UNI_IGNORE
    tail.append((op,av))
   break
 runs=[];q=0
 while _B:
  p=charmap.find(1,q)
  if p<0:break
  if len(runs)>=2:runs=_A;break
  q=charmap.find(0,p)
  if q<0:runs.append((p,len(charmap)));break
  runs.append((p,q))
 if runs is not _A:
  for(p,q)in runs:
   if q-p==1:out.append((LITERAL,p))
   else:out.append((RANGE,(p,q-1)))
  out+=tail
  if hascased or len(out)<len(charset):return out,hascased
  return charset,hascased
 if len(charmap)==256:data=_mk_bitmap(charmap);out.append((CHARSET,data));out+=tail;return out,hascased
 charmap=bytes(charmap);comps={};mapping=bytearray(256);block=0;data=bytearray()
 for i in range(0,65536,256):
  chunk=charmap[i:i+256]
  if chunk in comps:mapping[i//256]=comps[chunk]
  else:mapping[i//256]=comps[chunk]=block;block+=1;data+=chunk
 data=_mk_bitmap(data);data[0:0]=[block]+_bytes_to_codes(mapping);out.append((BIGCHARSET,data));out+=tail;return out,hascased
_CODEBITS=_sre.CODESIZE*8
MAXCODE=(1<<_CODEBITS)-1
_BITS_TRANS=b'0'+b'1'*255
def _mk_bitmap(bits,_CODEBITS=_CODEBITS,_int=int):s=bits.translate(_BITS_TRANS)[::-1];return[_int(s[i-_CODEBITS:i],2)for i in range(len(s),0,-_CODEBITS)]
def _bytes_to_codes(b):a=memoryview(b).cast('I');assert a.itemsize==_sre.CODESIZE;assert len(a)*a.itemsize==len(b);return a.tolist()
def _simple(p):
 if len(p)!=1:return _C
 op,av=p[0]
 if op is SUBPATTERN:return av[0]is _A and _simple(av[-1])
 return op in _UNIT_CODES
def _generate_overlap_table(prefix):
 table=[0]*len(prefix)
 for i in range(1,len(prefix)):
  idx=table[i-1]
  while prefix[i]!=prefix[idx]:
   if idx==0:table[i]=0;break
   idx=table[idx-1]
  else:table[i]=idx+1
 return table
def _get_iscased(flags):
 if not flags&SRE_FLAG_IGNORECASE:return
 elif flags&SRE_FLAG_UNICODE:return _sre.unicode_iscased
 else:return _sre.ascii_iscased
def _get_literal_prefix(pattern,flags):
 prefix=[];prefixappend=prefix.append;prefix_skip=_A;iscased=_get_iscased(flags)
 for(op,av)in pattern.data:
  if op is LITERAL:
   if iscased and iscased(av):break
   prefixappend(av)
  elif op is SUBPATTERN:
   group,add_flags,del_flags,p=av;flags1=_combine_flags(flags,add_flags,del_flags)
   if flags1&SRE_FLAG_IGNORECASE and flags1&SRE_FLAG_LOCALE:break
   prefix1,prefix_skip1,got_all=_get_literal_prefix(p,flags1)
   if prefix_skip is _A:
    if group is not _A:prefix_skip=len(prefix)
    elif prefix_skip1 is not _A:prefix_skip=len(prefix)+prefix_skip1
   prefix.extend(prefix1)
   if not got_all:break
  else:break
 else:return prefix,prefix_skip,_B
 return prefix,prefix_skip,_C
def _get_charset_prefix(pattern,flags):
 while _B:
  if not pattern.data:return
  op,av=pattern.data[0]
  if op is not SUBPATTERN:break
  group,add_flags,del_flags,pattern=av;flags=_combine_flags(flags,add_flags,del_flags)
  if flags&SRE_FLAG_IGNORECASE and flags&SRE_FLAG_LOCALE:return
 iscased=_get_iscased(flags)
 if op is LITERAL:
  if iscased and iscased(av):return
  return[(op,av)]
 elif op is BRANCH:
  charset=[];charsetappend=charset.append
  for p in av[1]:
   if not p:return
   op,av=p[0]
   if op is LITERAL and not(iscased and iscased(av)):charsetappend((op,av))
   else:return
  return charset
 elif op is IN:
  charset=av
  if iscased:
   for(op,av)in charset:
    if op is LITERAL:
     if iscased(av):return
    elif op is RANGE:
     if av[1]>65535:return
     if any(map(iscased,range(av[0],av[1]+1))):return
  return charset
def _compile_info(code,pattern,flags):
 lo,hi=pattern.getwidth()
 if hi>MAXCODE:hi=MAXCODE
 if lo==0:code.extend([INFO,4,0,lo,hi]);return
 prefix=[];prefix_skip=0;charset=[]
 if not(flags&SRE_FLAG_IGNORECASE and flags&SRE_FLAG_LOCALE):
  prefix,prefix_skip,got_all=_get_literal_prefix(pattern,flags)
  if not prefix:charset=_get_charset_prefix(pattern,flags)
 emit=code.append;emit(INFO);skip=len(code);emit(0);mask=0
 if prefix:
  mask=SRE_INFO_PREFIX
  if prefix_skip is _A and got_all:mask=mask|SRE_INFO_LITERAL
 elif charset:mask=mask|SRE_INFO_CHARSET
 emit(mask)
 if lo<MAXCODE:emit(lo)
 else:emit(MAXCODE);prefix=prefix[:MAXCODE]
 emit(min(hi,MAXCODE))
 if prefix:
  emit(len(prefix))
  if prefix_skip is _A:prefix_skip=len(prefix)
  emit(prefix_skip);code.extend(prefix);code.extend(_generate_overlap_table(prefix))
 elif charset:charset,hascased=_optimize_charset(charset);assert not hascased;_compile_charset(charset,flags,code)
 code[skip]=len(code)-skip
def isstring(obj):return isinstance(obj,(str,bytes))
def _code(p,flags):flags=p.state.flags|flags;code=[];_compile_info(code,p,flags);_compile2(code,p.data,flags);code.append(SUCCESS);return code
def _hex_code(code):return'[%s]'%', '.join('%#0*x'%(_sre.CODESIZE*2+2,x)for x in code)
def dis(code):
 import sys;labels=set();level=0;offset_width=len(str(len(code)-1))
 def dis_(start,end):
  def print_(*args,to=_A):
   if to is not _A:labels.add(to);args+='(to %d)'%(to,),
   print('%*d%s '%(offset_width,start,':'if start in labels else'.'),end=_H*(level-1));print(*args)
  def print_2(*args):print(end=' '*(offset_width+2*level));print(*args)
  nonlocal level;level+=1;i=start
  while i<end:
   start=i;op=code[i];i+=1;op=OPCODES[op]
   if op in(SUCCESS,FAILURE,ANY,ANY_ALL,MAX_UNTIL,MIN_UNTIL,NEGATE):print_(op)
   elif op in(LITERAL,NOT_LITERAL,LITERAL_IGNORE,NOT_LITERAL_IGNORE,LITERAL_UNI_IGNORE,NOT_LITERAL_UNI_IGNORE,LITERAL_LOC_IGNORE,NOT_LITERAL_LOC_IGNORE):arg=code[i];i+=1;print_(op,'%#02x (%r)'%(arg,chr(arg)))
   elif op is AT:arg=code[i];i+=1;arg=str(ATCODES[arg]);assert arg[:3]=='AT_';print_(op,arg[3:])
   elif op is CATEGORY:arg=code[i];i+=1;arg=str(CHCODES[arg]);assert arg[:9]=='CATEGORY_';print_(op,arg[9:])
   elif op in(IN,IN_IGNORE,IN_UNI_IGNORE,IN_LOC_IGNORE):skip=code[i];print_(op,skip,to=i+skip);dis_(i+1,i+skip);i+=skip
   elif op in(RANGE,RANGE_UNI_IGNORE):lo,hi=code[i:i+2];i+=2;print_(op,'%#02x %#02x (%r-%r)'%(lo,hi,chr(lo),chr(hi)))
   elif op is CHARSET:print_(op,_hex_code(code[i:i+256//_CODEBITS]));i+=256//_CODEBITS
   elif op is BIGCHARSET:
    arg=code[i];i+=1;mapping=list(b''.join(x.to_bytes(_sre.CODESIZE,sys.byteorder)for x in code[i:i+256//_sre.CODESIZE]));print_(op,arg,mapping);i+=256//_sre.CODESIZE;level+=1
    for j in range(arg):print_2(_hex_code(code[i:i+256//_CODEBITS]));i+=256//_CODEBITS
    level-=1
   elif op in(MARK,GROUPREF,GROUPREF_IGNORE,GROUPREF_UNI_IGNORE,GROUPREF_LOC_IGNORE):arg=code[i];i+=1;print_(op,arg)
   elif op is JUMP:skip=code[i];print_(op,skip,to=i+skip);i+=1
   elif op is BRANCH:
    skip=code[i];print_(op,skip,to=i+skip)
    while skip:
     dis_(i+1,i+skip);i+=skip;start=i;skip=code[i]
     if skip:print_('branch',skip,to=i+skip)
     else:print_(FAILURE)
    i+=1
   elif op in(REPEAT,REPEAT_ONE,MIN_REPEAT_ONE,POSSESSIVE_REPEAT,POSSESSIVE_REPEAT_ONE):
    skip,min,max=code[i:i+3]
    if max==MAXREPEAT:max=_J
    print_(op,skip,min,max,to=i+skip);dis_(i+3,i+skip);i+=skip
   elif op is GROUPREF_EXISTS:arg,skip=code[i:i+2];print_(op,arg,skip,to=i+skip);i+=2
   elif op in(ASSERT,ASSERT_NOT):skip,arg=code[i:i+2];print_(op,skip,arg,to=i+skip);dis_(i+2,i+skip);i+=skip
   elif op is ATOMIC_GROUP:skip=code[i];print_(op,skip,to=i+skip);dis_(i+1,i+skip);i+=skip
   elif op is INFO:
    skip,flags,min,max=code[i:i+4]
    if max==MAXREPEAT:max=_J
    print_(op,skip,bin(flags),min,max,to=i+skip);start=i+4
    if flags&SRE_INFO_PREFIX:prefix_len,prefix_skip=code[i+4:i+6];print_2('  prefix_skip',prefix_skip);start=i+6;prefix=code[start:start+prefix_len];print_2('  prefix','[%s]'%', '.join('%#02x'%x for x in prefix),'(%r)'%''.join(map(chr,prefix)));start+=prefix_len;print_2('  overlap',code[start:start+prefix_len]);start+=prefix_len
    if flags&SRE_INFO_CHARSET:level+=1;print_2('in');dis_(start,i+skip);level-=1
    i+=skip
   else:raise ValueError(op)
  level-=1
 dis_(0,len(code))
def compile2(p,flags=0):
 if isstring(p):pattern=p;p=parse(p,flags)
 else:pattern=_A
 code=_code(p,flags)
 if flags&SRE_FLAG_DEBUG:print();dis(code)
 groupindex=p.state.groupdict;indexgroup=[_A]*p.state.groups
 for(k,i)in groupindex.items():indexgroup[i]=k
 return _sre.compile(pattern,flags|p.state.flags,code,p.state.groups-1,groupindex,tuple(indexgroup))
_cache={}
_MAXCACHE=512
@enum.global_enum
@enum._simple_enum(enum.IntFlag,boundary=enum.KEEP)
class RegexFlag:NOFLAG=0;ASCII=A=SRE_FLAG_ASCII;IGNORECASE=I=SRE_FLAG_IGNORECASE;LOCALE=L=SRE_FLAG_LOCALE;UNICODE=U=SRE_FLAG_UNICODE;MULTILINE=M=SRE_FLAG_MULTILINE;DOTALL=S=SRE_FLAG_DOTALL;VERBOSE=X=SRE_FLAG_VERBOSE;TEMPLATE=T=SRE_FLAG_TEMPLATE;DEBUG=SRE_FLAG_DEBUG;__str__=object.__str__;_numeric_repr_=hex
Pattern=type(compile2('',0))
def _compile(pattern,flags):
 if isinstance(flags,RegexFlag):flags=flags.value
 try:return _cache[type(pattern),pattern,flags]
 except KeyError:pass
 if isinstance(pattern,Pattern):
  if flags:raise ValueError('cannot process flags argument with a compiled pattern')
  return pattern
 if not isstring(pattern):raise TypeError('first argument must be string or compiled pattern')
 if flags&T:import warnings;warnings.warn("The re.TEMPLATE/re.T flag is deprecated as it is an undocumented flag without an obvious purpose. Don't use it.",DeprecationWarning)
 p=compile2(pattern,flags)
 if not flags&DEBUG:
  if len(_cache)>=_MAXCACHE:
   try:del _cache[next(iter(_cache))]
   except(StopIteration,RuntimeError,KeyError):pass
  _cache[type(pattern),pattern,flags]=p
 return p
def compile(pattern,flags=0):return _compile(pattern,flags)