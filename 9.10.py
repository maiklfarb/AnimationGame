from Restaurant import Restaurant
class Restaurant():
    def __init__(self,name):
        self.name = name
    def describe_restaurant(self):
        long_name = f'{self.name}'
        return long_name.title()
    def open_restaurant(self):
        print(f"{self.describe_restaurant()} открыты!")

rest = Restaurant("Победа")
rest1 = Restaurant("Грузинский")
rest2 = Restaurant("Радость")
print(rest.describe_restaurant())
print(rest1.describe_restaurant())
print(rest2.describe_restaurant())
