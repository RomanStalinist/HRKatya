import db.db
import tkinter as t
import customtkinter as ct

window = ct.CTk()
window.geometry('500x500')
window.title('Отдел кадров')

frame = ct.CTkFrame(master=window, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=t.CENTER)

name_label = ct.CTkLabel(master=frame, text='user')
name_label.pack(pady=(10, 5), padx=20)

employees_btn = ct.CTkButton(master=frame, text='Работники')
employees_btn.pack(pady=5, padx=20)

passports_btn = ct.CTkButton(master=frame, text='Паспорта')
passports_btn.pack(pady=5, padx=20)

exit_btn = ct.CTkButton(master=frame, text='Выйти')
exit_btn.pack(pady=5, padx=20)

if __name__ == '__main__':
    window.mainloop()
