import random

COLORS = ["R","G","B","Y","W","O"]
TRIES = 10
CODE_LENGTH = 4

#Generates the code
def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code

#Allows the user to input their guess and check if it is valid
def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess)!= CODE_LENGTH:
            print(f"You must guess {CODE_LENGTH} colors.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color: {color}. Try again.")
                break
        else:
            break
    
    return guess

#Checks if the code is correct
def check_code(guess,real_code):
    
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 0  
        color_counts[color] += 1

    #Find the colors in the correct position    
    for guess_color, real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] += 1

    #Find the colors in the incorrect position
    for guess_color, real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos
    
#Overall control sequence for the game
def game():

    print(f"Welcome to Mastermind, you have {TRIES} tries to guess the code.")
    print("The valid colors are ", *COLORS)

    code = generate_code()
   
    for attempts in range(1, TRIES + 1):
        print(f"You have {TRIES-attempts + 1} tries left.")
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess,code)
        
        if correct_pos == len(guess) and incorrect_pos == 0:
            print(f"Congratulations! You guessed the code in {attempts} tries.")
            break
        
        print(f"Correct Positions: {correct_pos} | Incorrect Positions{incorrect_pos}")
       
    else:
        print(f"Sorry, you ran out of tries. The code was: ", *code)

if __name__ == "__main__":
    game()