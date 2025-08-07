import matplotlib
import random

class main:
    def __init__(self):
        self.menu = ["Start Game", "Settings", "Exit"]
        self.gride_size = 20
        self.value = random.randint(1, 100)
        self.inter = 0
        self.snake = snake()
        self.food = food()

class snake:
    def __init__(self):
        self.length = 3
        self.position = (0, 0)
        self.body = [(0, 0), (0, 1), (0,2)]

    def game_over():
        if snake.head in snake.body[1:] | snake.position < max(main.gride_size) | snake.position > snake.position < min(main.gride_size):

            print("Game Over!")
            return True
    
    def move(self, direction):
        match direction:
            case 'up':
                self.position = (self.position[0], self.position[1] + 1)
            case 'down':
                self.position = (self.position[0], self.position[1] - 1)
            case 'left':
                self.position = (self.position[0] - 1, self.position[1])
            case 'right':
                self.position = (self.position[0] + 1, self.position[1])
            case _:
                print("Invalid direction")

class food():
    def __init__(self):
        pass