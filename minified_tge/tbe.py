_E='function_name'
_D='type'
_C=None
_B=True
_A=False
from collections.abc import Iterable
from typing import List,Union,Tuple,Any,get_type_hints
import types,ast,os,sys,importlib
from difflib import get_close_matches
import inspect
def pass_func(*args):0
def execute_function(func=pass_func,*args,**kwargs):return func(*args,**kwargs)
def determine_affirmative(text):
	B="i can't go along with that";A='not really';text=text.strip().lower();positives=['y','yes','yeah','yup','uh-huh','sure','affirmative','absolutely','indeed','certainly','of course','definitely','you bet','roger','right on','no doubt','by all means','most certainly','positively','without a doubt','naturally','indubitably','sure thing','yuppers','aye','ok','okey-dokey','all right','righto','very well','exactly','precisely','no problem','for sure','most assuredly','you got it',"that's right",'sure as shooting','all righty','of course, my dear',"couldn't agree more",'a thousand times, yes',"i'm in","it's a go","i'll go along with that",'count me in',"i'm on board",'without hesitation','undoubtedly','yeye'];negatives=['n','no','nope','nah','nuh-uh','negative','not at all','absolutely not','certainly not','no way','never','i disagree',"i'm afraid not","i can't agree with that",'i beg to differ',"i'm not convinced",A,"i'm not so sure",'i have my doubts',"that's not correct","that's incorrect","i don't think so","i'm not on board with that","i'm not buying it",B,"i can't support that","i'm opposed to that","i'm against it","i'm not in favor of that","that's a negative",'no chance','not a chance','no siree',"i can't see that happening","i'm not inclined to agree","i can't accept that","i'm not on the same page","i'm not feeling it",'i have reservations',"i can't endorse that","that's out of the question","i can't support that notion","i'm skeptical","that doesn't work for me","i don't agree with that assessment","i'm not persuaded","i'm not buying into that","i don't subscribe to that view",B,"i'm not swayed by that argument","i don't believe so","i'm not on board","i can't back that up","i'm not convinced of its validity","that's not my understanding","i'm not sold on that idea","i can't vouch for that","i don't really feel like it",A]
	if text in positives:return _B
	if text in negatives:return _A
	closest_positive_match=get_close_matches(text,positives,n=1,cutoff=.8);closest_negative_match=get_close_matches(text,negatives,n=1,cutoff=.8)
	if closest_positive_match:return _B
	if closest_negative_match:return _A
def categorize_responses(text_list):
	response_list=[]
	for text in text_list:response_list.append(determine_affirmative(text))
	return response_list
def get_available_variables():
	g_variables={};l_variables={};global_vars=globals()
	for(var_name,var_value)in global_vars.items():g_variables[var_name]=var_value
	local_vars=locals()
	for(var_name,var_value)in local_vars.items():l_variables[var_name]=var_value
	return g_variables,l_variables
def get_docstring(obj):
	try:return inspect.getdoc(obj)
	except:return''
