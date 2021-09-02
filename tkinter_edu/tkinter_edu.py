
import tkinter as tk
count = 0


def btn_1():
    print('Hello!')


def btn_2():
    label = tk.Label(win, text='text!!!')
    label.pack()


def counter():
    global count
    count += 1
    btn4['text'] = f'Счетчик {count}'

win = tk.Tk()
photo = tk.PhotoImage(file='fav.png')
win.iconphoto(False, photo)
win.title('Первое графическое!!')
# win.config(bg='green')
win.geometry('500x500+500+100')
win.minsize(300, 300)
win.maxsize(1000, 700)
win.resizable(True, True)

# btn1 = tk.Button(win, text='1',
#                  command=btn_1
#                  )
# btn2 = tk.Button(win, text='2',
#                  command=btn_2
#                  )
# btn3 = tk.Button(win, text='3',
#                  command=lambda: tk.Label(win, text='text new!!!').pack()
#                  )
# btn4 = tk.Button(win, text=f'Счетчик {count}',
#                  command=counter,
#                  activebackground='blue',
#                  activeforeground='white',
#                  bg='red',
#                  state=tk.DISABLED # отключает кнопку
#                  )
#
#
# btn1.pack()
# btn2.pack()
# btn3.pack()
# btn4.pack()

btn5 = tk.Button(win, text='Hello')
btn6 = tk.Button(win, text='Hello')
btn7 = tk.Button(win, text='Hello')
btn8 = tk.Button(win, text='Hello')
btn9 = tk.Button(win, text='Hello')


btn5.grid(row=0, column=0, stick='we')
btn6.grid(row=0, column=1)
btn7.grid(row=1, column=0, columnspan=2, stick='we')
btn8.grid(row=0, column=2, rowspan=2, stick='ns')
btn9.grid(row=0, column=3, rowspan=2, stick='s')
win.grid_columnconfigure(0, minsize=200)
win.grid_columnconfigure(1, minsize=200)
win.grid_rowconfigure(1, minsize=200)
win.grid_rowconfigure(2, minsize=200)

win.mainloop()

from tkinter import *

root1 = Tk()
root2 = Tk()
root1.after(500, root1.mainloop) # первый цикл запускаем в фоне
root2.mainloop()

