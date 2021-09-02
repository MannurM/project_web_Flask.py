
import tkinter as tk

count = 0

def btn_reg(count=count):

    print('Registration!')
    import registration
    # if count == 0:
    #     import registration
    #
    # else:
    #     import registration
    # count +=1

def btn_enter():
    name_man = entre_name_man.get()
    email = entre_name_email.get()
    password = entre_password.get()


def btn_clear():
    entre_name_man.delete(0, 'end')
    entre_name_email.delete(0, 'end')
    entre_password.delete(0, 'end')


win = tk.Tk()
win.title('Обучение и проверка знаний по охране труда сотрудников ')
win.config(bg='dark green')
win.geometry('600x600+100+0')
win.minsize(300, 300)
win.maxsize(1000, 800)
win.resizable(True, True)

title_org = ' ГБОУ СОШ (ОЦ) с. Челно-Вершины'
title_man = 'Фамилия Имя (Отчество)'
title_email = 'Адрес электронной почты'
title_password = 'Пароль'
label_name_org = tk.Label(win, text=title_org, font=('Arial', 20, 'bold'), bg='dark green', fg='white').\
    grid(row=0, column=0, columnspan=5, stick='we', ipadx=5, ipady=5)  # font, bg, fg, size
label_name_man = tk.Label(win, text=title_man, font=('', 14), bg='dark green', fg='white').\
    grid(row=1, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
label_email = tk.Label(win, text=title_email, font=('', 10), bg='dark green', fg='white').\
    grid(row=2, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
label_password = tk.Label(win, text=title_password, font=('', 10), bg='dark green', fg='white').\
    grid(row=3, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size


entre_name_man = tk.Entry(win, textvariable='Введите ФИО', font=12, fg='green')
entre_name_man.grid(row=1, column=1, stick='w', padx=10, pady=10)
entre_name_man.focus()
entre_name_email = tk.Entry(win, textvariable='Введите еmail', font=12,)  # TODO для проверки использовать re??
entre_name_email.grid(row=2, column=1, stick='w', padx=10, pady=10)
entre_password = tk.Entry(win, textvariable='Введите пароль', font=12, show='*')
entre_password.grid(row=3, column=1, stick='w', padx=10, pady=10)

btn_1 = tk.Button(win, text='Войти', command=btn_enter,  font=12, bg='yellow', fg='red')
btn_1.grid(row=2, column=2, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
btn_2 = tk.Button(win, text='Очистить', command=btn_clear,  font=12, bg='yellow', fg='red')
btn_2.grid(row=3, column=2, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
btn_3 = tk.Button(win, text='Регистрация', command=btn_reg,  font=12, bg='yellow', fg='red')
btn_3.grid(row=1, column=2,  stick='we', padx=10, pady=10)  # font, bg, fg, size



#
# TODO как обновить форму с новыми параметрами

win.mainloop()