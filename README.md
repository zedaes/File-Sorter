# FileSorter

FileSorter is a Python script that organizes files and folders within a specified directory. It categorizes files based on their type and moves them into appropriate subdirectories. It also handles folders by placing them into a dedicated "Folders" directory.

## Features

- **Categorizes Files**: Sorts files into directories based on type, including documents, images, videos, audio, archives, spreadsheets, presentations, executables, code, and others.
- **Handles Folders**: Moves folders into a "Folders" directory.
- **Concurrent Processing**: Uses multi-threading to handle files and folders efficiently.

## Installation

This script uses only Python’s standard library, so no additional packages are required. Ensure you have Python 3.6 or later installed on your system.

## Usage

1. **Clone the Repository**:
   ```
   git clone https://github.com/zedaes/File-Sorter.git
   cd FileSorter
   ```

2. Edit the Script:
    Update the `folder` variable in `sorter.py` to point to the directory you want to sort. For example, if you want to sort your Downloads folder:

    ```
    downloadsFolder = os.path.expanduser('~/Downloads')
    ```

3. Run the Script:
    ```
    python sorter.py
    ```

4. Check the Results:
    After running the script, your files and folders will be organized into their respective categories.

## Configuration
You can customize the file categories and types by modifying the getFileTypes method in sorter.py. The current categories include:

- Documents
- Images
- Videos
- Audio
- Archives
- Spreadsheets
- Presentations
- Executable
- Code
- Folders
- Others

### Example
Given the following files in your directory:

- `example.jpg`
- `document.pdf`
- `movie.mp4`
- `script.py`
- `my_folder`

After running the script, you will find:

- Documents folder containing `document.pdf`
- Images folder containing `example.jpg`
- Videos folder containing `movie.mp4`
- Code folder containing `script.py`
- Folders folder containing `my_folder`