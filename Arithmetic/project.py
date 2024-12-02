import random
import pygame
import csv
import os

# Initialize pygame mixer for sounds
pygame.mixer.init()
pygame.mixer.music.load("C:\\Users\\Immanuel\\Arithmetic\\bg.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)
wrongAnswer = pygame.mixer.Sound("C:\\Users\\Immanuel\\Arithmetic\\wrong.mp3")
correctAnswer = pygame.mixer.Sound("C:\\Users\\Immanuel\\Arithmetic\\correct.mp3")

# Color codes for console output
GREEN = "\033[92m"  
RED = "\033[91m"    
RESET = "\033[0m"

# Load leaderboard from CSV
def load_leaderboard(operation):
    leaderboard = {}
    filename = f"{operation.lower()}_leaderboard.csv"  # Example: addition_leaderboard.csv
    if os.path.exists(filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                user_id, score = row
                leaderboard[user_id] = int(score)
    return leaderboard

# Save leaderboard to CSV
def save_leaderboard(operation, leaderboard):
    filename = f"{operation.lower()}_leaderboard.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for user_id, score in leaderboard.items():
            writer.writerow([user_id, score])

# Update leaderboard in memory
def update_leaderboard(leaderboard, user_id, score):
    current_score = leaderboard.get(user_id, 0)
    if score > current_score and score <= 10:
        leaderboard[user_id] = score

# Display leaderboard
def display_leaderboard(leaderboard, operation):
    print(f"\nLeaderboard for {operation}:")
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    if not sorted_leaderboard:
        print("No scores yet.")
    else:
        for user, score in sorted_leaderboard:
            print(f"{user}: {score}")

# Generate a unique pair of numbers for the quiz
def generate_unique_pair(previous_pairs):
    while True:
        num1 = random.randint(2, 10)
        num2 = random.randint(1, num1 - 1)
        pair = (num1, num2)
        if pair not in previous_pairs and (num2, num1) not in previous_pairs:
            previous_pairs.append(pair)
            return num1, num2

# Define arithmetic operations
#function for addtion
def ifAddition(count, score, previous_pairs, user_id, leaderboard):
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
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)  # Update with the new score
        return score
    
#function for subtraction
def ifSubtraction(count, score, previous_pairs, user_id, leaderboard):
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
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)  # Update with the new score
        return score

#function for multiplication
def ifMultiplication(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    print(f"{count}. {num1} * {num2 }")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = num1 * num2
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)  # Update with the new score
        return score
    
#function for dividion
def ifDivision(count, score, previous_pairs, user_id, leaderboard):
    num1, num2 = generate_unique_pair(previous_pairs)
    nums2 = num2 * num1
    print(f"{count}. {nums2} / {num1}")
    
    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    answerNum = nums2 / num1
    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)  # Update with the new score
        return score
    
#function for modulus
def ifModulus(count, score, previous_pairs, user_id, leaderboard):
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
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1
        update_leaderboard(leaderboard, user_id, score)  # Update with the new score
        return score
    
#function for mixed
def ifMixed(count, score, previous_pairs, user_id, leaderboard):
    operation = random.choice(["Addition", "Subtraction", "Multiplication", "Division", "Modulus"])
    num1, num2 = generate_unique_pair(previous_pairs)

    # Initialize the answer number based on the operation
    if operation == "Addition":
        answerNum = num1 + num2
        print(f"{count}. {num1} + {num2}")
    elif operation == "Subtraction":
        answerNum = num1 - num2
        print(f"{count}. {num1} - {num2}")
    elif operation == "Multiplication":
        answerNum = num1 * num2
        print(f"{count}. {num1} * {num2}")
    elif operation == "Division":
        nums2 = num2 * num1  # Ensure the division is valid
        answerNum = nums2 / num1
        print(f"{count}. {nums2} / {num1}")
    elif operation == "Modulus":
        answerNum = num1 % num2
        print(f"{count}. {num1} % {num2}")

    while True:
        try:
            sagot = int(input("What is your answer? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if sagot != answerNum:
        wrongAnswer.play()
        print(f"{RED}Oops, wrong!{RESET}\n")
        return score  # No score increment
    else:
        print(f"{GREEN}Correct!!{RESET}\n")
        correctAnswer.play()
        score += 1  # Increment score

    # Update the leaderboard for the mixed operation only
    update_leaderboard(leaderboard["Mixed"], user_id, score)
    
    return score

def main():
    choices = ["Addition", "Subtraction", "Multiplication", "Division", "Modulus", "Mixed"]
    prompt = input("Hello there, what should I call you? ")
    print(f"Hello there {prompt}, welcome to the arithmetic game!!!")
    
    previous_pairs = []  
    # Load leaderboard for all operations
    leaderboard = {choice: load_leaderboard(choice) for choice in choices}  # Load leaderboard for each operation

    # Load mixed leaderboard separately
    leaderboard["Mixed "] = load_leaderboard("Mixed")

    while True:
        answer = input(" Would you like to continue? (Yes/No) ").capitalize()
        if answer == "No":
            print(f"Thank you, Goodbye {prompt}.")
            # Save leaderboard for each operation before exiting
            for choice in choices:
                save_leaderboard(choice, leaderboard[choice])  # Save each leaderboard
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
                score = ifAddition(count, score, previous_pairs, prompt, leaderboard["Addition"])
            elif choice == 2:
                score = ifSubtraction(count, score, previous_pairs, prompt, leaderboard["Subtraction"])
            elif choice == 3:
                score = ifMultiplication(count, score, previous_pairs, prompt, leaderboard["Multiplication"])
            elif choice == 4:
                score = ifDivision(count, score, previous_pairs, prompt, leaderboard["Division"])
            elif choice == 5:
                score = ifModulus(count, score, previous_pairs, prompt, leaderboard["Modulus"])
            elif choice == 6:
                score = ifMixed(count, score, previous_pairs, prompt, leaderboard)
            guess -= 1
        
        print(f"Congratulations!!, your score is {score}/10, Good job!!")
        
        # Display the specific leaderboard for the chosen operation after all questions
        display_leaderboard(leaderboard[choices[choice - 1]], choices[choice - 1])  
        
        answer = input("Do you want to try it again? (Yes/No) ").capitalize()

main()