class TextFileReader:
    def __init__(self, file_path, encoding='utf-8'):
        print("TextFileReader initialized")
        self.file_path = file_path
        self.encoding = encoding

    def __enter__(self):
        print("Entering context: opening text file")
        self.file_obj = open(self.file_path, 'r', encoding=self.encoding)
        return self.file_obj
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context: closing text file")
        self.file_obj.close()