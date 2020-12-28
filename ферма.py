import random


class Farm(object):


    def __init__(self, name): # Метод конструктор
        self.name = name
        self.hunger = random.randint(0, 16)
        self.boredom = random.randint(0, 16)

    def __str__(self): # Метод вывода на экран
        rep = 'Name: ' + self.name + '\n' + 'Hunger: ' + str(self.hunger) + '\n' + 'Boredom: ' + str(self.boredom)
        return rep

    def __pass_time(self): # Течение времени
        self. + = 1
        self.boredom += 1

    @property
    def mood(self): # Свойство состояния
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Счастливая"
        elif 5 < = unhappiness <= 10:
            m = "Хорошо"
        elif 11 < = unhappiness < = 15:
            m = "Разочарованная"
        else:
            m = "Плохая"
        return m

    def talk(self): # Разговор
        print("Я", self.name, "чувствую себя", self.mood, "сейчас")
        self.__pass_time()

    @staticmethod
    def number(number=None, c=0, m=0):  # Метод для ввода и проверки 
        while c == 0:  # ошибки численных значений кормежки и игры
            number = input('Сколько? От 0 до бесконечности... ')
            try:
                m = int(number)
                c = 1
            except:
                print('Попробуй еще раз.')

        if int(number) < 0:
            number = 0
        else:
            number = m
        return number

    def eat(self, food):  # Кормежка
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun):  # Игра
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():  # Основная функция
    print('Привет, ты на ферме! У тебя есть лошадка, корова и курица, придумай им имена.')
    crit_name = input("Как зовут Лошадку: ")
    horse = Farm(crit_name)
    crit_name = input("Как зовут Корову: ")
    cow = Farm(crit_name)
    crit_name = input("Как зовут Курицу: ")
    chicken = Farm(crit_name)

    choice = None
    numb = None
    while choice != "0":
        print \
            ("""
        Владелец фермы
        0 - Выход
        1 - Что говорят зверушки
        2 - Покорми зверушек
        3 - Поиграй
        """)

        choice = input("Выбор: ")
        print()

        # exit
        if choice == "0":
            print("До свидания.")

        # listen to your livestock
        elif choice == "1":
            horse.talk()
            print('игого.\n')
            cow.talk()
            print('муууу.\n')
            chicken.talk()
            print('ко ко ко.\n')

        # feed your livestock
        elif choice == "2":
            numb = Farm.number()
            horse.eat(numb)
            print("Игого. Спасибо.")
            cow.eat(numb)
            print("Мууу. Спасибо.")
            chicken.eat(numb)
            print("Ко ко. Спасибо.")

        # play with your livestock
        elif choice == "3":
            numb = Farm.number()
            horse.play(numb)
            cow.play(numb)
            chicken.play(numb)
            print("Ура! Ура! Ура!")

        # secret
        elif choice = = "4":
            print(horse)
            print(cow)
            print(chicken)
        # some unknown choice
        else:
            print("\nПрости, но", choice, "это не правильный выбор.")


main()
("\n\nНажми enter для выхода.")
