from customtkinter import *

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

    root.mainloop()

home = CTk()
home.geometry("300x200")
home.title("Color-Following-Game - Home")

start_button = CTkButton(home, text="Start", width=10, height=2, command=open_game)
start_button.place(relx=0.5, rely=0.5, anchor="center")

home.mainloop()
