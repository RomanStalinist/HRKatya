import os
import db.db
import customtkinter as ct
from models.user import User
import tkinter.messagebox as mb
import tkinter.simpledialog as sd
from views import login, sign_up, main, employees, passports, add_passport, add_employee

sqlite = db.db.prepare()
ct.set_appearance_mode('light')
ct.set_default_color_theme('blue')


class _SESSION:
    def __init__(self, user: User = User(-1, '', '')):
        self.user = user

    def set_user(self, user: User):
        self.user = user


def switch_window(new_window):
    global root
    root.withdraw()
    root = new_window
    root.deiconify()
    root.protocol("WM_DELETE_WINDOW", lambda: os._exit(0))
    root.mainloop()


def update_name_label(text):
    main.name_label.configure(text=text)


def auth():
    global session
    login_text = login.login_entry.get()
    password_text = login.password_entry.get()

    if len(login_text) == 0 or len(password_text) == 0:
        mb.showerror(message='Заполните все поля', title='Ошибка')
        return

    result = sqlite.query(
        table='Пользователи', selection='Логин = ? AND Пароль = ?', selectionArgs=(login_text, password_text)
    )

    if len(result) == 0:
        mb.showerror(message='Неверный логин или пароль', title='Ошибка')
        return

    found = result[0]
    user = User(found[0], found[1], found[2])
    session.set_user(user)
    update_name_label(user.login)
    switch_window(main.window)


def signup():
    global session
    login_text = sign_up.login_entry.get()
    password_text = sign_up.password_entry.get()
    repeat_password_text = sign_up.repeat_password_entry.get()

    if len(login_text) == 0 or len(password_text) == 0 or len(repeat_password_text) == 0:
        mb.showerror(title='Ошибка', message='Все поля должны быть заполнены')
    elif len(login_text) > 20:
        mb.showerror(title='Ошибка', message='Имя не больше 20 символов')
    elif password_text != repeat_password_text:
        mb.showerror(title='Ошибка', message='Пароли не совпадают')
    else:
        found = sqlite.query(table='Пользователи', selection='Логин = ?', selectionArgs=(login_text,))

        if len(found) > 0:
            mb.showerror(title='Ошибка', message='Логин уже занят')
            return

        sqlite.insert(table='Пользователи', values={
            'Логин': login_text,
            'Пароль': password_text
        })

        new = sqlite.query(table='Пользователи', selection='Логин = ?', selectionArgs=(login_text, ))[0]
        user = User(new[0], new[1], new[2])
        mb.showinfo(title='Успех', message=f'Добро пожаловать, {user.login}!')
        session.set_user(user)
        update_name_label(user.login)
        switch_window(main.window)


def logout():
    global session
    session.set_user(None)
    update_name_label('')
    switch_window(login.window)


def add_passport_click():
    seria = add_passport.seria_entry.get()
    number = add_passport.number_entry.get()
    fullname = add_passport.fullname_entry.get()
    sex = add_passport.sex_combobox.get()
    dob = add_passport.dob_entry.get()
    pob = add_passport.pob_entry.get()

    if len(seria) > 0 and len(number) > 0 and len(fullname) > 0 and len(sex) > 0 and len(dob) > 0 and len(pob) > 0:
        try:
            sqlite.insert(table='Паспорта', values={
                'Серия': seria,
                'Номер': number,
                'ФИО': fullname,
                'Пол': sex,
                'ДатаРождения': dob,
                'МестоРождения': pob
            })

            passports_data = sqlite.query(table='Паспорта')

            for i in range(len(passports.table.get())):
                passports.table.delete_row(i + 1)

            for row in passports_data:
                passports.table.add_row(row)

            mb.showinfo('Успех', 'Паспорт добавлен')
            switch_window(passports.window)

        except Exception as ex:
            mb.showerror('Ошибка', ex)
    else:
        mb.showerror('Ошибка', 'Все поля должны быть заполненными')


def show_delete_passport():
    passport_id = sd.askstring(title='Информация', prompt='Код паспорта')
    try:
        sqlite.delete(table='Паспорта', whereClause='Код = ?', whereArgs=(int(passport_id), ))
        passports_data = sqlite.query(table='Паспорта')
        headers = ['Код', 'Серия', 'Номер', 'ФИО', 'Пол', 'Дата Рождения', 'Место Рождения']
        p = [headers] + passports_data
        passports.table.configure(values=p, rows=len(p))
        sqlite.commit()
    except Exception as ex:
        mb.showerror('Ошибка', ex)


def add_employee_click():
    education = add_employee.education_entry.get()
    job = add_employee.job_entry.get()
    profession = add_employee.profession_entry.get()
    department = add_employee.department_entry.get()
    enrollment_date = add_employee.enrollment_date_entry.get()
    salary = add_employee.salary_entry.get()
    passport_id = add_employee.passport_combobox.get()

    if (len(education) > 0 and len(job) > 0 and len(profession) > 0 and len(department) > 0 and len(enrollment_date) > 0
            and len(salary) > 0 and len(passport_id) > 0 and str.isnumeric(salary)):
        try:
            sqlite.insert(table='Работники', values={
                'Образование': education,
                'Должность': job,
                'Профессия': profession,
                'Подразделение': department,
                'ДатаПоступленияНаРаботу': enrollment_date,
                'Оклад': salary,
                'ПаспортныеДанные': passport_id,
            })

            employees_data = sqlite.query(table='Работники')

            for i in range(len(passports.table.get())):
                employees.table.delete_row(i + 1)

            for row in employees_data:
                employees.table.add_row(row)

            switch_window(employees.window)
        except Exception as ex:
            mb.showerror('Ошибка', ex)
        return

    mb.showerror('Ошибка', 'Все поля должны быть заполненными')


def show_delete_employee():
    employee_id = sd.askstring(title='Информация', prompt='Код работника')
    try:
        sqlite.delete(table='Работники', whereClause='Код = ?', whereArgs=(int(employee_id),))
        employees_data = sqlite.query(table='Работники')
        headers = ['Код', 'Образование', 'Должность', 'Профессия', 'Подразделение', 'Дата поступления', 'Оклад',
                   'Паспортные данные']
        e = [headers] + employees_data
        employees.table.configure(values=e, rows=len(e))
        sqlite.commit()
    except Exception as ex:
        mb.showerror('Ошибка', ex)


if __name__ == "__main__":
    root = ct.CTk()

    login.login_btn._command = auth
    login.sign_up_btn._command = lambda: switch_window(sign_up.window)

    sign_up.sign_up_btn._command = signup
    sign_up.login_btn._command = lambda: switch_window(login.window)

    main.employees_btn._command = lambda: switch_window(employees.window)
    main.passports_btn._command = lambda: switch_window(passports.window)
    main.exit_btn._command = logout

    passports.add_button._command = lambda: switch_window(add_passport.window)
    passports.delete_button._command = show_delete_passport
    passports.back_button._command = lambda: switch_window(main.window)

    employees.add_button._command = lambda: switch_window(add_employee.window)
    employees.delete_button._command = show_delete_employee
    employees.back_button._command = lambda: switch_window(main.window)

    add_employee.back_btn._command = lambda: switch_window(employees.window)
    add_employee.add_btn._command = add_employee_click

    add_passport.back_btn._command = lambda: switch_window(passports.window)
    add_passport.add_btn._command = add_passport_click

    session = _SESSION(None)
    switch_window(login.window)
