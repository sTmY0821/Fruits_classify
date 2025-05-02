from day19.library_manager_system_v8.dal import LibraryDao
from day19.library_manager_system_v8.dtl import LibraryModel


class LibraryController:
    def __init__(self):
        self.library_dao = LibraryDao()
        self.library_list = self.library_dao.load()
    def add_book(self, model: LibraryModel):
        self.library_list.append(model)
        self.library_dao.save(self.library_list)

    def delete_book(self, name: str) -> bool:
        try:
            self.library_list.remove(LibraryModel(name))
            self.library_dao.save(self.library_list)
            return True
        except ValueError:
            return False

    def modify_book(self,name,model):
        for i in range(len(self.library_list)):
            if self.library_list[i].name == name:
                self.library_list[i] = model
                self.library_dao.save(self.library_list)
                return True
        return False
