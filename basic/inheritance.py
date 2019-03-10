class Chef:
    def make_chicken(self):
        print("The chef makes a chicken.")
    def make_salad(self):
        print("The chef makes a salad.")
    def make_special_dish(self):
        print("The chef makes a steak.")

my_chef = Chef()
my_chef.make_special_dish()


class ChineseChef(Chef):
    def make_special_dish(self):
        print("The chef makes an orange chicken.")
    def make_fried_rice(self):
        print("The chef makes fried rice")

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()