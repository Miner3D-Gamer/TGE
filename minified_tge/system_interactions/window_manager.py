#type: ignore
from..import SYSTEM_NAME
__all__=['is_window_minimized','minimize_window','maximize_window','get_window_position','set_window_position','get_window_by_title']
if SYSTEM_NAME=='windows':from.window.windows import is_window_minimized,minimize_window,maximize_window,get_window_position,set_window_position,get_window_by_title
elif SYSTEM_NAME=='linux':from.window.linux import is_window_minimized,minimize_window,maximize_window,get_window_position,set_window_position,get_window_by_title
elif SYSTEM_NAME=='darwin':from.window.mac import is_window_minimized,minimize_window,maximize_window,get_window_position,set_window_position,get_window_by_title
else:__all__=[]