_C=False
_B=True
_A=None
import time,os
from typing import List,Union,Tuple,Any
from random import random,choice
import sys
from.tbe import determine_affirmative
__all__=['typingPrint']
if os.name=='nt':
	def clear():os.system('cls')
else:
	def clear():os.system('clear')
def typingPrint(text,delay):
	'\n    Prints the given text with a typing effect.\n\n    Args:\n        text: The string to print.\n\n    Returns:\n        None\n    ';A=delay
	if not A>0:A=.05
	for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
def typingInput(text,delay=0):
	'\n    Displays the given text character by character with a delay of 0.05 seconds,\n    then waits for the user to type a string and press Enter. Returns the entered string.\n\n    Parameters:\n    text (str): The text to be displayed before waiting for input.\n\n    Returns:\n    str: The string entered by the user.\n\n    Example:\n    >> typingInput("Please type your name: ")\n    Please type your name: Alice\n    \'Alice\'\n    ';A=delay
	if not A>0:A=.05
	for B in text:sys.stdout.write(B);sys.stdout.flush();time.sleep(A)
	C=input('');return C
def writeSentencesToConsole(punctuations,o_text,type_delay,line_delay):
	'\n    Writes text and splits it into sentences with punctuations and prints them\n\n    Args:\n    - punctuations: a list of valid sentence-ending punctuations\n    - o_text: the input text to split into sentences and print\n\n    Returns:\n    - A tuple containing a boolean indicating if the function succeeded and a message string\n    ';H=type_delay;G='Þ';E=line_delay;D=punctuations;A=o_text
	try:
		A=str(A)
		if type(D)!=list:D[D]
	except:return _C
	D=['.','!','?',':',';']
	for I in D:A=A.replace(I,I+G)
	F=A.split(G);B=0;C=0
	if not E>=0:E=.7
	typingPrint(A[C:len(F[B])+C],H);time.sleep(E);C+=len(F[B])+1;B+=1
	for K in range(A.count(G)-1):
		print(' ');time.sleep(E);J=A[C:len(F[B])+C][1:]
		if not J=='':typingPrint(J,H)
		C+=len(F[B])+1;B+=1
	return _B
def chooseFromTextMenu(text,prompt,ans_prompt):
	'\n    Displays a text menu and prompts the user to choose an option.\n\n    Args:\n        text (list): List of options to display in the menu.\n        prompt (str): Prompt to display before the menu.\n        ans_prompt (str): Prompt to display when asking for user input.\n\n    Returns:\n        int: The index of the chosen option in the \'text\' list.\n\n    Raises:\n        None.\n\n    Example:\n        text = [\'Option 1\', \'Option 2\', \'Option 3\']\n        prompt = "Please select an option:"\n        ans_prompt = "Enter the option number:"\n\n        index = chooseFromTextMenu(text, prompt, ans_prompt)\n        # User is prompted with the menu and enters an option number\n        # Returns the index of the chosen option\n    ';B=text;C=_B;print(prompt)
	while C:
		for D in range(len(B)):typingPrint(f"{D}: {B[D]}");print(' ');time.sleep(.05)
		time.sleep(.25);A=typingInput(ans_prompt)
		try:
			if A in B:return B.index(A)
			A=int(A);print('')
		except:print('')
		if type(A)==int:
			if A<=len(B)and A>=0:C=_C;return int(A)
def skip_line():'Prints a newline character to skip to the next line.';print('\n')
def print_table(data):
	'\n    Prints a table representation of the provided data.\n\n    Args:\n        data (list): A list of lists containing the data to be printed as a table.\n    \n    Returns:\n        tuple: A tuple containing a boolean value and a string message.\n            - The boolean value indicates the success or failure of the table printing.\n            - The string message provides additional information in case of failure.\n    \n    Raises:\n        None\n    \n    Example:\n        data = [[\'Name\', \'Age\', \'Country\'],\n                [\'John\', 25, \'USA\'],\n                [\'Emily\', 32, \'Canada\']]\n        success, message = print_table(data)\n        if success:\n            print("Table printed successfully!")\n        else:\n            print("Error:", message)\n    ';A='+'
	try:
		B=[max(len(str(A))for A in A)for A in zip(*data)];C=A+A.join('-'*(A+2)for A in B)+A;print(C)
		for D in data:E='| '+' | '.join(str(A).ljust(B)for(A,B)in zip(D,B))+' |';print(E)
		print(C);return _B,''
	except:return _C,'Unable to print table, make sure the data is a list of lists'
