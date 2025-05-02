from day19.library_manager_system_v8.dtl import LibraryModel
class LibraryDao:
    def __init__(self):
        self.file_name = "book.txt"

    def save(self,data):
        with open(self.file_name,"w",encoding="utf-8") as file:
            file.write(data.__repr__())

    def load(self):
        try:
            with open(self.file_name,"r",encoding="utf-8") as file:
                return eval(file.read())
        except:
            return []
