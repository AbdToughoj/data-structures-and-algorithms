class AnimalShelter:
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []

    def enqueue(self, animal):
        if animal.species == "dog":
            self.dog_queue.append(animal)
        elif animal.species == "cat":
            self.cat_queue.append(animal)

    def dequeue():
        pass