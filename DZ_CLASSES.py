# класс животных
class Animal:
    def __init__(self, class_name='животина', voice='голос', name='Без имени', weight=10):
        self.class_name = class_name
        self.name = name
        self.voice = voice
        self.health = 100
        self.weight = weight

    def feed(self, value):
        self.health += value
        return f'{self.name} - покормлен(а) и здоровья теперь - {self.health}%'

    def weight_show(self):
        return self.weight

    def voice_listen(self):
        return self.voice

    def action(self):
        return 'погладить =)'



class Birds(Animal):
    def action(self):
        return 'собирать яйца'



class Hooves(Animal):
    def action(self):
        return 'доить'



class Sheeps(Animal):
    def action(self):
        return 'стричь'



#                   ПТИЦЫ
# гуси
guce_grey = Birds('гусь', 'кря-кря', 'Серый', 15)
guce_white = Birds('гусь', 'кря-кря', 'Белый', 17)

# куры
chicken = Birds('курица', 'ко-ко-ко', 'Ко-ко', 3)
rooster = Birds('курица', 'ко-ко-ку-ка-ре-ку-я-ж-петух!', 'Кукареку', 5)

# утка
duck = Birds('утка', 'кря-кря', 'Кряква',)



#                   КОПЫТНЫЕ
# корова
cow = Hooves('корова', 'Му-му', 'Манька', 150)

# овцы
sheep_barash = Sheeps('овца', 'бе-бе', 'Барашек', 63)
sheep_curly = Sheeps('овца', 'бе-бе', 'Кудрявый', 45)

# козы
goat_horns = Hooves('коза', 'блеееееэээ', 'Рога', 35)
goat_hooves = Hooves('коза', 'блеееееэээ', 'Копыта', 28)

# списки животных и их имен
enimals_list = [guce_grey, guce_white, chicken, rooster, duck, cow, sheep_curly, sheep_barash, goat_horns, goat_hooves]
enimals_names_list = [enimal.name for enimal in enimals_list]


# вычисляем самое тяжелое животное
max_weight = 0
max_weight_class = ''
max_weight_name = ''


for enimal in enimals_list:
    # вес взял с помощью метода .weight_show()
    if enimal.weight_show() > max_weight:
        max_weight = enimal.weight_show()
        max_weight_class = enimal.class_name
        max_weight_name = enimal.name



# вывод информации:
print('Задача №1:')
print('Животное: ' + goat_hooves.class_name,\
      '\nИмя: ' + goat_hooves.name,\
      '\nГолос: ' + goat_hooves.voice_listen(),\
      '\nВес:', goat_hooves.weight_show())



print('\n\nЗадача №2:')
print(chicken.feed(10))
print('Животное ' + sheep_barash.class_name +\
      ' по имени ' + sheep_barash.name +\
      ' можно ' + sheep_barash.action())



print('\n\nЗадача №3:')
print('Самое тяжелое животное ' + max_weight_class,\
      'по имени ' + max_weight_name, 'весит:', max_weight, 'кг')