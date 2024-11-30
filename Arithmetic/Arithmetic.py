import random
import pygame

pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Immanuel\\Arithmetic\\bg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = -1)

def main():
    choices = ["+", "-", "*", "/", "%"]
    prompt = input("Hello there, what should I call you? ")
    print(f"Hello there {prompt}, welcome to the arithmetic game!!!")
    
    previous_pairs = []  
    
    while True:
        answer = input("Would you like to continue? (Yes/No) ").capitalize()
        if answer == "No":
            print(f"Thank you, Goodbye {prompt}.")
            break
        elif answer != "Yes":
            print("Please answer with 'Yes' or 'No'.")
            continue
        
        print("[1] Addition\n[2] Subtraction\n[3] Multiplication\n[4] Division\n[5] Modulus\n[6] Mixed")
        
        try:
            choice = int(input("Please select what you want to try: "))
            if choice not in range(1, 7):
                print("I said 1-6 only, please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
            continue
        
        count = 0
        guess = 10
        score = 0
        
        while guess != 0:
            count += 1
            if choice == 1:
                score = ifAddition(count, score, previous_pairs)
            elif choice == 2:
                score = ifSubtraction(count, score, previous_pairs)
            elif choice == 3:
                score = ifMultiplication(count, score, previous_pairs)
            elif choice == 4:
                score = ifDivision(count, score, previous_pairs)
            elif choice == 5:
                score = ifModulus(count, score, previous_pairs)
            elif choice == 6:
                score = ifMixed(count, score, previous_pairs, choices)
            guess -= 1
        
        print(f"Congratulations!!, your score is {score}/10, Good job!!")
        
        answer = input("Do you want to try it again? (Yes/No) ").capitalize()

def generate_unique_pair(previous_pairs):
    while True:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        if num1 != num2:  # Ensure the numbers are not the same
            pair = (num1, num2)
            if pair not in previous_pairs and (num2, num1) not in previous_pairs:
                previous_pairs.append(pair)
                return num1, num2

def ifAddition(count, score, previous_pairs):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} + {num2}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num1 + num2
    if sagot != answerNum:
        print("Oops, wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

def ifSubtraction(count, score, previous_pairs):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} - {num2}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num1 - num2
    if sagot != answerNum:
        print("Oops, Wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

def ifMultiplication(count, score, previous_pairs):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} * {num2}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num1 * num2
    if sagot != answerNum:
        print("Oops, wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

def ifDivision(count, score, previous_pairs):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num2} / {num1}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num2 / num1
    if sagot != answerNum:
        print("Oops, wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

def ifModulus(count, score, previous_pairs):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} % {num2}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num1 % num2
    if sagot != answerNum:
        print("Oops, wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

def ifMixed(count, score, previous_pairs, choices):
    operation = random.choice(choices)
    num1, num2 = generate_unique_pair(previous_pairs)
    
    if operation == "+":
        print(f"{count}. {num1} + {num2}")
        answerNum = num1 + num2
    elif operation == "-":
        print(f"{count}. {num1} - {num2}")
        answerNum = num1 - num2
    elif operation == "*":
        print(f"{count}. {num1} * {num2}")
        answerNum = num1 * num2
    elif operation == "/":
        print(f"{count}. {num2} / {num1}")
        answerNum = num2 / num1
    elif operation == "%":
        print(f"{count}. {num1} % {num2}")
        answerNum = num1 % num2
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    if sagot != answerNum:
        print("Oops, wrong!\n")
    else:
        print("Correct!!\n")
        score += 1
    return score

main()