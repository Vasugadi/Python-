class warrior:
    battle="avengers"
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def attack_warrior(self):
        print(f"{self.name} has {self.health} health left")

    def attack_mage(self):
        print(f"{self.name} has {self.health} health left")
        
thor = warrior("thor", 100, 50)
hulk = warrior("hulk", 200, 100)

thor.attack_warrior()
hulk.attack_mage()
print(thor.name)
print(warrior.battle)
print(thor.battle)
hulk.battle="marvel"
print(hulk.battle)