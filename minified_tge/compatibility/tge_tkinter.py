from tkinter import messagebox
def show_message(message_level,user_feedback_level=0,title=None,message=None,**F):
	B=message_level;A=user_feedback_level;C=['info','warning','error','question'];D=['ok','okcancel','yesno','yesnocancel','retrycancel','abortretryignore']
	if B<0 or B>len(C):B=0
	if A<0 or A>len(D):A=0
	E=messagebox._show(title,message,C[B],D[A],**F)
	if A==2:
		if E=='yes':return True
		else:return False
	else:return E
if __name__=='__main__':print(show_message(message_level=2,user_feedback_level=0,title='Error!',message='An Error occurred.'))