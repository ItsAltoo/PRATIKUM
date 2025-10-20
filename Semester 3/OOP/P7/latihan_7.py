import os
from datetime import datetime

class FileAnalyzer:
    
    def __init__(self,file_path):
        if os.path.exists(file_path):
            self.__file_path = file_path
            self.__file_size = os.path.getsize(file_path)
            self.__file_ada = True
        else:
            print(f"-> ERROR: File tidak ditemukan di path '{file_path}'.")
            self.__file_ada = False
            self.__file_path = None
            self.__file_size = 0
            
    def get_file_size(self, unit="bytes"):
        if not self.__file_ada:
            return "File tidak tersedia."
        
        if unit == "bytes":
            return f"{self.__file_size} bytes"
        elif unit == "KB":
            return f"{self.__file_size / 1024} KB"
        elif unit == "MB":
            return f"{self.__file_size / (1024 * 1024)} MB"
        else:
            return "Unit tidak dikenali. Gunakan 'bytes', 'KB', atau 'MB'."
        
    def get_modification_time(self):
        if not self.__file_ada:
            return "File tidak tersedia."
        
        mod_time = os.path.getmtime(self.__file_path)
        return f"Waktu modifikasi terakhir: {datetime.fromtimestamp(mod_time)}"
    
    def analyze(self):
        if self.__file_ada:
            print(f"File Path: {self.__file_path}")
            print(f"File Exists: {self.__file_ada}")
            print(f"File Size: {self.get_file_size("KB")}")
            print(f"Last Modified: {self.get_modification_time()}")
    
    
analyzer = FileAnalyzer("dokumen.txt")
analyzer.analyze()