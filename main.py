
from tkinter import *
from tkinter import messagebox
from ti_t import b1,b2,b3,b4,b5,b6,b7,b8,b9,on_click,c_o


def disable_all():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


    
def checkifwon():
    global winner
    winner=False
    if b1["text"] == "X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="#3EDF10")
        b2.config(bg="#3EDF10")
        b3.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b4["text"] == "X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b6.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b7["text"] == "X" and b8["text"]=="X" and b9["text"]=="X":
        b7.config(bg="#3EDF10")
        b8.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b1["text"] == "X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="#3EDF10")
        b4.config(bg="#3EDF10")
        b7.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b2["text"] == "X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b8.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b3["text"] == "X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="#3EDF10")
        b6.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b1["text"] == "X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," X wins")
        disable_all()
    elif b3["text"] == "X" and b5["text"]=="X" and b7["text"]=="X":
        b3.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b7.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    # O
    if b1["text"] == "O" and b2["text"]=="O" and b3["text"]=="O":
        b1.config(bg="#3EDF10")
        b2.config(bg="#3EDF10")
        b3.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b4["text"] == "O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b6.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b7["text"] == "O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="#3EDF10")
        b8.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b1["text"] == "O" and b4["text"]=="O" and b7["text"]=="O":
        b1.config(bg="#3EDF10")
        b4.config(bg="#3EDF10")
        b7.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b2["text"] == "O" and b5["text"]=="O" and b8["text"]=="O":
        b2.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b8.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b3["text"] == "O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="#3EDF10")
        b6.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b1["text"] == "O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b9.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()
    elif b3["text"] == "O" and b5["text"]=="O" and b7["text"]=="O":
        b3.config(bg="#3EDF10")
        b5.config(bg="#3EDF10")
        b7.config(bg="#3EDF10")
        winner=True
        messagebox.showinfo("Tic Tac Toe"," O wins")
        disable_all()   
    if c_o == 9 and winner ==False:
        messagebox.showinfo("Tic Tac Toe","It's Tie")
        disable_all()



def b_click(b):
    global on_click,c_o
    if b["text"]==" " and on_click==True:
        b["text"]="X"
        on_click=False
        c_o+=1
        checkifwon()
    elif b["text"]==" " and on_click==False:
        b["text"]="O"
        on_click=True
        c_o+=1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! that box has already been selected\nPick another one")