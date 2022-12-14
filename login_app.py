from tkinter import *
import customtkinter


class Dafney:
    
    def __init__(self):

        customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
        customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

        self.login_app = customtkinter.CTk()
        self.login_app.title("Dafney")
        self.login_app.geometry("400x300")

        self.user = customtkinter.StringVar()
        self.password = customtkinter.StringVar()

    def getEntry_login(self):
        print(self.user.get(),self.password.get())

    def login(self):
        # User
        self.text_1 =  customtkinter.CTkLabel(self.login_app, text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.text_1.pack(pady=(50, 10))

        self.entry_1 = customtkinter.CTkEntry(master=self.login_app, placeholder_text="user",textvariable=self.user)
        self.entry_1.pack(pady=0, padx=10)
        self.entry_1.focus()

        # Password
        self.entry_2 = customtkinter.CTkEntry(master=self.login_app, placeholder_text="password",show="*",textvariable=self.password)
        self.entry_2.pack(pady=5, padx=10)

        self.button_check = customtkinter.CTkButton(master=self.login_app,fg_color="transparent", border_width=2, text_color=("Connexion", "#85C1E9"),text="Connexion",command=self.getEntry_login)
        self.button_check.pack(pady=10, padx=10)

        self.login_app.mainloop()


if __name__ == '__main__':
    app = Dafney()
    app.login()

