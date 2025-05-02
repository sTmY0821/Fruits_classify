from sympy import false


class EpidemicModel:
    def __init__(self, area: str="", current_people: int=0, increase_people: int=0):
        self.area = area
        self.current_people = current_people
        self.increase_people = increase_people

    def __str__(self):
        # return f"地区：{self.area} 现有人数：{self.current_people} 新增人数：{self.increase_people}"
        return "%s地区目前疫情现有人数%s人，新增%s人" % (self.area, self.current_people, self.increase_people)

    def __eq__(self, other):
        return self.area == other.area



if __name__ == '__main__':
    epidemic_model = EpidemicModel("上海", 100, 10)
    print(epidemic_model)
    epidemic_model2 = EpidemicModel("上海", 100, 10)
    print(epidemic_model == epidemic_model2)