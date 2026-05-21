warrior_name = "thor"
warrior_health = 100
warrior_attack = 50

mage_name = "hulk"
mage_health = 200
mage_attack = 100

def attack_warrior(attack, health):
    print(f"Warrior attacks with {attack} damage")
def attack_mage(attack, health):
    print(f"Mage attacks with {attack} damage")

attack_warrior(warrior_attack, warrior_health)
attack_mage(mage_attack, mage_health)
