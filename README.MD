# Text Game Engine (TGE)

Originally designed for console-based games, TGE has evolved into a versatile general-purpose library. Since 2021, it has expanded significantly, now offering over 600 functions for various applications, including file manipulation, UI handling, audio playback, and more.

## Installation Instructions

1. Download the `.py` downloader from the [releases](#).
2. Execute the downloader.
3. Enjoy (or don't) TGE.

## Comparison: TGE vs. Minified TGE

| Feature           | Normal     | Minified  |
| ----------------- | ---------- | --------- |
| **Import Time**   | ~200-350ms | ~60-250ms |
| **Size**          | ~550kb     | ~350kb    |
| **Docstrings**    | 100%       | Removed   |
| **Type Notation** | ~95%       | Removed   |

## Downloader Options

The downloader supports additional inputs to customize the installation without user intervention:

### `-suppression_level` (Default: 0)

- **0**: Logs all messages
- **1**: Logs warnings and errors only
- **2**: Logs errors only
- **3**: Completely silent

### `-path` (Default: Asks user)

- The directory to a file <sup><sub>(python.exe)</sub></sup> or folder used by `-install_option`.

### `-install_option` (Default: Asks user)

- **1**: Install TGE for all installed Python installations in the default Python directory (`{C:\Users\{Username}\AppData\Local\Programs\Python}`).
- **2**: Select a `.exe` file in the Python folder.
- **3**: Select a folder to install TGE into.
- **4**: Same as 3 -> Internally when asking the user, 3 allows them to select the folder in a visual window while 4 requests the file to be provided in the console.

### `-install_minified` (Flag)

- If set, install the minified version of TGE

### `-clingy` (Flag)

- If set and `-suppression_level` is below 3, the script will wait for user input before closing.

### `-skip_dependencies` (Flag)

- If set, skips checking for and downloading dependencies.

### `-skip_checking_local` (Flag)

If set, skips checking the status of the locally installed TGE if it is installed

### `-inherit_empty_directory` (Flag)

- If set, tge will copy its files directly into the given directory instead of _creating a new_/_replacing an old_ tge folder (Only applicable when -install_option is 3 or 4)