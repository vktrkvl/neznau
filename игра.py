import random

class Warrior:
    def __init__(self,health):
        self.health = health

    def hit(self,target,target1):
        if target.health > 0:
            target.health -= 20
            if target1 == warrior1:
                target1 = "Воин добра"
            if target1 == warrior2:
                target1 = "Воин зла"
            print(target1, " Атакован")
            print(target.health, " ХП осталось")
        if target.health == 0:
            print(target1, "проиграл,почему,а потому что легчайшая,для кого,для величайшего,VI KA")



warrior1 = Warrior(100)
warrior2 = Warrior(100)

q = int(input("Ударь(1),Сдайся(2)"))

while q != 2:
    if q == 1:
        j = random.randint(1,3)
        if j % 2 == 0:
            warrior1.hit(warrior2,warrior1)
            q = int(input("Ударь(1),Сдайся(2)"))
        else:
            warrior2.hit(warrior1,warrior2)
            q = int(input("Ударь(1),Сдайся(2)"))
    else:
        print("КоНеЦ")
        break
pass
