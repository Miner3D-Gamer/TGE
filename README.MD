# Text Game Engine (TGE)

Originally designed for console-based games, TGE has evolved into a versatile general-purpose library. Since 2021, it has expanded significantly, now offering over 800 functions for various applications, including file manipulation, UI handling, audio playback, and more.

## Installation Instructions

1. Download the `.py` downloader from the [releases](#).
2. Execute the downloader.
3. Enjoy (or don't) TGE.

## Comparison: TGE vs. Minified TGE

| Feature           | Normal      | Minified    |
|-------------------|-------------|-------------|
| **Import Time**   | ~500ms      | ~150ms      |
| **Size**          | ~500kb      | ~300kb      |
| **Docstrings**    | ~80%        | Removed     |
| **Type Notation** | ~90%        | Removed     |

## Downloader Options

The downloader supports additional inputs to customize the installation without user intervention:

### `-suppression_level` (Default: 0)

- **0**: Logs all messages
- **1**: Logs warnings and errors only
- **2**: Logs errors only
- **3**: Completely silent

### `-path` (No Default)

- **{str}**: The directory to a file or folder, based on `-install_option`.

### `-install_option` (Default: Asks user)

- **1**: Install TGE for all installed Python installations in the default Python directory (`{C:\Users\{Username}\AppData\Local\Programs\Python}`).
- **2**: Select a `.exe` file in the Python folder or use the path provided by `-path`.
- **3**: Select a folder to install TGE into or use the path provided by `-path`.

### `-install_minified` (Default: N)

- `y`, `1`, `sure`: Installs the minified version of TGE.
- `n`, `2`, `nope`: Installs the normal version of TGE.

### `-clingy`

- If set and `-suppression_level` is below 3, the script will wait for user input before closing.

### `-skip_dependencies`

- If set, skips checking for and downloading dependencies.