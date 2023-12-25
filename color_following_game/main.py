from customtkinter import *
import random
import csv

def open_game():
    home.destroy()  # Close the home window
    start_game()

def start_game():
    root = CTk()
    root.geometry("500x500")
    root.title("Color-Following-Game")

    # Function to print a message when a button is clicked
    def button_clicked(direction):
        print(f"Button {direction} clicked.")
        check_sequence(direction)

    # Check if the clicked button is in the correct sequence
    def check_sequence(direction):
        nonlocal sequence_index, score, highest_score
        if direction == sequence[sequence_index]:
            sequence_index += 1
            score += 1
            if score > highest_score:
                highest_score = score
        else:
            print("Incorrect sequence! Game over.")
            save_highest_score()
            root.destroy()
            rematch_prompt()

        if sequence_index == len(sequence):
            update_sequence()

    # Update the sequence and show it
    def update_sequence():
        nonlocal sequence, sequence_index
        sequence.append(random.choice(["Top", "Left", "Bottom", "Right"]))
        sequence_index = 0
        print("New sequence:", sequence)
        show_sequence()

    # Show the current sequence by highlighting the buttons
    def show_sequence():
        nonlocal sequence
        for direction in sequence:
            if direction == "Top":
                top_button.configure(fg_color="#FF0000")  # Change to red
                root.update()
                root.after(1000)  # Show for 1 second
                top_button.configure(fg_color="#65B741")  # Revert to green
                root.update()
                root.after(500)  # Delay between button flashes
            elif direction == "Left":
                left_button.configure(fg_color="#FF0000")  # Change to red
                root.update()
                root.after(1000)  # Show for 1 second
                left_button.configure(fg_color="#BF3131")  # Revert to red
                root.update()
                root.after(500)  # Delay between button flashes
            elif direction == "Bottom":
                bottom_button.configure(fg_color="#FF0000")  # Change to red
                root.update()
                root.after(1000)  # Show for 1 second
                bottom_button.configure(fg_color="#FFFB73")  # Revert to yellow
                root.update()
                root.after(500)  # Delay between button flashes
            elif direction == "Right":
                right_button.configure(fg_color="#FF0000")  # Change to red
                root.update()
                root.after(1000)  # Show for 1 second
                right_button.configure(fg_color="#4CB9E7")  # Revert to blue
                root.update()
                root.after(500)  # Delay between button flashes

    def rematch_prompt():
        rematch_window = CTk()
        rematch_window.geometry("300x100")
        rematch_window.title("Rematch")
        rematch_label = CTkLabel(rematch_window, text="Do you want to play again?")
        rematch_label.pack()

        def play_again():
            rematch_window.destroy()
            start_game()

        def end_game():
            save_highest_score()
            rematch_window.destroy()

        rematch_yes_button = CTkButton(rematch_window, text="Yes", width=8, height=1, command=play_again)
        rematch_yes_button.pack(side="left")

        rematch_no_button = CTkButton(rematch_window, text="No", width=8, height=1, command=end_game)
        rematch_no_button.pack(side="right")

    def save_highest_score():
        with open('highest.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([highest_score])

    # Load the highest score from file
    try:
        with open('highest.csv', 'r') as file:
            reader = csv.reader(file)
            highest_score = int(next(reader)[0])
    except FileNotFoundError:
        highest_score = 0

    sequence = []  # Initialize the sequence
    sequence_index = 0  # Initialize the sequence index
    score = 0  # Initialize the score

    # Top button - Green
    top_button = CTkButton(root, text="", width=150, height=150, fg_color="#65B741", corner_radius=100, hover_color="#458230", command=lambda: button_clicked("Top"))
    top_button.place(relx=0.5, rely=0.1, anchor="n")

    # Left button - Red
    left_button = CTkButton(root, text="", width=150, height=150, fg_color="#BF3131", corner_radius=100, hover_color="#8C1F1F", command=lambda: button_clicked("Left"))
    left_button.place(relx=0.1, rely=0.5, anchor="w")

    # Bottom button - Yellow
    bottom_button = CTkButton(root, text="", width=150, height=150, fg_color="#FFFB73", corner_radius=100, hover_color="#CCC64C", command=lambda: button_clicked("Bottom"))
    bottom_button.place(relx=0.5, rely=0.9, anchor="s")

    # Right button - Blue
    right_button = CTkButton(root, text="", width=150, height=150, fg_color="#4CB9E7", corner_radius=100, hover_color="#3384A5", command=lambda: button_clicked("Right"))
    right_button.place(relx=0.9, rely=0.5, anchor="e")

    update_sequence()  # Start the first sequence
    root.mainloop()

home = CTk()
home.geometry("300x200")
home.title("Color-Following-Game - Home")

name_label = CTkLabel(home, text="Enter Your Name:")
name_label.place(relx=0.3, rely=0.3, anchor="center")

name_entry = CTkEntry(home)
name_entry.place(relx=0.7, rely=0.3, anchor="center")

start_button = CTkButton(home, text="Start", width=10, height=2, command=open_game)
start_button.place(relx=0.5, rely=0.6, anchor="center")

home.mainloop()
