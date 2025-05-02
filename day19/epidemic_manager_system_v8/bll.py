from dal import EpidemicDao
from dtl import EpidemicModel


class EpidemicController:
    def __init__(self):
        self.read = EpidemicDao()
        self.epidemic_list = self.read.load()

    def add_epidemic(self, model: EpidemicModel):
        self.epidemic_list.append(model)
        self.read.save(self.epidemic_list)

    def delete_epidemic(self, area: str) -> bool:
        try:
            self.epidemic_list.remove(EpidemicModel(area))
            return True
        except ValueError:
            return False

    def modify_epidemic(self, area: str, model: EpidemicModel):
        for i in range(len(self.epidemic_list)):
            if self.epidemic_list[i] == EpidemicModel(area):
                self.epidemic_list[i] = model
                self.read.save(self.epidemic_list)
                return True
        return False