def progress_bar(progress_name,current,total,length,show_float=_B,empty_tile='-',full_tile='#'):
	'\n    Displays a progress bar indicating the completion of a task.\n\n    Parameters:\n    - progress_name (str): Name of the progress bar (optional).\n    - current (int): Current progress value.\n    - total (int): Total value representing the completion of the task.\n    - length: Length of the progress bar (number of tiles).\n    - show_float (bool): Determines whether to show the percentage as a float or an integer.\n    - empty_tile (str): Symbol representing empty tiles in the progress bar (default: \'-\').\n    - full_tile (str): Symbol representing filled tiles in the progress bar (default: \'#\').\n\n    Returns:\n    None\n\n    Example:\n    >>> progress_bar("Loading", 50, 100, 20, False,\'-\', \'#\')\n    Loading: [##########----------] 50%\n    ';E=length;D=progress_name;B=total;A=current
	if show_float:C=float(int(float(A/B*100)*10)/10)
	else:C=int(A/B*100)
	F=int(E*A//B);G=f"{full_tile}"*F+f"{empty_tile}"*(E-F)
	if D=='':sys.stdout.write(f"\r[{G}] {C}%");sys.stdout.flush()
	else:sys.stdout.write(f"\r{D}: [{G}] {C}%");sys.stdout.flush()
def colorize_text(text,color):
	"\n    Colorizes the input text using the specified color.\n\n    Args:\n        text (str): The text to be colorized.\n        color (str): The color to be applied to the text. It should be one of the following options:\n                    'black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white',\n                    'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue',\n                    'bright_magenta', 'bright_cyan', 'bright_white', 'bg_black', 'bg_red',\n                    'bg_green', 'bg_yellow', 'bg_blue', 'bg_magenta', 'bg_cyan', 'bg_white',\n                    'bg_bright_black', 'bg_bright_red', 'bg_bright_green', 'bg_bright_yellow',\n                    'bg_bright_blue', 'bg_bright_magenta', 'bg_bright_cyan', 'bg_bright_white',\n                    or 'reset'.\n\n    Returns:\n        str: The colorized text.\n\n    Raises:\n        ValueError: If an invalid color is specified.\n    ";C='reset';B=color;A={'black':'\x1b[30m','red':'\x1b[31m','green':'\x1b[32m','yellow':'\x1b[33m','blue':'\x1b[34m','magenta':'\x1b[35m','cyan':'\x1b[36m','white':'\x1b[37m','bright_black':'\x1b[90m','bright_red':'\x1b[91m','bright_green':'\x1b[92m','bright_yellow':'\x1b[93m','bright_blue':'\x1b[94m','bright_magenta':'\x1b[95m','bright_cyan':'\x1b[96m','bright_white':'\x1b[97m','bg_black':'\x1b[40m','bg_red':'\x1b[41m','bg_green':'\x1b[42m','bg_yellow':'\x1b[43m','bg_blue':'\x1b[44m','bg_magenta':'\x1b[45m','bg_cyan':'\x1b[46m','bg_white':'\x1b[47m','bg_bright_black':'\x1b[100m','bg_bright_red':'\x1b[101m','bg_bright_green':'\x1b[102m','bg_bright_yellow':'\x1b[103m','bg_bright_blue':'\x1b[104m','bg_bright_magenta':'\x1b[105m','bg_bright_cyan':'\x1b[106m','bg_bright_white':'\x1b[107m',C:'\x1b[0m'}
	if B not in A:raise ValueError('Invalid color specified.')
	return A[B]+text+A[C]
def visualize_directory(path,prefix='',lines=_A):
	'\n    Recursively visualizes the directory structure of a given path.\n\n    Args:\n        path (str): The path of the directory to visualize.\n        prefix (str, optional): The prefix for indentation in the visualization.\n                                Defaults to an empty string.\n        lines (list, optional): The list to store the visualization lines.\n                                Defaults to an empty list.\n\n    Returns:\n        None\n\n    Raises:\n        None\n\n    This function recursively traverses the directory structure starting from\n    the given path and prints the directory structure using ASCII characters.\n    Directories are represented in square brackets and files are indicated with\n    a forward slash ("/"). If a directory or file cannot be accessed due to\n    permission issues, "(Access Denied)" is displayed.\n\n    Example:\n        >>> visualize_directory(\'/path/to/directory\')\n        [directory]\n        ├── [subdirectory1]\n        │   ├── /file1.txt\n        │   └── [subsubdirectory]\n        └── [subdirectory2]\n            ├── /file2.txt\n            └── /file3.txt\n    ';H='├──';G='└──';B=prefix;A=lines
	if A is _A:A=[]
	if B=='':I=os.path.basename(path);A.append(f"[{I}]")
	C=_C
	try:
		with os.scandir(path)as D:
			D=list(D)
			for(J,E)in enumerate(D):
				C=J==len(D)-1;F=G if C else H
				if E.is_dir():A.append(f"{B}{F}[{E.name}]");K=B+'│   'if not C else B+'    ';visualize_directory(E.path,K,A)
				else:A.append(f"{B}{F}/{E.name}")
	except PermissionError:F=G if C else H;A.append(f"{B}{F}(Access Denied)")
	return A
def clear_lines(num_lines,move_front=_C):
	'\n    Clears a specified number of lines on the console screen.\n\n    Args:\n    num_lines (int): The number of lines to clear on the console screen.\n\n    Returns:\n    None: This function does not return anything.\n\n    Raises:\n    None\n\n    Description:\n    This function moves the cursor up num_lines lines on the console screen and clears the current line, effectively clearing a specified number of lines. It uses escape sequences to control the cursor and clear the line.\n\n    Example:\n    clear_lines(3)\n    This will move the cursor up 3 lines and clear the current line, effectively clearing 3 lines on the console screen.\n    ';A='\x1b[F';sys.stdout.write(A*num_lines);sys.stdout.write('\x1b[K')
	if move_front:sys.stdout.write(A)
def prompt_bool(question,allow_undeterminable=_C,tries=0,delete_lines=_B,return_value_when_tries_are_depleted=_A):
	C=tries;D=0
	while _B:
		D+=1;A=str(input(question)).lower();B=determine_affirmative(A)
		if B is not _A:return B,A
		elif allow_undeterminable:return B,A
		if C>0:
			if D>=C:return return_value_when_tries_are_depleted,A
		if delete_lines:clear_lines(1)
def prompt_number(question,min=_A,max=_A,incorrect=_A,error=_A,delete_lines=_B,tries=0,try_return=_A):
	'\n    Asks the user a number question and validates the input.\n\n    Args:\n        question (str): The question to ask the user.\n        min (int, optional): Minimum allowed value. Defaults to None.\n        max (int, optional): Maximum allowed value. Defaults to None.\n        incorrect (callable, optional): Callback function to handle incorrect input. Defaults to None.\n        error (callable, optional): Callback function to handle errors during input conversion. Defaults to None.\n        delete_lines (bool, optional): Whether to delete previous lines. Defaults to True.\n        tries (int, optional): Maximum number of tries. Defaults to 0.\n        try_return (callable, optional): Callback function to handle reaching maximum tries. Defaults to None.\n\n    Returns:\n        int: The validated input number or None if maximum tries reached.\n\n    Raises:\n        ValueError: If the input cannot be converted to an integer.\n\n    ';G=delete_lines;F=error;E=incorrect;C=try_return;B=tries;D=0
	while _B:
		D+=1
		try:
			A=int(input(question))
			if min is _A or max is _A:return A
			elif min<=A<=max:return A
			else:
				if B>0:
					if D>=B:
						if C is not _A:return C(A)
						else:return
				if G:clear_lines(1)
				if E is not _A:return E(A)
		except:
			if B>0:
				if D>=B:
					if C is not _A:return C(A)
					else:return
			if G:clear_lines(1)
			if F is not _A:return F(A)
def matrix_rain(rows,columns,speed=.1,density=.2,duration=_A,symbols=['0','1']):
	"\n    Displays a matrix rain animation on the console.\n\n    Args:\n        rows (int): The number of rows in the matrix.\n        columns (int): The number of columns in the matrix.\n        speed (float, optional): The speed at which the raindrops fall. Default is 0.1.\n        density (float, optional): The density of raindrops in the matrix. Default is 0.2.\n        duration (float, optional): The duration (in seconds) for which the matrix rain should be displayed. If not provided, it runs indefinitely.\n\n    Returns:\n        None\n\n    Raises:\n        None\n\n    Note:\n        - The raindrops are represented by '0' and '1' characters.\n        - The console is cleared before each frame is printed.\n    ";E=duration;D=columns;C=rows;global tge_matrix_console_stop;tge_matrix_console_stop=_C;H=time.time();A=[[' 'for A in range(D)]for A in range(C)]
	while _B:
		for B in range(D):
			if random()<density:A[0][B]=choice(symbols)
			else:A[0][B]=' '
		for B in range(C-1,0,-1):
			for F in range(D):A[B][F]=A[B-1][F]
		G='';I=0
		for J in A[1:]:G+=''.join(J)+'\n';I+=1
		clear_lines(C+1);print(G)
		if E is not _A:
			if time.time()-H>E:break
		elif tge_matrix_console_stop:break
		time.sleep(speed)
from io import StringIO
class ConsoleCapture:
	def __init__(A):"\n        A context manager for capturing and redirecting standard output.\n\n        This class provides functionality to capture and redirect the standard output\n        during its context, allowing you to capture printed output into a string buffer.\n\n        Usage:\n        ------\n        To use this context manager, create an instance of OutputCapture within a `with` block.\n        During the block's execution, any printed output will be captured into a buffer.\n        ";A.original_stdout=sys.stdout;A.captured_output=StringIO();A.capturing=_C
	def start_capture(A):
		'\n        Start capturing the standard output if capturing is not already active.\n\n        This method is used to redirect the standard output (stdout) to the captured output stream\n        associated with this object. The captured output can be useful for logging or saving the\n        output of specific code segments.\n\n        If capturing is already active, calling this method will have no effect.\n        '
		if A.capturing==_C:sys.stdout=A.captured_output
	def stop_capture(A):
		"\n        Stops capturing the standard output and restores the original stdout if capturing is currently active.\n\n        This method checks the state of the 'capturing' attribute in the instance and, if it is currently set to True,\n        it restores the original stdout stream, effectively stopping the redirection of output that was previously\n        enabled by the 'start_capture' method.\n\n        Parameters:\n            self (object): The instance of the capturing class.\n        "
		if A.capturing==_B:sys.stdout=A.original_stdout
	def get_captured_output(A):'\n        Retrieve the content from the captured output buffer.\n\n        This method returns the content stored in the internal captured output buffer,\n        which is typically used to capture and store the output produced by various\n        operations or functions. The buffer is first rewound to the beginning to ensure\n        reading starts from the start of the content.\n\n        Returns:\n            str: The content stored in the captured output buffer.\n        ';A.captured_output.seek(0);return A.captured_output.read()
def suppress_print():"\n    Temporarily suppresses the standard output (print statements) by capturing\n    and redirecting them. This function initializes a global 'console_capture'\n    object of type 'ConsoleCapture' and starts capturing the console output.\n    \n    Usage:\n    suppress_print()\n    # ... code block where print statements should be suppressed ...\n    release_print()  # To release the suppressed print statements\n    ";global console_capture;console_capture=ConsoleCapture();console_capture.start_capture()
def enable_print():"\n    Reverses the effect of a previously enabled console output capture,\n    allowing the standard output to be displayed in the console again.\n\n    This function stops the capture of console output that was previously\n    initiated through the 'console_capture' global object. It retrieves the\n    captured output and returns it as a string.\n\n    Returns:\n        str: The captured console output accumulated since capture started.\n    ";global console_capture;console_capture.stop_capture();A=console_capture.get_captured_output();return A