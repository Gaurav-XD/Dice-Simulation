from tkinter import *
import random

root=Tk()
root.title("Roll Dice")
root.geometry("600x400")

label=Label(root,font=('helvetica',300,'bold'),text='')





def rolldice():
    dice=['\u2680','\u2681','\u2682','\u2683','\u2684','\u2685']
    label.configure(text=f'{random.choice(dice)}')
    label.pack()
button=Button(root,font=('helvetica',25,'bold'),text='Roll dice', command=rolldice)
button.pack()
root.mainloop()