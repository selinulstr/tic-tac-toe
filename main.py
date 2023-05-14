from tkinter import *
from tkinter import ttk
from tkinter.ttk import Style
from tkinter import messagebox

clicked = True
count = 0


def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def OnButtonClick(button):
    global clicked, count
    if button['text'] == '' and clicked:
        button['text'] = 'X'
        clicked = False
        count += 1
        if_winner()
    elif button['text'] == '' and not clicked:
        button['text'] = 'O'
        clicked = True
        count += 1
        if_winner()
    else:
        messagebox.showerror("Tic Tac Toe", "Please select a blank box")


def if_winner():
    global winner, b1, b2, b3, b4, b5, b6, b7, b8, b9
    winner = False

    if b1['text'] == "X" and b2['text'] == 'X' and b3['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b4['text'] == "X" and b5['text'] == 'X' and b6['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b7['text'] == "X" and b8['text'] == 'X' and b9['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b1['text'] == "X" and b4['text'] == 'X' and b7['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b2['text'] == "X" and b5['text'] == 'X' and b8['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b3['text'] == "X" and b6['text'] == 'X' and b9['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b1['text'] == "X" and b5['text'] == 'X' and b9['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b3['text'] == "X" and b5['text'] == 'X' and b7['text'] == 'X':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "X is the winner!")
        disable_all_buttons()

    elif b1['text'] == "O" and b2['text'] == 'O' and b3['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b4['text'] == "O" and b5['text'] == 'O' and b6['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b7['text'] == "O" and b8['text'] == 'O' and b9['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b1['text'] == "O" and b4['text'] == 'O' and b7['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b2['text'] == "O" and b5['text'] == 'O' and b8['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b3['text'] == "O" and b6['text'] == 'O' and b9['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b1['text'] == "O" and b5['text'] == 'O' and b9['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    elif b3['text'] == "O" and b5['text'] == 'O' and b7['text'] == 'O':

        winner = True
        messagebox.showinfo("Tic Tac Toe", "O is the winner!")
        disable_all_buttons()

    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disable_all_buttons()


root = Tk()
root.title("Tic-Tac-Toe Game")
style = ttk.Style()
style.theme_use('alt')
style.configure("TButton")
style.map('TButton', background=[('disabled', 'green'), ('active', 'white')],
          font="courier 20")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

def play_again():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global clicked, count
    clicked = True
    count = 0
    b1 = ttk.Button(root, text="")
    b1.grid(row=1, column=0, ipady=20)
    b1.config(command=lambda button=b1: OnButtonClick(button))
    b2 = ttk.Button(root, text="")
    b2.grid(row=1, column=1, ipady=20)
    b2.config(command=lambda button=b2: OnButtonClick(button))
    b3 = ttk.Button(root, text="")
    b3.grid(row=1, column=2, ipady=20)
    b3.config(command=lambda button=b3: OnButtonClick(button))
    b4 = ttk.Button(root, text="")
    b4.grid(row=2, column=0, ipady=20)
    b4.config(command=lambda button=b4: OnButtonClick(button))
    b5 = ttk.Button(root, text="")
    b5.grid(row=2, column=1, ipady=20)
    b5.config(command=lambda button=b5: OnButtonClick(button))
    b6 = ttk.Button(root, text="")
    b6.grid(row=2, column=2, ipady=20)
    b6.config(command=lambda button=b6: OnButtonClick(button))
    b7 = ttk.Button(root, text="")
    b7.grid(row=3, column=0, ipady=20)
    b7.config(command=lambda button=b7: OnButtonClick(button))
    b8 = ttk.Button(root, text="")
    b8.grid(row=3, column=1, ipady=20)
    b8.config(command=lambda button=b8: OnButtonClick(button))
    b9 = ttk.Button(root, text="")
    b9.grid(row=3, column=2, ipady=20)
    b9.config(command=lambda button=b9: OnButtonClick(button))


game_menu = Menu(root)
root.config(menu=game_menu)

options_menu = Menu(game_menu, tearoff=False)
game_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Restart", command=play_again)

play_again()
root.mainloop()
