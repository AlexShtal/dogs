from random import randint, sample


class Dog:
    def __init__(self, name: str, breed: str, age: int):
        """Initializing"""
        moods = ['Good', 'Bad']
        self.name = name
        self.breed = breed
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


class DogsGroup:
    def __init__(self, amount: int, names: list, breeds: list):
        self.dogs_list = []

        sampled_names = [names[randint(0, len(names) - 1)] for _ in range(amount)]
        sampled_breeds = [breeds[randint(0, len(breeds) - 1)] for _ in range(amount)]

        for i in range(amount):
            self.dogs_list.append(Dog(sampled_names[i], sampled_breeds[i], randint(1, 20)))

    def getList(self) -> list:
        return self.dogs_list

    def talks(self, number_of_dogs: int):
        """Dogs interaction"""

        for _ in range(number_of_dogs):
            first_dog = self[randint(0, len(self.getList()) - 1)]
            second_dog = self[randint(0, len(self.getList()) - 1)]

            if first_dog.isGood() and second_dog.isGood():
                pass
            if not second_dog.isGood() and not first_dog.isGood() and randint(1, 100) > 45:
                first_dog.setMood('Good')
                second_dog.setMood('Good')
            if not second_dog.isGood() or not first_dog.isGood() and randint(1, 100) > 55:
                first_dog.setMood('Bad')
                second_dog.setMood('Bad')

    def printDogsMood(self):
        """Printing dogs moods info"""
        count_good = 0
        count_bad = 0

        for dog in self.getList():
            if dog.getMood() == 'Good':
                count_good += 1
            else:
                count_bad += 1
        print(
            'Amount of happy dogs: {0} ({1}%)'.format(
                count_good, round((count_good * 100) / (count_good + count_bad), 2)
            ) + '\n' +
            'Amount of sad dogs: {0} ({1}%)'.format(count_bad, round((count_bad * 100) / (count_good + count_bad), 2))
        )

    def getDogsMood(self) -> dict:
        """Getter for dogs mood"""
        count_good = 0
        count_bad = 0

        for dog in self.getList():
            if dog.getMood() == 'Good':
                count_good += 1
            else:
                count_bad += 1
        return {
            'Good': count_good,
            'Bad': count_bad
        }

    def getRandomDog(self) -> Dog:
        """Getter for random dog"""
        return self.getList()[randint(0, len(dogs) - 1)]


"""Loading dogs names and ages"""
with open('names.txt', 'r') as names_file:
    names = [str(i)[:-1] for i in names_file]

with open('breeds.txt', 'r', encoding='utf-8') as breeds_file:
    breeds = [str(i)[:-1] for i in breeds_file]

"""Testing code"""

dogs1 = DogsGroup(1000, names, breeds)

dogs1.printDogsMood()
