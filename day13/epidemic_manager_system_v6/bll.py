from dtl import EpidemicModel


class EpidemicController:

    def __init__(self):
        self.epidemic_list = [] #type:list[EpidemicModel]

    def add_epidemic(self, model):
        self.epidemic_list.append(model)

    def delete_epidemic(self, area_name) -> bool:
        try:
            model = EpidemicModel(area_name)
            self.epidemic_list.remove(model)
            return True
        except:
            return False

    def modify_epidemic(self, area_name, model: EpidemicModel) -> bool:
        for i in range(len(self.epidemic_list)):
            if self.epidemic_list[i].area == area_name:
                self.epidemic_list[i] = model
                # self.epidemic_list[i].__dict__= model.__dict__
            return True
        return False