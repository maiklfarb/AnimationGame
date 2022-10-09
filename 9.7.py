class Admin:
    def __init__(self,name):
        self.name = name
    def describe_restaurant(self):
        long_name = f'{self.name}'
        return long_name.title()

    def show_priveleges(self):
        print(f"{self.describe_restaurant()}")
priveleges1 = Admin('разрешено добавлять сообщения')
priveleges2 = Admin('разрешено банить пользователей')
priveleges3 = Admin('разрешено удалять пользователей')
print(priveleges1.describe_restaurant())
print(priveleges2.describe_restaurant())
print(priveleges3.describe_restaurant())