#type: ignore
from..import SYSTEM_NAME
if SYSTEM_NAME=='windows':from.other.windows import create_virtual_drive,add_to_path_to_system_path_variables
elif SYSTEM_NAME=='linux':from.other.linux import create_virtual_drive,add_to_path_to_system_path_variables
elif SYSTEM_NAME=='darwin':from.other.mac import create_virtual_drive,add_to_path_to_system_path_variables
else:...
__all__=['create_virtual_drive','add_to_path_to_system_path_variables']