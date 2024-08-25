from tkinter import *
from random import randint

window = Tk()
window.title("Rock-Paper-Scissors")
window.resizable(False,False)

comp_point = 0
user_point = 0
max_points = 5
#RESET game
def reset_game():
    global comp_point, user_point
    comp_point = 0
    user_point = 0
    label_score.config(text=f"You: {user_point} \t Computer: {comp_point}")
    result.set("Game Reset! Start Playing Again!")
    user_label.config(image='')
    comp_label.config(image='')

# Function to update the game based on user choice
def play_game(user_choice):
    global comp_point, user_point
    
    # Check if the game is already over
    if user_point >= max_points or comp_point >= max_points:
        result.set("Game over! Click Reset to play again.")
        return
    
    # Get computer's choice
    comp_choice = randint(1, 3)
    
    user_image=None
    comp_image=None

    # Update the images for user and computer choices
    if user_choice == 1:
        user_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\STONE_codsoft.jpeg")
    elif user_choice == 2:
        user_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\paper_codsoft.jpeg")
    elif user_choice == 3:
        user_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\scissor_codsoft.png")
    
    if comp_choice == 1:
        comp_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\STONE_codsoft.jpeg")
    elif comp_choice == 2:
        comp_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\paper_codsoft.jpeg")
    elif comp_choice == 3:
        comp_image = PhotoImage(file=r"C:\Users\Abhilove Goyal\Desktop\C++\Codsoft_Task\scissor_codsoft.png")
    
    # Display images
    user_label.config(image=user_image)
    user_label.image = user_image
    comp_label.config(image=comp_image)
    comp_label.image = comp_image
    
    # Determine the winner of the round
    if user_choice == comp_choice:
        result.set("It's a tie!")
    elif (user_choice == 1 and comp_choice == 3) or \
         (user_choice == 2 and comp_choice == 1) or \
         (user_choice == 3 and comp_choice == 2):
        user_point += 1
        result.set("You win this round!")
    else:
        comp_point += 1
        result.set("Computer wins this round!")
    
    # Update score
    label_score.config(text=f"You: {user_point} \t Computer: {comp_point}")
    
    # Check if someone has won the game
    if user_point >= max_points:
        result.set("Congratulations! You won the game!")
    elif comp_point >= max_points:
        result.set("Computer wins the game! Better luck next time!")

# Display score
label_score = Label(text=f"You: {user_point} \t Computer: {comp_point}", padx=50, pady=50)
label_score.grid(column=0, row=0, columnspan=3)

# user and computer images
user_label = Label(window)
user_label.grid(row=1, column=0, padx=20, pady=20)
comp_label = Label(window)
comp_label.grid(row=1, column=2, padx=20, pady=20)

#Result
result = StringVar()
result_label = Label(textvariable=result, font=("Arial", 24), pady=20)
result_label.grid(row=2, column=0, columnspan=3)

# Buttons for user input
Button(window, text="Rock", command=lambda: play_game(1), width=15, height=2).grid(row=3, column=0, pady=20)
Button(window, text="Paper", command=lambda: play_game(2), width=15, height=2).grid(row=3, column=1, pady=20)
Button(window, text="Scissors", command=lambda: play_game(3), width=15, height=2).grid(row=3, column=2, pady=20)

# Button to reset the game
Button(window, text="Reset", command=reset_game, width=15, height=2).grid(row=4, column=1, pady=20)

window.mainloop()
