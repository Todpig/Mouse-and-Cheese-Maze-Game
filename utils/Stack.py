class Stack:
    def __init__(self):
        self.positions = []

    def __len__(self):
        return len(self.positions)
    
    def __str__(self):
        return self.positions.__str__()

    def push_stack(self, item):
        self.positions.append(item)

    def pop_stack(self):
        return self.positions.pop()
