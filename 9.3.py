class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def describe_restaurant(self):
        long_name = f'{self.name} {self.age}'
        return long_name.title()
    def open_restaurant(self):
        print(f"{self.describe_restaurant()}")

        print("Приветствуем в ресторан Победа!")
name = "Введите ваше имя: "
print(name.describe_restaurant())
name.open_restaurant()

