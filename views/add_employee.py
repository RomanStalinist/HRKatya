import data.db
import tkinter as t
import tkcalendar as tc
import customtkinter as ct

window = ct.CTk()
window.geometry('600x600')
sqlite = data.db.prepare()
window.title('Добавить работника')
window.grid_rowconfigure((0, 3), weight=1)
window.grid_columnconfigure((0, 1), weight=1)

frame = ct.CTkFrame(master=window, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=t.CENTER)

education_entry = ct.CTkComboBox(master=frame, values=[
    'Дошкольное',
    'Начальное',
    'Основное',
    'Среднее общее',
    'Среднее профессиональное',
    'Высшее'
])
education_entry.set('Образование')
education_entry.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

job_entry = ct.CTkEntry(master=frame, placeholder_text='Должность')
job_entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='nsew')

profession_entry = ct.CTkEntry(master=frame, placeholder_text='Профессия')
profession_entry.grid(row=2, column=0, padx=20, pady=(0, 20), sticky='nsew')

department_entry = ct.CTkEntry(master=frame, placeholder_text='Подразделение')
department_entry.grid(row=3, column=0, padx=20, pady=(0, 20), sticky='nsew')

enrollment_date_entry = ct.CTkEntry(master=frame, placeholder_text='Дата поступления')
enrollment_date_entry.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

salary_entry = ct.CTkEntry(master=frame, placeholder_text='Оклад')
salary_entry.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='nsew')

password_ids = sqlite.query(table='Паспорта', columns=('Код', ))
password_ids = [str(item[0]) for item in password_ids]

passport_combobox = ct.CTkComboBox(master=frame, values=password_ids)
passport_combobox.set('Код паспорта')
passport_combobox.grid(row=2, column=1, padx=20, pady=(0, 20), sticky='nsew')

add_btn = ct.CTkButton(master=frame, text='Добавить')
add_btn.grid(row=4, column=0, padx=20, pady=(0, 20), sticky='nsew')

back_btn = ct.CTkButton(master=frame, text='Назад')
back_btn.grid(row=4, column=1, padx=20, pady=(0, 20), sticky='nsew')

if __name__ == '__main__':
    window.mainloop()
