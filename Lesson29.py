# 1.

class Animal:
    def eat(self):
        return "Animal is eating"

    def sleep(self):
        return "Animal is sleeping"


class Bird(Animal):
    def eat(self):
        return "Bird is pecking at its food"

    def fly(self):
        return "Bird is flying"


class Fish(Animal):
    def swim(self):
        return "Fish is swimming"