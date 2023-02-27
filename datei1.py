import tkinter as tk
from py import *

class LoginScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Login")
        self.parent.configure(bg='red')
        self.parent.attributes('-fullscreen', True)

        header_image = tk.PhotoImage(file="logo.png")
        header_label = tk.Label(self, image=header_image)
        header_label.image = header_image
        header_label.pack(pady=50)

        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=10)

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.pack()

    def login(self):
        if check_if_user_exists(self.username_entry.get()):
            self.destroy()
            MainScreen(self.parent)

class MainScreen(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.parent.title("Main Screen")
        self.parent.configure(bg='red')
        self.parent.attributes('-fullscreen', True)

        header_image = tk.PhotoImage(file="logo.png")
        header_label = tk.Label(self, image=header_image)
        header_label.image = header_image
        header_label.pack(pady=50)

        button_frame = tk.Frame(self)
        button_frame.pack(expand=True)

        button_1 = tk.Button(button_frame, text="Button 1")
        button_1.pack(side="left", padx=50, pady=50)

        button_2 = tk.Button(button_frame, text="Button 2")
        button_2.pack(side="left", padx=50, pady=50)

        button_3 = tk.Button(button_frame, text="Button 3")
        button_3.pack(side="left", padx=50, pady=50)

        button_4 = tk.Button(button_frame, text="Button 4")
        button_4.pack(side="left", padx=50, pady=50)

if __name__ == "__main__":
    root = tk.Tk()
    login_screen = LoginScreen(root)
    login_screen.pack(expand=True, fill="both")
    root.mainloop()
