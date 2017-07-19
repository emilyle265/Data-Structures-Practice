# an animal shelter, which holds only dogs and cats, operates on a strict FIFO
# basis. People must adopt either the oldest of all animals at the shelter,
# or they can select whether they would prefer a dog or a cat (and will receive
# the oldeest animal of hta tytpe). They can't select which specific animal they 
# would like. Create the data structure to maintain this system and implement 
# operations such as enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use
# the built in LinkedList data structure


class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):

    def enqueue(self, item):
        self.items.append(item)

    def isEmpty(self):
        return self.items == []

class AnimalShelterQueue:
    def __init__(self, species=None):
        self.allAnimals = Queue()
        self.allCats = Queue()
        self.allDogs = Queue()
        self.species = species

    def enqueueAll(self, animal, species):
        self.allAnimals.append(animal)

        if self.species == 'cat':
            self.allCats.append(animal, self.species)
        else:
            self.allDogs.append(animal, self.species)

    def adopt(self, species):
        if self.species == 'cat':
            dequeueCat()
        elif self.species == 'dog':
            dequeueDog()
        else:
            dequeueAny()


    def dequeueAny(self):
        return self.allAnimals.pop(0)

    # must also dequeueAny to remove from allAnimals list
    def dequeueDog(self):
        dequeueAny()
        return self.allDogs.pop(0)

    # must also dequeueAny to remove from allAnimals list
    def dequeueCat(self):
        dequeueAny()
        return self.allCats.pop(0)




