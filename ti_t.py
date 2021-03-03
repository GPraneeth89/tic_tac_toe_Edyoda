from tkinter import *
from tkinter import messagebox
# from ti_t import *
root=Tk()
root.title("Tic -Tac-Toe")
on_click=True
c_o=0

# row 0 buttons
b7=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b7))
b7.grid(row=0,column=0)
b8=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b8))
b8.grid(row=0,column=1)
b9=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b9))
b9.grid(row=0,column=2)
# row 1 buttons
b4=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b4))
b4.grid(row=1,column=0)
b5=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b5))
b5.grid(row=1,column=1)
b6=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b6))
b6.grid(row=1,column=2)

# row 2 buttons
b1=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b1))
b1.grid(row=2,column=0)
b2=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b2))
b2.grid(row=2,column=1)
b3=Button(root,text=" ", font=("Helvetica",20),height=3,width=6,bg="#FFFFFA",command=lambda:b_click(b3))
b3.grid(row=2,column=2)

from main import disable_all,checkifwon,b_click


root.mainloop()