from Modules_Name import My_Class
from my_Modules_Surname import My_Surname
from my_Modules_Age import My_Age

import colorama  # İmport Colors
colorama.init()

class My_modules():
    def __init__(self):
        self.startProject()

    def name(self):
        resultName = My_Class().name()
        return resultName.capitalize()
    def surname(self):
        resultSurname = My_Surname().surname()
        return resultSurname.upper()

    def age(self):
        age = My_Age().age()
        return age
    

    def startProject(self):
        message = f"Hello By {colorama.Fore.GREEN+self.name()} {colorama.Fore.GREEN+self.surname()} {colorama.Fore.WHITE} your age calculation: {colorama.Fore.RED+str(self.age())}"
        print(message)

My_modules()