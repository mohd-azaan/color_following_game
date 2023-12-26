from customtkinter import *
import random
import time
import pygame.mixer

label_font = ("Arial", 20) 
def main():
    file = open ("highest.csv","r")
    highest=file.readlines()
    n=len(highest)-1
    highest_name=highest[n].split(",")[1].strip()
    highest_score=int(highest[n].split(",")[0])

    def open_game():
        player_name = name_entry.get().title()
        home.destroy()  
        start_game(player_name)

    def start_game(player_name):
        nonlocal highest_name,highest_score

        root = CTk()

        highest_score_label = CTkLabel(root, text=f"High Score: {highest_score} by {highest_name}", font=label_font)
        highest_score_label.pack(side="top",padx=8, pady=10, anchor="ne")
        current_score_label = CTkLabel(root, text=f"Current Score: {player_name} {0}", font=("Arial", 20))
        current_score_label.place(rely=0.017,relx=0.02)
        root.geometry("640x640+300+130")
        root.resizable(False,False)
        root.title("Color-Following-Game")
        
        # XXX 
        
        def button_clicked(direction):
            check_sequence(direction)
            

        def check_sequence(direction):
            nonlocal sequence_index, score, player_name,highest_score,highest_name

            if direction == sequence[sequence_index]:
                pygame.mixer.init()
                button_sound = pygame.mixer.Sound('button-sound-1-trimmed-1.mp3')
                button_sound.set_volume(500)
                button_sound.play() 
                sequence_index += 1
                score += 1
                current_score_label.configure(text=f"Current Score : {player_name} {score}")
                if score > highest_score:
                    highest_score = score
                    highest_name = player_name
            else:
                pygame.mixer.init()
                button_sound = pygame.mixer.Sound('game_over_sound2.mp3')
                button_sound.set_volume(500)
                button_sound.play() 
                # print("Incorrect sequence! Game over.")
                save_highest_score(highest_score, highest_name)
                root.destroy()
                game_over(highest_score, highest_name)

            if sequence_index == len(sequence):
                update_sequence()

        def update_sequence():
            nonlocal sequence, sequence_index
            sequence.append(random.choice(["Top", "Left", "Bottom", "Right"]))
            sequence_index = 0
            # print("New sequence:", sequence)
            show_sequence()

        def show_sequence():
            nonlocal sequence
            # Disable buttons during sequence display
            top_button.configure(state="disabled")
            left_button.configure(state="disabled")
            bottom_button.configure(state="disabled")
            right_button.configure(state="disabled")

            countdown_label = CTkLabel(root, text="2", font=("Arial", 40))
            countdown_label.place(relx=0.5, rely=0.5, anchor="center")
            root.update()
            time.sleep(1)
            countdown_label.configure(text="1")
            root.update()
            time.sleep(1)
            countdown_label.configure(text="Be Ready")
            root.update()
            time.sleep(1)
            countdown_label.destroy()
            root.update()
            time.sleep(1)

            for direction in sequence:
                if direction == "Top":
                    top_button.configure(fg_color="#FFFFFF")  # Change to white
                    root.update()
                    root.after(800)  # Show for 1 second
                    top_button.configure(fg_color="#65B741")  # Revert to green
                    root.update()
                    root.after(500)  # Delay between button flashes
                elif direction == "Left":
                    left_button.configure(fg_color="#FFFFFF")  # Change to white
                    root.update()
                    root.after(800)  # Show for 1 second
                    left_button.configure(fg_color="#BF3131")  # Revert to red
                    root.update()
                    root.after(500)  # Delay between button flashes
                elif direction == "Bottom":
                    bottom_button.configure(fg_color="#FFFFFF")  # Change to white
                    root.update()
                    root.after(800)  # Show for 1 second
                    bottom_button.configure(fg_color="#FFFB73")  # Revert to yellow
                    root.update()
                    root.after(500)  # Delay between button flashes
                elif direction == "Right":
                    right_button.configure(fg_color="#FFFFFF")  # Change to white
                    root.update()
                    root.after(800)  # Show for 1 second
                    right_button.configure(fg_color="#4CB9E7")  # Revert to blue
                    root.update()
                    root.after(500)  # Delay between button flashes

            # After showing the sequence
            countdown_label = CTkLabel(root, text="Your turn", font=("Arial", 40))
            countdown_label.place(relx=0.5, rely=0.5, anchor="center")
            root.update()
            time.sleep(1)
            countdown_label.destroy()

            # Enable buttons after sequence display
            top_button.configure(state="normal")
            left_button.configure(state="normal")
            bottom_button.configure(state="normal")
            right_button.configure(state="normal")
            

        def game_over(highest_score, highest_name):
            nonlocal player_name,score
            game_over_root = CTk()
            game_over_root.geometry("640x640+300+130")
            game_over_root.resizable(False,False)
            game_over_label = CTkLabel(game_over_root, text="Game Over!", font=("Arial", 60))
            game_over_label.place(relx=0.5,rely=0.4,anchor=CENTER)
            current_score_label = CTkLabel(game_over_root, text=f"You Scored: {player_name} {score}", font=("Arial", 20))
            current_score_label.place(rely=0.2,relx=0.3)
            highest_score_label = CTkLabel(game_over_root, text=f"High Score: {highest_score} by {highest_name}", font=label_font)
            highest_score_label.pack(side="top",padx=8, pady=10, anchor="ne")
            play_again_button=CTkButton(game_over_root,text="Play Again",font=label_font,command=lambda :play_again(game_over_root,player_name))
            play_again_button.place(relx=0.66,rely=0.55,anchor=CENTER)
            home_button=CTkButton(game_over_root,text="Home",font=label_font,command=lambda :call_main(game_over_root))
            home_button.place(relx=0.33,rely=0.55,anchor=CENTER)
            game_over_root.mainloop()

        def call_main(game_over_root):
            game_over_root.destroy()
            main()
        def play_again(game_over_root,player_name):
            game_over_root.destroy()
            start_game(player_name)

        def save_highest_score(score, player_name):
            with open('highest.csv', 'w') as file:
                file.write(f"{score},{player_name}")
                # writer.writerow([score, player_name])
        
        sequence = []
        sequence_index = 0
        score = 0
        
        top_button = CTkButton(root, text="", width=150, height=150,bg_color="transparent", fg_color="#65B741", corner_radius=100,
                        hover_color="#458230", command=lambda: button_clicked("Top"))
        top_button.place(relx=0.5, rely=0.1, anchor="n")
        top_button.configure(state="disabled")  

        left_button = CTkButton(root, text="", width=150, height=150,bg_color="transparent", fg_color="#BF3131", corner_radius=100,
                                hover_color="#8C1F1F", command=lambda: button_clicked("Left"))
        left_button.place(relx=0.1, rely=0.5, anchor="w")
        left_button.configure(state="disabled")  

        bottom_button = CTkButton(root, text="", width=150, height=150,bg_color="transparent", fg_color="#FFFB73", corner_radius=100,
                                hover_color="#CCC64C", command=lambda: button_clicked("Bottom"))
        bottom_button.place(relx=0.5, rely=0.9, anchor="s")
        bottom_button.configure(state="disabled")  

        right_button = CTkButton(root, text="", width=150, height=150,bg_color="transparent", fg_color="#4CB9E7", corner_radius=100,
                                hover_color="#3384A5", command=lambda: button_clicked("Right"))
        right_button.place(relx=0.9, rely=0.5, anchor="e")
        right_button.configure(state="disabled")  
        # game_over()

        update_sequence()
        root.mainloop()
    home = CTk()
    highest_score_label=CTkLabel(home,text=f"Highest Score : {highest_score} by {highest_name} ",font=("Arial", 16) )
    highest_score_label.pack(pady=10)
    home.geometry("350x300+300+130")
    home.resizable(False,False)
    home.title("Color-Following-Game - Home")

    name_label = CTkLabel(home, text="Enter Your Name :   ",font=("Arial", 16) )
    name_label.place(relx=0.3, rely=0.3, anchor="center")

    name_entry = CTkEntry(home)
    name_entry.place(relx=0.7, rely=0.3, anchor="center")

    start_button = CTkButton(home, text="Start", command=open_game)
    start_button.place(relx=0.5, rely=0.5, anchor="center")

    home.mainloop()
main()
