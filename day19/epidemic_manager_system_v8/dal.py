from dtl import EpidemicModel
class EpidemicDao:
    def __init__(self):
        self.file_name = "epidemic01.txt"

    def load(self):
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return eval(file.read())
        except FileNotFoundError:
            return []

    def save(self,data):
        with open(self.file_name, "w", encoding="utf-8") as file:
            file.write(data.__repr__())

