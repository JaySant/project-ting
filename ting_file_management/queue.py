from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.items = list()

    def __len__(self):
        return len(self.items)

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        return self.items.pop(0)

    def search(self, index):
        if index >= 0 and index < len(self.items):
            return self.items[index]
        raise IndexError("Índice Inválido ou Inexistente")
