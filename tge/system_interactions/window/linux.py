import subprocess

def is_window_minimized_linux(window_name):
    result = subprocess.run(['wmctrl', '-lG'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if window_name in line:
            parts = line.split()
            state = parts[8]
            return state == '0'  # 0 means the window is not minimized
    return False

def minimize_window_linux(window_name):
    result = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    window_id = None
    for line in lines:
        if window_name in line:
            window_id = line.split()[0]
            break

    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(['wmctrl', '-i', '-r', window_id, '-b', 'add,hidden'])

def get_window_position_linux(window_name):
    result = subprocess.run(['wmctrl', '-lG'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    for line in lines:
        if window_name in line:
            parts = line.split()
            x, y = int(parts[2]), int(parts[3])
            return x, y
    raise ValueError("Window not found")

def maximize_window_linux(window_name):
    result = subprocess.run(['wmctrl', '-l'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    window_id = None
    for line in lines:
        if window_name in line:
            window_id = line.split()[0]
            break

    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(['wmctrl', '-i', '-r', window_id, '-b', 'add,maximized_vert,maximized_horz'])

def set_window_position_linux(window_name, x, y, width, height):
    result = subprocess.run(['wmctrl', '-lG'], stdout=subprocess.PIPE, text=True)
    lines = result.stdout.splitlines()
    window_id = None
    for line in lines:
        if window_name in line:
            window_id = line.split()[0]
            break

    if window_id is None:
        raise ValueError("Window not found")

    subprocess.run(['wmctrl', '-i', '-r', window_id, '-e', f'0,{x},{y},{width},{height}'])