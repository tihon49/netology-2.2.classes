# общий класс животных
class Animal:
    total_weight = 0
    max_weight = 0
    max_weight_name = ''

    def __init__(self, name='Без имени', weight=1):
        self.name = name
        self.weight = weight
        Animal.total_weight += self.weight

        if self.weight > Animal.max_weight:
            Animal.max_weight = self.weight
            Animal.max_weight_name = self.name

    def feed(self):
        return f'{self.name} - покормлен(а)'

    def action(self):
        return 'погладить =)'


###################################################
### ОПРЕДЕЛЕНИЕ КЛАССОВ НАСЛЕДОВАННЫХ ОТ ANIMAL ###
class Chicken(Animal):
    class_name = 'курица'

    def get_voice(self):
        return 'ko-ko'

    def action(self):
        return 'собирать яйца'



class Duck(Animal):
    class_name = 'утка'

    def get_voice(self):
        return 'кря-кря'

    def action(self):
        return 'собирать яйца'



class Guse(Animal):
    class_name = 'гусь'

    def get_voice(self):
        return 'кря-кря'

    def action(self):
        return 'собирать яйца'



class Cow(Animal):
    class_name = 'корова'

    def get_voice(self):
        return 'му-му'

    def action(self):
        return 'доить'



class Sheep(Animal):
    class_name = 'овца'

    def get_voice(self):
        return 'бе-бе'

    def action(self):
        return 'стричь'



class Goat(Animal):
    class_name = 'коза'

    def get_voice(self):
        return 'бле-бле'

    def action(self):
        return 'доить'

###################################################

# гуси
guce_grey = Guse('Серый', 7)
guce_white = Guse('Белый', 5)

# куры
chicken_koko = Chicken('Ко-ко', 3)
rooster = Chicken('Кукареку', 4)

# утка
duck = Duck('Кряква', 5)

# корова
cow = Cow('Манька', 150)

# овцы
sheep_barash = Sheep('Барашек', 45)
sheep_curly = Sheep('Кудрявый', 60)

# козы
goat_horns = Goat('Рога', 30)
goat_hooves = Goat('Копыта', 34)

###################################################

# Задача №1
print('Задача №1')
print('Животное:', duck.class_name, ' Имя:', duck.name + \
      '\nГолос:', duck.get_voice(), ' вес:', duck.weight, 'кг')


# Задача №2
print('\nЗадача №2')
print(goat_horns.feed())
print('Животное', sheep_curly.class_name, 'по имени', sheep_curly.name, \
      'можно', sheep_curly.action())


#Задача №3
print('\nЗадача №3')
print('Самое тяжелое животное зовут', Animal.max_weight_name, 'весит:', Animal.max_weight, 'кг')
print('Общий вес всех животных:', Animal.total_weight, 'кг')