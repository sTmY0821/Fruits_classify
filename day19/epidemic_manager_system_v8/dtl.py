class EpidemicModel:
    def __init__(self, area: str = "", current_people: int = 0, increase_people: int = 0):
        self.area = area
        self.current_people = current_people
        self.increase_people = increase_people

    def __str__(self):
        return "地区：%s，现有确诊人数：%d，新增确诊人数：%d" % (self.area, self.current_people, self.increase_people)

    def __eq__(self, other):
        return self.area == other.area

    def __repr__(self):
        return 'EpidemicModel("%s", %s, %s)' % (self.area, self.current_people, self.increase_people)
