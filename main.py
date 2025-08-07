import matplotlib
import random

def start_game():
    print("Starting game...")
    # Initialize game logic here
    # For example, set up the snake and food, start the game loop, etc.

class main:
    def __init__(self):
        self.menu = ["Start Game", "Settings", "Exit"]
        self.gride_size = 20
        self.inter = 0
        self.snake = snake()
        self.food = food()

    match self.menu:
        case "start game":
            start_game()
        case "settings":
            pass
        case "exit":
            print("Exiting game...")
            exit()


class snake:
    def __init__(self):
        color("#749351")
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
        random.randint(0, main.gride_size - 1)
        color("#801312")
