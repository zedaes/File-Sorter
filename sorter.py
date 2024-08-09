import os
import shutil
from concurrent.futures import ThreadPoolExecutor
from typing import List, Dict

class FileSorter:
    def __init__(self, folderPath: str):
        self.folderPath = folderPath
        self.fileTypes = self.getFileTypes()
        self.executor = ThreadPoolExecutor(max_workers=4)

    def getFileTypes(self) -> Dict[str, List[str]]:
        return {
            'Documents': [
                '.pdf', '.doc', '.docx', '.odt', '.rtf', '.tex', '.txt', '.wpd', '.wps'
            ],
            'Images': [
                '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.ico', '.svg', '.webp'
            ],
            'Videos': [
                '.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm', '.mpg', '.mpeg'
            ],
            'Audio': [
                '.mp3', '.wav', '.aac', '.ogg', '.flac', '.m4a', '.wma', '.aiff'
            ],
            'Archives': [
                '.zip', '.tar', '.gz', '.rar', '.7z', '.bz2', '.xz'
            ],
            'Spreadsheets': [
                '.xls', '.xlsx', '.ods', '.csv'
            ],
            'Presentations': [
                '.ppt', '.pptx', '.odp'
            ],
            'Executable': [
                '.exe', '.bin', '.app', '.sh', '.bat'
            ],
            'Code': [
                '.py', '.java', '.c', '.cpp', '.js', '.html', '.css', '.rb', '.php', '.pl'
            ],
            'Folders': [],
            'Others': []
        }

    def sortFile(self, filePath: str, destFolder: str):
        try:
            if not os.path.exists(destFolder):
                os.makedirs(destFolder)
            shutil.move(filePath, os.path.join(destFolder, os.path.basename(filePath)))
        except Exception as e:
            print(f"Error moving file {filePath}: {e}")

    def sortFolder(self, folderPath: str, destFolder: str):
        try:
            if not os.path.exists(destFolder):
                os.makedirs(destFolder)
            shutil.move(folderPath, os.path.join(destFolder, os.path.basename(folderPath)))
        except Exception as e:
            print(f"Error moving folder {folderPath}: {e}")

    def getFileDestination(self, fileName: str) -> str:
        _, ext = os.path.splitext(fileName)
        for folder, extensions in self.fileTypes.items():
            if ext in extensions:
                return os.path.join(self.folderPath, folder)
        return os.path.join(self.folderPath, 'Others')

    def sortFiles(self):
        for itemName in os.listdir(self.folderPath):
            itemPath = os.path.join(self.folderPath, itemName)
            if os.path.isfile(itemPath):
                destFolder = self.getFileDestination(itemName)
                self.executor.submit(self.sortFile, itemPath, destFolder)
            elif os.path.isdir(itemPath):
                destFolder = os.path.join(self.folderPath, 'Folders')
                self.executor.submit(self.sortFolder, itemPath, destFolder)

    def close(self):
        self.executor.shutdown(wait=True)

if __name__ == "__main__":
    folder = os.path.expanduser('~/Downloads')
    sorter = FileSorter(folder)
    sorter.sortFiles()
    sorter.close()
    print("Sorting complete.")
