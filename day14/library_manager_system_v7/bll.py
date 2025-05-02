from day14.library_manager_system_v7.dtl import LibraryModel


class LibraryController:
    def __init__(self):
        self.library_list = []

    def add_book(self, model: LibraryModel):
        self.library_list.append(model)

    def delete_book(self, name: str) -> bool:
        try:
            model = LibraryModel(name=name)
            self.library_list.remove(model)
            return True
        except:
            return False
    def modify_book(self, name: str, model: LibraryModel) -> bool:
        for i in range(len(self.library_list)):
            if self.library_list[i].name == name:
                self.library_list[i] = model
                return True
            return False

