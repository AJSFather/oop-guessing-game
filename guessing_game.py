import random

class GuessingGame:
    
    def __init__(self, num):
        self.num = num
        self.answer_number = random.randint(1,num)
        self.solved = False

    def guess(self, user_guess):
        if user_guess < self.answer_number:
            print(self.answer_number)
            return f"{user_guess} is too low, try again!"
        elif user_guess > self.answer_number:
            print(self.answer_number)
            return f"{user_guess} is too high, try again!"
        else:
            self.solved = True
            return "correct! you guessed it!"
    def solved(self):
        return self.solved
    
    


# print(game.guess(5))  # => 'low'
# print(game.solved)    # =>  False
# print(game.guess(20)) # => 'high'
# print(game.solved)   # => False
# print(game.guess(10)) # => 'correct'
# print(game.solved)   # => True

