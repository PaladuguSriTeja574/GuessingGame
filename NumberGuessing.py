import random
import tkinter as tk
from tkinter import messagebox

def getDigits(num):
    return [int(i) for i in str(num)]

def noDuplicates(num):
    num_li = getDigits(num)
    return len(num_li) == len(set(num_li))

def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num

def numOfBullsCows(num, guess):
    bull_cow = [0, 0]
    num_li = getDigits(num)
    guess_li = getDigits(guess)
    
    for i, j in zip(num_li, guess_li):
        if j in num_li:
            if j == i:
                bull_cow[0] += 1
            else:
                bull_cow[1] += 1
    return bull_cow

def check_guess():
    global tries, num
    guess = entry_guess.get()
    if not guess.isdigit() or len(guess) != 4:
        messagebox.showerror("Invalid Input", "Enter a 4 digit number only.")
        return
    
    guess = int(guess)
    if not noDuplicates(guess):
        messagebox.showerror("Invalid Input", "Number should not have repeated digits.")
        return
    
    bull_cow = numOfBullsCows(num, guess)
    result_text.set(f"{bull_cow[0]} bulls, {bull_cow[1]} cows")
    tries -= 1
    tries_text.set(f"Tries left: {tries}")
    
    if bull_cow[0] == 4:
        messagebox.showinfo("Congratulations", "You guessed right!")
        reset_game()
    elif tries == 0:
        messagebox.showinfo("Game Over", f"You ran out of tries. The number was {num}")
        reset_game()

def reset_game():
    global tries, num
    tries = int(entry_tries.get())
    tries_text.set(f"Tries left: {tries}")
    num = generateNum()
    entry_guess.delete(0, tk.END)
    result_text.set("")

app = tk.Tk()
app.title("Bulls and Cows Game")

tk.Label(app, text="Bulls and Cows Game", font=("Arial", 16)).pack(pady=10)
tk.Label(app, text="Bull: correct number in correct place").pack()
tk.Label(app, text="Cow: correct number in wrong place").pack()

tk.Label(app, text="Enter number of tries:").pack(pady=5)
entry_tries = tk.Entry(app)
entry_tries.pack()
entry_tries.insert(0, "10")

tk.Label(app, text="Enter your guess:").pack(pady=5)
entry_guess = tk.Entry(app)
entry_guess.pack()

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, font=("Arial", 14)).pack(pady=10)

tries_text = tk.StringVar()
tk.Label(app, textvariable=tries_text).pack()

tk.Button(app, text="Submit Guess", command=check_guess).pack(pady=5)

tries = 10
num = generateNum()
reset_game()

app.mainloop()
