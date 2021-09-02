import tkinter as tk


def check_password(entre_reg_password, entre_reg_password2):
    password = entre_reg_password.get()
    password2 = entre_reg_password2.get()
    if not password == password2:
        label_reg_text = tk.Label(win_reg, text='пароли не совпадают')
        label_reg_text.grid(row=10, column=0)
        return False
    else:
        label_reg_text = tk.Label(win_reg, text='пароли совпадают')
        label_reg_text.grid(row=10, column=0)
        return True


def btn_entr():
    bool_check = check_password(entre_reg_password, entre_reg_password2)
    print(bool_check)
    return bool_check


def btn_cls():
    entre_reg_man.delete(0, 'end')
    entre_reg_email.delete(0, 'end')
    entre_reg_password.delete(0, 'end')
    entre_reg_password2.delete(0, 'end')


def btn_cls_pass():
    entre_reg_password.delete(0, 'end')
    entre_reg_password2.delete(0, 'end')


def btn_ext():
    win_reg.destroy()


win_reg = tk.Tk()
win_reg.title('Регистрация!')
win_reg.config()
win_reg.geometry('550x450+120+50')
reg_man = 'Введите Фамилию Имя Отчество'
reg_email = ' введите адрес электронной почты,  если имеется'
reg_password = 'введите Пароль'
reg_password2 = 'повторите Пароль'


label_reg_man = tk.Label(win_reg, text=reg_man, font=('', 10), bg='dark green', fg='white'). \
    grid(row=1, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
label_reg_email = tk.Label(win_reg, text=reg_email, font=('', 10), bg='dark green', fg='white'). \
    grid(row=2, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
label_reg_password = tk.Label(win_reg, text=reg_password, font=('', 10), bg='dark green', fg='white'). \
    grid(row=3, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
label_reg_password2 = tk.Label(win_reg, text=reg_password2, font=('', 10), bg='dark green', fg='white'). \
    grid(row=4, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size

entre_reg_man = tk.Entry(win_reg, textvariable='Введите ФИО', font=12, fg='green')
entre_reg_man.grid(row=1, column=1, stick='w', padx=10, pady=10)
entre_reg_man.focus()
entre_reg_email = tk.Entry(win_reg, textvariable='Введите еmail', font=12, )  # TODO для проверки использовать re??
entre_reg_email.grid(row=2, column=1, stick='w', padx=10, pady=10)
entre_reg_password = tk.Entry(win_reg, textvariable='Введите пароль', font=12, show='*')
entre_reg_password.grid(row=3, column=1, stick='w', padx=10, pady=10)
entre_reg_password2 = tk.Entry(win_reg, textvariable='Повторите пароль', font=12, show='*')
entre_reg_password2.grid(row=4, column=1, stick='w', padx=10, pady=10)

name_man = entre_reg_man.get()
email = entre_reg_email.get()
password = entre_reg_password.get()


btn_save = tk.Button(win_reg, text='Сохранить', command=btn_entr, font=12, bg='yellow', fg='red'). \
    grid(row=5, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
btn_clr = tk.Button(win_reg, text='Очистить всё', command=btn_cls, font=12, bg='yellow', fg='red'). \
    grid(row=5, column=1, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
btn_clr_pass = tk.Button(win_reg, text='Очистить пароли', command=btn_cls_pass, font=12, bg='yellow', fg='red'). \
    grid(row=6, column=1, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size
btn_exit = tk.Button(win_reg, text='Выход без сохранения', command=btn_ext, font=12, bg='yellow', fg='red'). \
    grid(row=6, column=0, columnspan=1, stick='we', padx=10, pady=10)  # font, bg, fg, size



win_reg.mainloop()