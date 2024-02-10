from __future__ import annotations
from random import randint, sample


class Dog:
    dogs = []

    def __init__(self, name: str, age: int):
        """Initializing"""
        moods = ['Good', 'Bad']
        self.name = name
        self.age = age
        self.mood = moods[randint(0, 1)]

    def setMood(self, mood: str):
        """Setter for mood"""
        self.mood = mood

    def getMood(self) -> str:
        """Getter for mood"""
        return self.mood

    def getAge(self) -> int:
        """Getter for age"""
        return self.age

    def getName(self) -> str:
        """Getter for name"""
        return self.name

    def isGood(self) -> bool:
        return self.getMood() == "Good"

    def talk(self, partner: Dog):
        """Dogs interaction"""

        if self.isGood() and partner.isGood():
            pass
        if not partner.isGood() and not self.isGood() and randint(1, 100) > 45:
            self.setMood('Good')
            partner.setMood('Good')
        if not partner.isGood() or not self.isGood() and randint(1, 100) > 55:
            self.setMood('Bad')
            partner.setMood('Bad')


    @staticmethod
    def getRandomDog() -> list:
        """Getter for random dog"""
        return dogs[randint(0, len(dogs) - 1)]

    @staticmethod
    def printDogsMood():
        """Printing gogs moods info"""
        count_good = 0
        count_bad = 0

        for i in dogs:
            if i.getMood() == 'Good':
                count_good += 1
            else:
                count_bad += 1
        print(
            'Amount of happy dogs: {0} ({1}%)'.format(
                count_good, round((count_good * 100) / (count_good + count_bad), 2)
            ) + '\n' +
            'Amount of sad dogs: {0} ({1}%)'.format(count_bad, round((count_bad * 100) / (count_good + count_bad), 2))
        )

    @staticmethod
    def getDogsMood() -> dict:
        """Getter for dogs mood"""
        count_good = 0
        count_bad = 0

        for i in dogs:
            if i.getMood() == 'Good':
                count_good += 1
            else:
                count_bad += 1
        return {
            'Good': count_good,
            'Bad': count_bad
        }


"""Loading dogs names and ages"""
with open('names.txt', 'r') as names_file:
    names = [str(i)[:-1] for i in names_file]

with open('breeds.txt', 'r', encoding='utf-8') as breeds_file:
    breeds = [str(i)[:-1] for i in breeds_file]

"""Creating tuple with random dogs"""
Dog.dogs = [Dog(name, randint(1, 20)) for name in sample(names, len(names))]
Dog.dogs = tuple(Dog.dogs)

"""Testing code"""
