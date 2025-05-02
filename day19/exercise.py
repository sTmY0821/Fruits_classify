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

    def __repr__(self):
        return 'EpidemicModel("%s", %s, %s)'% (self.area, self.current_people, self.increase_people)

e1= [EpidemicModel("上海", 100, 10),
     EpidemicModel("北京", 300, 20),
     EpidemicModel("广东", 400, 30)]
with open("epidemic.txt", "w", encoding="utf-8") as file:
    file.write(e1.__repr__())
with open("epidemic.txt", "r", encoding="utf-8") as file:
    m1 = eval(file.read())
    for item in m1:
        print(item)