def convert_number_to_words_less_than_thousand(n,dash=_B):
	TINY_NUMBERS=['zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'];SMALL_NUMBERS=['','','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
	if n>=100:
		hundreds_digit=n//100;rest=n%100;result=TINY_NUMBERS[hundreds_digit]+' hundred'
		if rest>0:result+=' and '+convert_number_to_words_less_than_thousand(rest)
		return result
	elif n>=20:
		tens_digit=n//10;rest=n%10;result=SMALL_NUMBERS[tens_digit]
		if rest>0:
			if dash:result+='-'+TINY_NUMBERS[rest]
			else:result+=' '+TINY_NUMBERS[rest]
		return result
	else:return TINY_NUMBERS[n]
def number_to_words(number):
	C='cennovemseptuagintillion';B='censexagintillion';A='trevigintillion';big_numbers=['','thousand','million','billion','trillion','quadrillion','quintillion','sextillion','septillion','octillion','nonillion','decillion','undecillion','duodecillion','tredecillion','quattuordecillion','quindecillion','sexdecillion','septendecillion','octodecillion','novemdecillion','vigintillion','unvigintillion','duovigintillion',A,'quattuorvigintillion','quinvigintillion','sexvigintillion','septenvigintillion','octovigintillion','novemvigintillion','trigintillion','untrigintillion','duotrigintillion',A,'quattuortrigintillion','quintrigintillion','sextrigintillion','septentrigintillion','octotrigintillion','novemtrigintillion','quadragintillion','unquadragintillion','duoquadragintillion','trequadragintillion','quattuorquadragintillion','quinquadragintillion','sexquadragintillion','septenquadragintillion','octoquadragintillion','novemquadragintillion','quinquagintillion','unquinquagintillion','duoquinquagintillion','trequinquagintillion','quattuorquinquagintillion','quinquinquagintillion','sexquinquagintillion','septenquinquagintillion','octaquinquagintillion','novemquinquagintillion','sexagintillion','unsexagintillion','duosexagintillion','tresexagintillion','quattuorsexagintillion','quinsexagintillion','sexsexagintillion','septensexagintillion','octasexagintillion','novemsexagintillion','septuagintillion','unseptuagintillion','duoseptuagintillion','treseptuagintillion','quattuorseptuagintillion','quinseptuagintillion','sexseptuagintillion','septenseptuagintillion','octaseptuagintillion','novemseptuagintillion','octagintillion','unoctogintillion','duooctogintillion','treoctogintillion','quattuoroctogintillion','quinoctogintillion','sexoctogintillion','septenoctogintillion','octaoctogintillion','novemoctogintillion','nonagintillion','unnonagintillion','duononagintillion','trenonagintillion','quattuornonagintillion','quinnonagintillion','sexnonagintillion','septennonagintillion','octanonagintillion','novemnonagintillion','centillion','cenuntillion','centretillion','cenquattuortillion','cenquintillion','censextillion','censeptentillion','cenoctotillion','cennovemtillion','cendecillion','centredecillion','cenquattuordecillion','cenquindecillion','censexdecillion','censeptendecillion','cenoctodecillion','cennovemdecillion','cenvigintillion','cenunvigintillion','cendovigintillion','centrevigintillion','cenquattuorvigintillion','cenquinvigintillion','censexvigintillion','censeptenvigintillion','cenoctovigintillion','cennovemvigintillion','centrigintillion','cenuntrigintillion','cendotrigintillion','centretrigintillion','cenquattuortrigintillion','cenquintrigintillion','censextrigintillion','censeptentrigintillion','cenoctotrigintillion','cennovemtrigintillion','cenquadragintillion','cenunquadragintillion','cendoquadragintillion','centrequadragintillion','cenquattuorquadragintillion','cenquinquadragintillion','censexquadragintillion','censeptenquadragintillion','cenoctoquadragintillion','cennovemquadragintillion','cenquinquagintillion','cenunquinquagintillion','cendoquinquagintillion','centrequinquagintillion','cenquattuorquinquagintillion','cenquinquinquagintillion','censexquinquagintillion','censeptenquinquagintillion','cenoctoquinquagintillion','cennovemquinquagintillion',B,'cenunsexagintillion','cendosexagintillion','centresexagintillion','cenquattuorsexagintillion','cenquinsexagintillion','cenquinsexagintilliard',B,'censexsexagintilliard','censeptensexagintillion','censeptensexagintilliard','cenoctosexagintillion','cenoctosexagintilliard','cennovemsexagintillion','cennovemsexagintilliard','censeptuagintillion','censeptuagintilliard','cenunseptuagintillion','cenunseptuagintilliard','cendoseptuagintillion','cendoseptuagintilliard','centreseptuagintillion','centreseptuagintilliard','cenquattuorseptuagintillion','cenquattuorseptuagintilliard','cenquinseptuagintillion','cenquinseptuagintilliard','censexseptuagintillion','censexseptuagintilliard','censeptenseptuagintillion','censeptenseptuagintilliard','cenoctoseptuagintillion','cenoctoseptuagintilliard',C,C,'cennovemseptuagintilliard','cenoctogintillion','cenoctogintilliard','cenunoctogintillion','cenunoctogintilliard','cendooctogintillion','cendooctogintilliard','centreoctogintillion']
	if number==0:return'zero'
	elif number<0:return'minus '+number_to_words(abs(number))
	groups=[]
	while number>0:groups.append(number%1000);number//=1000
	result_parts=[]
	for(i,group)in enumerate(groups):
		if group!=0:result_parts.append(convert_number_to_words_less_than_thousand(group)+' '+big_numbers[i])
	return', '.join(reversed(result_parts))
def find_undocumented_functions(file_path):
	undocumented_functions=[]
	with open(file_path,'r',encoding='utf8')as file:tree=ast.parse(file.read())
	for node in ast.walk(tree):
		if isinstance(node,ast.FunctionDef):
			if not ast.get_docstring(node):undocumented_functions.append([node.name,node.end_lineno])
	return undocumented_functions
def check_directory_for_undocumented_functions(directory_path):
	undocumented_functions_dict={}
	for filename in os.listdir(directory_path):
		if filename.endswith('.py'):
			file_path=os.path.join(directory_path,filename);undocumented_functions=find_undocumented_functions(file_path)
			if undocumented_functions:undocumented_functions_dict[filename]=undocumented_functions
	return undocumented_functions_dict
def check_directory_and_sub_directory_for_undocumented_functions(directory_path):
	undocumented_functions_dict={}
	def _check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(current_path):
		for item in os.listdir(current_path):
			item_path=os.path.join(current_path,item)
			if os.path.isdir(item_path):_check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(item_path)
			elif item.endswith('.py'):
				undocumented_functions=find_undocumented_functions(item_path)
				if undocumented_functions:filename=os.path.relpath(item_path,directory_path);undocumented_functions_dict[filename]=undocumented_functions
	_check_directory_and_sub_directory_for_undocumented_functions_traverse_directory(directory_path);return undocumented_functions_dict
def autocomplete(prefix,word_list):return[word for word in word_list if word.startswith(prefix)]
def strict_autocomplete(prefix,word_list):
	words=autocomplete(prefix=prefix,word_list=word_list)
	if len(words)==1:return words[0]
	if prefix in words:return prefix
	return words
def is_iterable(thing):return hasattr(thing,'__iter__')
def split_with_list(string,separators,limit=_C):
	for separator in separators:string=string.replace(separator,'𘚟')
	return string.split('𘚟')
def analyze_text(text):
	A='min_commas_per_sentence';text=text.replace('...','…').replace('\n','').strip();legacy_sentences=split_with_list(text,['. ','! ','? ']);sentences=[];word_amounts=[];comma_amounts=[]
	for i in range(len(legacy_sentences)):
		commas=legacy_sentences[i].count(',');words=legacy_sentences[i].split(' ');deleted=0
		for j in range(len(words)):
			words[j]=words[j].replace(',','')
			if words[j].strip()=='':words.pop(j);deleted+=1
			if len(words)<=j+deleted:break
		if not len(words)==0:word_amounts.append(len(words))
		sentences.append(words);comma_amounts.append(commas)
	total_word_count=0
	for word_amount in word_amounts:total_word_count+=word_amount
	total_comma_count=0
	for comma_amount in comma_amounts:total_comma_count+=comma_amount
	return{'sentence_amount':len(sentences),'total_word_count':total_word_count,'average_word_count_per_sentence':total_word_count/len(word_amounts),'max_words_per_sentence':max(word_amounts),'min_words_per_sentence':min(word_amounts),'total_comma_count':total_comma_count,'average_commas_count_per_sentence':total_comma_count/len(comma_amounts),A:max(comma_amounts),A:min(comma_amounts),'word_amount_list':word_amounts,'comma_amount_list':comma_amounts}
import uuid,hashlib
def generate_uuid_from_directory(directory,blacklisted_extensions=[]):
	hash_md5=hashlib.md5()
	for(root,_,files)in os.walk(directory):
		for file in sorted(files):
			blacklisted=_B
			for ext in blacklisted_extensions:
				if file.endswith(ext):break
			else:blacklisted=_A
			if blacklisted:continue
			file_path=os.path.join(root,file)
			if os.path.isfile(file_path):
				with open(file_path,'rb')as f:
					for chunk in iter(lambda:f.read(4096),b''):hash_md5.update(chunk)
	unique_hash=hash_md5.hexdigest();unique_uuid=uuid.UUID(unique_hash[:32]);return unique_uuid
def check_for_functions_in_module_with_missing_notations(library_module):
	functions_with_missing_annotations=[]
	for(name,obj)in inspect.getmembers(library_module):
		if isinstance(obj,types.FunctionType):
			input_parameters=get_function_inputs(obj);missing_input_types=[param for param in input_parameters if param[_D]is NoInputType];return_type=get_return_type(obj)
			if missing_input_types or return_type is MissingReturnType:functions_with_missing_annotations.append({_E:name,'missing_input_types':missing_input_types,'return_type':return_type})
	return functions_with_missing_annotations
def print_check_for_functions_in_module_with_missing_notations(library_module):
	data=check_for_functions_in_module_with_missing_notations(library_module)
	for i in data:print(f"Function '{i[_E]}' of type {'Missing Return'if i[_E]is MissingReturnType else'Missing Input type'}")
def get_function_id_by_name(func_name):
	if func_name in globals():
		func_obj=globals()[func_name]
		if callable(func_obj):return func_obj
class NoInputType:0
def get_function_inputs(func):
	B='default';A='name';signature=inspect.signature(func);type_hints=get_type_hints(func);input_parameters=[]
	for(param_name,param)in signature.parameters.items():
		param_type=type_hints.get(param_name,_C)
		if param.default is not inspect.Parameter.empty:default_value=param.default;input_parameters.append({A:param_name,_D:param_type,B:default_value})
		else:input_parameters.append({A:param_name,_D:param_type,B:NoInputType})
	return input_parameters
class MissingReturnType:0
def get_return_type(func):
	signature=inspect.signature(func);return_type=signature.return_annotation
	if return_type==inspect.Signature.empty:return MissingReturnType
	else:return return_type
def count_functions_in_module(module,library_name):
	function_count=0
	for(name,obj)in inspect.getmembers(module):
		if inspect.isfunction(obj):function_count+=1
		elif inspect.ismodule(obj)and obj.__package__.startswith(library_name):function_count+=count_functions_in_module(obj,library_name)
	return function_count
def count_functions_in_library(library_name):
	try:module=importlib.import_module(library_name)
	except ModuleNotFoundError:return-1
	function_count=count_functions_in_module(module,library_name);return function_count
class ArgumentHandler:
	def __init__(self,arguments=_C):
		if arguments is _C:arguments=sys.argv[1:]
		self.arguments=arguments;self.argument_list_length=len(arguments)
	def get_argument(self,argument,delete=_A,default=_C):
		value_id=self.get_id(argument)
		if value_id<0:return default
		if delete:value=self.arguments.pop(value_id);self.argument_list_length-=1
		else:value=self.arguments.__getitem__(value_id)
		return value
	def get_argument_by_flag(self,flag,delete=_A,default=_C):
		value_id=self.get_id(flag)
		if value_id<0:return default
		if value_id+1==len(self.arguments):return default
		if delete:self.arguments.pop(value_id);value=self.arguments.pop(value_id);self.argument_list_length-=2
		else:value=self.arguments.__getitem__(value_id+1)
		return value
	def get_id(self,item):
		if not item in self.arguments:return-1
		value_id=self.arguments.index(item);return value_id
	def is_empty(self):return self.argument_list_length==0
def print_undocumented_functions_in_directory(directory=os.path.dirname(__file__)):
	undocumented=check_directory_and_sub_directory_for_undocumented_functions(directory);amount=0
	for i in undocumented:
		print('\n'+i)
		for j in undocumented[i]:amount+=1;print(f'\t{j[0]} (File "{directory}\\{i}", line {j[1]})')
	print('\nA total of %s functions are undocumented'%amount)
def get_from_dict_by_list(data_dict,keys):
	for key in keys:data_dict=data_dict[key]
	return data_dict
def set_in_dict_by_list(data_dict,keys,value):
	for key in keys[:-1]:data_dict=data_dict.setdefault(key,{})
	data_dict[keys[-1]]=value
from collections import defaultdict
class TrieNode:
	def __init__(self):self.children=defaultdict(TrieNode);self.is_end_of_path=_A
def insert_path(root,path):
	node=root
	for part in path:node=node.children[part]
	node.is_end_of_path=_B
def build_trie(paths):
	root=TrieNode()
	for path in paths:insert_path(root,path.split('/'))
	return root
def serialize_trie(node):
	if not node.children:return[]
	if len(node.children)==1 and node.is_end_of_path==_A:
		key,child=next(iter(node.children.items()));serialized_child=serialize_trie(child)
		if isinstance(serialized_child,list)and not serialized_child:return key
		if isinstance(serialized_child,str):return f"{key}/{serialized_child}"
		return{key:serialized_child}
	result={}
	for(key,child)in node.children.items():
		serialized_child=serialize_trie(child)
		if isinstance(serialized_child,list)and not serialized_child:result.setdefault('files',[]).append(key)
		else:result[key]=serialized_child
	return result
def compress_directory_list(paths):trie=build_trie(paths);compressed=serialize_trie(trie);return compressed
def decompress_directory_list(compressed):
	paths=[]
	def dfs(node,current_path=''):
		if isinstance(node,list):paths.append(f"{current_path}/{node[0]}".strip('/'));return
		if isinstance(node,str):paths.append(node);return
		for(key,value)in node.items():
			if key=='files':
				for file_path in value:paths.append(f"{current_path}/{file_path}".strip('/'))
			else:dfs(value,f"{current_path}/{key}".strip('/'))
	dfs(compressed);return paths
import python_minifier
def minify(text,rename_important_names=_A,remove_docstrings=_B):return python_minifier.minify(text,rename_globals=rename_important_names,remove_literal_statements=remove_docstrings)