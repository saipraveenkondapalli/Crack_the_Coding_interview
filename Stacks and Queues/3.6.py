"""
An animal shelter, which holds only dogs and cats,
operates on a strictly "first in, first out" basis.
People must adopt either the "oldest" (based on arrival time) 
of all animals at the shelter, or they can select whether they would prefer a dog or a cat 
(and will receive the oldest animal of that type). They cannot select which specific animal they would like.
Create the data structures to maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat.
You may use the built-in LinkedList data structure.

"""
from linked_lists import *

from queue import Queue


class Animal:
    def __init__(self) -> None:
        self.name = None
        self.order = None
    
    def set_name(self, name):
        self.name = name
    
    def set_order(self, order):
        self.order = order
    
    def get_order(self):
        return self.order
    
    def is_older_than(self, pet):
        return self.order < pet.get_order()
    

class AnimalEnqeue:
    def __init__(self) -> None:
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0
    
    def enqueue(self,animal):
        animal.set_order(self.order)
        self.order += 1
        if animal.name == "dog":
            self.dogs.enqueue(animal)
        elif animal.name == "cat":
            self.cats.enqueue(animal)
    
    def dequeueAny(self):
        if self.dogs.is_empty():
            return self.dequeueCat()
        elif self.cats.is_empty():
            return self.dequeueDog()
        dog = self.dogs.peek()
        cat = self.cats.peek()
        if dog.is_older_than(cat):
            return self.dequeueDog()
        else:
            return self.dequeueCat()
    
    def dequeueDog(self):
        return self.dogs.dequeue()
    
    def dequeueCat(self):
        return self.cats.dequeue()
    

class Dog(Animal):
    def __init__(self, tag) -> None:
        super().__init__()
        self.name = "dog"
        self.tag = self.name + str(tag)


class Cat(Animal):
    def __init__(self, tag) -> None:
        super().__init__()
        self.name = "cat"
        self.tag = self.name + str(tag)


if __name__ == "__main__":
    animal = AnimalEnqeue()
    animal.enqueue(Dog(1))
    animal.enqueue(Cat(1))
    animal.enqueue(Dog(2))
    animal.enqueue(Cat(2))
    animal.enqueue(Dog(3))
    animal.enqueue(Cat(3))
    animal.enqueue(Dog(4))
    animal.enqueue(Cat(4))
    