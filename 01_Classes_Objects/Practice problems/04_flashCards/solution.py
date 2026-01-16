import random
class Flashcard:
    def __init__(self):

        self.fruits = {
            "banana": "yellow",
            "strawberry": "pink",
            "cherry": "red",
            "grapes": "purple",
            "mango": "yellow"
        }
    
    def play(self):
        fruit,color = random.choice(list(self.fruits.items()))
        answer = input(f'enter the color of {fruit} : ')
        if answer.lower() == color:
            print("correct answer")
        else:
            print("wrong answer")

obj = Flashcard()
obj.play()