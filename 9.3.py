class User:
    def __init__(self,name):
        self.name = name

    def describe_restaurant(self):
        long_name = f'{self.name}'
        return long_name.title()

    def open_restaurant(self):
        print(f"{self.describe_restaurant()}")

        print("Приветствуем в ресторан Победа!")
name = "Введите ваше имя: "
print(name.describe_restaurant())
name.open_restaurant()

