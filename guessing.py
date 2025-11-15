import guessing_game


game = guessing_game.GuessingGame(100)
last_guess = 0
last_result = 0

print('HEY PLAYER1 WELCOME TO MY NUMBER GUESSING GAME')
user_input = input("What is your name: ")
print(f'Welcome {user_input}! I hope you are ready to play!')
# user_guess = int(input("pick a number: "))
# print(user_guess)



while game.solved == False:
    last_guess = int(input("enter guess: "))
    last_result = game.guess(last_guess)
    if last_guess != None:
        print(f"Oops! Your last guess ({last_guess}) was {last_result}")

print(f"{last_guess} was correct!")