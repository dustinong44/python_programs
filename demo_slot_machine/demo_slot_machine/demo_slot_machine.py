
import random
import tkinter as tk
from tkinter import messagebox

def spin_wheel():
    """Simulate a slot machine spin."""
    symbols = ['🍒', '🍋', '🔔', '⭐', '🍉']
    return [random.choice(symbols) for _ in range(3)]

def check_win(spin):
    """Check if the player wins."""
    return spin[0] == spin[1] == spin[2]

def play_game():
    global balance
    try:
        bet = float(bet_entry.get())
        if bet > balance or bet <= 0:
            messagebox.showerror("Error", "Invalid bet amount.")
            return
    except ValueError:
        messagebox.showerror("Error", "Enter a valid bet amount.")
        return
    
    balance -= bet
    spin = spin_wheel()
    spin_result.set(" | ".join(spin))
    
    if check_win(spin):
        winnings = bet * 5
        balance += winnings
        messagebox.showinfo("Win!", f"You won! Payout: ${winnings:.2f}")
    else:
        messagebox.showinfo("Lost", "You lost. Better luck next time!")
    
    balance_var.set(f"Balance: ${balance:.2f}")
    if balance <= 0:
        messagebox.showinfo("Game Over", "You're out of money! Game over.")
        root.quit()

def start_game():
    global balance
    try:
        balance = float(deposit_entry.get())
        if balance <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Enter a valid deposit amount.")
        return
    
    balance_var.set(f"Balance: ${balance:.2f}")
    deposit_frame.pack_forget()
    game_frame.pack()


root = tk.Tk()
root.title("Casino Slot Machine")

balance = 0

deposit_frame = tk.Frame(root)
tk.Label(deposit_frame, text="Enter deposit amount: $").pack()
deposit_entry = tk.Entry(deposit_frame)
deposit_entry.pack()
tk.Button(deposit_frame, text="Start Game", command=start_game).pack()
deposit_frame.pack()


game_frame = tk.Frame(root)
spin_result = tk.StringVar()
balance_var = tk.StringVar()

tk.Label(game_frame, textvariable=balance_var).pack()
tk.Label(game_frame, textvariable=spin_result, font=("Arial", 24)).pack()
tk.Label(game_frame, text="Enter your bet: $").pack()
bet_entry = tk.Entry(game_frame)
bet_entry.pack()
tk.Button(game_frame, text="Spin", command=play_game).pack()

game_frame.pack_forget()

root.mainloop()

