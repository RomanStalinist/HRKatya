import db.db
import tkinter as t
import customtkinter as ct

window = ct.CTk()
window.geometry('600x600')
sqlite = db.db.prepare()
window.title('Добавить паспортные данные')
window.grid_rowconfigure((0, 2), weight=1)
window.grid_columnconfigure((0, 1), weight=1)

frame = ct.CTkFrame(master=window, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=t.CENTER)

seria_entry = ct.CTkEntry(master=frame, placeholder_text='Серия')
seria_entry.grid(row=0, column=0, padx=20, pady=20, sticky='nsew')

number_entry = ct.CTkEntry(master=frame, placeholder_text='Номер')
number_entry.grid(row=1, column=0, padx=20, pady=(0, 20), sticky='nsew')

fullname_entry = ct.CTkEntry(master=frame, placeholder_text='ФИО')
fullname_entry.grid(row=2, column=0, padx=20, pady=(0, 20), sticky='nsew')

sex_combobox = ct.CTkComboBox(master=frame, values=['Мужской', 'Женский'])
sex_combobox.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')

dob_entry = ct.CTkEntry(master=frame, placeholder_text='Дата рождения')
dob_entry.grid(row=1, column=1, padx=20, pady=(0, 20), sticky='nsew')

pob_entry = ct.CTkEntry(master=frame, placeholder_text='Место рождения')
pob_entry.grid(row=2, column=1, padx=20, pady=(0, 20), sticky='nsew')

add_btn = ct.CTkButton(master=frame, text='Добавить')
add_btn.grid(row=3, column=0, padx=20, pady=(0, 20), sticky='nsew')

back_btn = ct.CTkButton(master=frame, text='Назад')
back_btn.grid(row=3, column=1, padx=20, pady=(0, 20), sticky='nsew')

if __name__ == '__main__':
    window.mainloop()
