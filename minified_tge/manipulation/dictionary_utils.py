#type: ignore
def remove_duplicates_from_dictionary(dictionary):
 B=dictionary;C=set(B.values());D={}
 for(E,A)in B.items():
  if A in C:D[E]=A;C.remove(A)
 return D
def get_from_dict_by_list(data_dict,keys):
 A=data_dict
 for B in keys:A=A[B]
 return A
def set_in_dict_by_list(data_dict,keys,value):
 A=data_dict
 for B in keys[:-1]:A=A.setdefault(B,{})
 A[keys[-1]]=value
__all__=['remove_duplicates_from_dictionary','get_from_dict_by_list','set_in_dict_by_list']