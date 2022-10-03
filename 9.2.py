class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        long_name = f'{self.name} {self.type}'
        return long_name.title()
    def open_restaurant(self):
        print(f"{self.describe_restaurant()} открыт!")

rest = Restaurant("победа")
print(rest.describe_restaurant())
rest.open_restaurant()
print('--------------------------')
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        long_name = f'{self.name} {self.type}'
        return long_name.title()
    def open_restaurant(self):
        print(f"{self.describe_restaurant()} открыт!")

rest = Restaurant("радость")
print(rest.describe_restaurant())
rest.open_restaurant()
print('--------------------------')
class Restaurant:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def describe_restaurant(self):
        long_name = f'{self.name} {self.type}'
        return long_name.title()
    def open_restaurant(self):
        print(f"{self.describe_restaurant()} открыт!")

rest = Restaurant("грузинский")
print(rest.describe_restaurant())
rest.open_restaurant()