import db.db
import tkinter as tk
import customtkinter as ct


window = ct.CTk()
window.geometry('500x500')
window.title('Регистрация')
sqlite = db.db.prepare()

frame = ct.CTkFrame(master=window, corner_radius=16)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

ct.CTkLabel(master=frame, text='Логин').pack(pady=(10, 5), padx=20)
login_entry = ct.CTkEntry(master=frame, placeholder_text='Ваш логин')
login_entry.pack(padx=20)

ct.CTkLabel(master=frame, text='Пароль').pack(pady=(10, 5), padx=20)
password_entry = ct.CTkEntry(master=frame, placeholder_text='Ваш пароль')
password_entry.configure(show='*')
password_entry.pack(padx=20)

ct.CTkLabel(master=frame, text='Еще раз').pack(pady=(10, 5), padx=20)
repeat_password_entry = ct.CTkEntry(master=frame, placeholder_text='Еще раз')
repeat_password_entry.configure(show='*')
repeat_password_entry.pack(padx=20)

sign_up_btn = ct.CTkButton(master=frame, text='Создать')
sign_up_btn.pack(pady=(15, 5), padx=20)

login_btn = ct.CTkButton(master=frame, text='Войти')
login_btn.pack(pady=5, padx=20)

if __name__ == '__main__':
    window.mainloop()
