class IceCreamStand:
    def __init__(self,name):
        self.name = name
    def describe_restaurant(self):
        long_name = f'{self.name}'
        return long_name.title()
    def IceCreamStand(self):
        print(f"{self.describe_restaurant()}")

flavors1 = IceCreamStand('клубничное')
flavors2 = IceCreamStand('шоколадное')
flavors3 = IceCreamStand('ванильное')
print(flavors1.describe_restaurant())
print(flavors2.describe_restaurant())
print(flavors3.describe_restaurant())