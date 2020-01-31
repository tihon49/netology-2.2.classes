# класс животных
class Animal:
    def __init__(self, class_name='животина', voice='голос', name='Без имени', use='действие', weight=10):
        self.class_name = class_name
        self.name = name
        self.use = use
        self.voice = voice
        self.health = 100
        self.weight = weight

    def feed(self, value):
        self.health += value
        return f'{self.name} - покормлен(а) и здоровья теперь - {self.health}%'

    def action(self):
        return self.use



#                   ПТИЦЫ
# гуси
guce_grey = Animal('гусь', 'кря-кря', 'Серый', 'собирать яйца', 15)
guce_white = Animal('гусь', 'кря-кря', 'Белый', 'собирать яйца', 17)

# куры
chicken = Animal('курица', 'ко-ко-ко', 'Ко-ко', 'собирать яйца', 3)
rooster = Animal('курица', 'ко-ко-ку-ка-ре-ку-я-ж-петух!', 'Кукареку', 'собирать яйца', 5)

# утка
duck = Animal('утка', 'кря-кря', 'Кряква', 'собирать яйца')



#                   КОПЫТНЫЕ
# корова
cow = Animal('корова', 'Му-му', 'Манька', 'доить', 150)

# овцы
sheep_barash = Animal('овца', 'бе-бе', 'Барашек', 'стричь', 63)
sheep_curly = Animal('овца', 'бе-бе', 'Кудрявый', 'стричь', 45)

# козы
goat_horns = Animal('коза', 'блеееееэээ', 'Рога', 'доить', 35)
goat_hooves = Animal('коза', 'блеееееэээ', 'Копыта', 'доить', 28)

# списки животных и их имен
enimals_list = [guce_grey, guce_white, chicken, rooster, duck, cow, sheep_curly, sheep_barash, goat_horns, goat_hooves]
enimals_names_list = [enimal.name for enimal in enimals_list]

# вычисляем самое тяжелое животное
max_weight = 0
max_weight_class = ''
max_weight_name = ''

for enimal in enimals_list:
    if enimal.weight > max_weight:
        max_weight = enimal.weight
        max_weight_class = enimal.class_name
        max_weight_name = enimal.name



# получаем имя животного от юзера
def question():
    question = input ('''
\nКого хотите помотреть? (напишите имя)
Ваш выбор: ''')

    return question.capitalize()



# вывод информации на основании данных из функции question()
def show_time(question):
    for enimal in enimals_list:
        if question in enimals_names_list:
            if question == enimal.name:
                print (f'''
###################################################################
Привет, я {enimal.class_name}, и меня зовут {enimal.name}
со здоровьем всё в порядке, оно составляет - {enimal.health}%
мой вес в данный момент = {enimal.weight}кг
спросите какая от меня польза? ну как минимум можно {enimal.action()}
голос мой звучит так: {enimal.voice}
одну минуточку, хочу немного перекусить......
спустя 30 минут... {enimal.feed(10)} !!!
:)


для информации:
общий вес всех животных = {sum(i.weight for i in enimals_list)}кг
самое тяжелое животное - {max_weight_class} {max_weight_name} и весит {max_weight}кг
###################################################################''')

        elif question not in enimals_names_list:
            return False # print('К сожалению, такого имени нет.')



# запускаем шарманку!!!
if __name__ == '__main__':
    print('''
достсупные варианты:
гусь "Серый"
гусь "Белый"
курица "Ко-Ко"
курица (но это не точно) "Кукареку"
утка "Кряква"
корова "Манька"
овЕц "Барашек"
овЕц "Кудрявый"
коза (еще какая) "Рога"
коза (не лучше предыдущей) "Копыта"

[!] ДЛЯ ВЫХОДА НАЖМИТЕ 'q' ''') 

    while True:
        show_time(question())
