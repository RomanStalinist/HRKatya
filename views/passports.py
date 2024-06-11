import db.db
import tkinter as t
import customtkinter as ct
from CTkTable import CTkTable

window = ct.CTk()
window.title('Паспорта')
window.geometry('1200x800')
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure((0, 1), weight=1)
sqlite = db.db.prepare()

frame = ct.CTkFrame(master=window, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=t.CENTER)

add_button = ct.CTkButton(master=frame, text='Добавить')
add_button.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='nsew')

delete_button = ct.CTkButton(master=frame, text='Удалить')
delete_button.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='nsew')

back_button = ct.CTkButton(master=frame, text='Назад')
back_button.grid(row=1, column=2, padx=20, pady=(0, 20), sticky='nsew')

passports_data = sqlite.query(table='Паспорта')
headers = ['Код', 'Серия', 'Номер', 'ФИО', 'Пол', 'Дата Рождения', 'Место Рождения']
passports = [headers] + passports_data

table = CTkTable(master=frame, row=len(passports), column=7, values=passports)
table.grid(row=0, column=0, columnspan=3, padx=20, pady=20, sticky='nsew')

if __name__ == '__main__':
    window.mainloop()
