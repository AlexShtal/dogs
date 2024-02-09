from random import randint, sample


class Dog:
    """Создание собаки"""
    global dogs

    def __init__(self, name, age):
        """Инициализация атрибутов"""
        moods = ['Good', 'Bad']
        self.name = name
        self.age = age
        self.mood = moods[randint(0, 1)]

    def mood_set(self, mood):
        """Смена настроения"""
        self.mood = mood

    def mood_get(self):
        return self.mood

    def age_get(self):
        return self.age

    def name_get(self):
        return self.name

    def talk(self, partner):
        """Собачка разговаривает с другой собачкой"""

        if self.mood == 'Good' and partner.mood == 'Good':
            pass
        if partner.mood == 'Bad' and self.mood == 'Bad' and randint(1, 100) > 45:
            self.mood = 'Good'
            partner.mood = 'Good'
        if partner.mood == 'Bad' or self.mood == 'Bad' and randint(1, 100) > 55:
            self.mood = 'Bad'
            partner.mood = 'Bad'

    @staticmethod
    def rand_dog():
        return dogs[randint(0, len(dogs) - 1)]

    @staticmethod
    def dogs_mood_print():
        """Выводит информацию о настроении всех собачек"""
        cnt_good = 0
        cnt_bad = 0

        for i in dogs:
            if i.mood_get() == 'Good':
                cnt_good += 1
            else:
                cnt_bad += 1
        print(
            'Количество веселых собачек: {0} ({1}%)'.format(
                cnt_good, round((cnt_good * 100) / (cnt_good + cnt_bad), 2)
            ) + '\n' +
            'Количество грустных собачек: {0} ({1}%)'.format(cnt_bad, round((cnt_bad * 100) / (cnt_good + cnt_bad), 2))
        )

    @staticmethod
    def dogs_mood():
        """Возвращает информацию о настроении всех собачек"""
        cnt_good = 0
        cnt_bad = 0

        for i in dogs:
            if i.mood_get() == 'Good':
                cnt_good += 1
            else:
                cnt_bad += 1
        return {
            'Good': cnt_good,
            'Bad': cnt_bad
        }


"""Создаем собачек"""
with open('names.txt', 'r') as f:
    names = [str(i)[:-1] for i in f]

with open('breeds.txt', 'r', encoding='utf-8') as f:
    breeds = [str(i)[:-1] for i in f]

dogs = [Dog(name, randint(1, 20)) for name in sample(names, len(names))]

dogs = tuple(dogs)

"""Код для теста"""
