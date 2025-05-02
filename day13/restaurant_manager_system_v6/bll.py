from usl import RestaurantModel


class RestaurantController:
    def __init__(self):
        self.restaurant_list = []

    def add_restaurant(self,model)->None:
        self.restaurant_list.append(model)

    def remove_restaurant(self,name)->bool:
        for i in range(len(self.restaurant_list)):
            if self.restaurant_list[i] == RestaurantModel(name):
                del self.restaurant_list[i]
                return True
        return False

    def modify_restaurant(self,name,model:RestaurantModel)->bool:
        for i in range(len(self.restaurant_list)):
            if self.restaurant_list[i] == RestaurantModel(name):
                self.restaurant_list[i] = model
                return True
        return False