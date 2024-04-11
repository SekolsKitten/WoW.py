class Character:  
    def __init__(self, name, race, level = 1):       
        self.name = name
        self.race = race 
        self.level= level

def show_info(self):
    print(f"Name: {self.name}\nRace: {self.race}\nLevel: {self.level}")          


class Warrior(Character):
    def __init__(self, name, race, weapon):
        super().__init__(name, race) 
        self.weapon = weapon



class Mage(Character):
    def __init__(self, name, race, magic_type):
        super().__init__(name, race)                     
        self.magic_type= magic_type



class Character:
    def __init__(self, name, race, level=1):
        self.name = name
        self.race = race 
        self.__level = level #private attribute 


        def level_up(self):
            self.__level += 1 


class Character:
    def special(self):
        print("This characters has no special abilites")


class Warrior(Character):
    def special(self):
        print(f"{self.name} swings their {self.weapon} mightily!")


class Mage(Character):
    def special_abilty(self):
        print(f"{self.name} casts a powerful{self.magic_type} spell!")
              


grommash = Warrior("Grommash", "Orc" "Axe")
jaina + Mage("Jiana", "Human", "Frost")  

grommash.show_info()
grommash.special._ability()     

jaina.show_info()
jaina.special_ability()
jaina.level_up() #Level up Jaina
jaina.show_info()