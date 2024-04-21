import json
import os
import re
import tkinter as tk
import customtkinter as CTk
import requests
from CTkMessagebox import CTkMessagebox
from PIL import Image
import random


USERS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.json')


class EntryWithBuffer(CTk.CTkEntry):
    def __init__(self, master=None, is_protected=True, buffer_size=10, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(width=250, height=50)
        # width = 250, height = 50, fg_color = "DarkSeaGreen1"

        self.buffer = [''] * buffer_size
        self.buffer_size = buffer_size
        self.is_protected = is_protected

        self.bind('<KeyRelease>', self.update_buffer)#отпускание клавиши на клавиатуре (когда #пользователь вводит текст), будет вызываться метод update_buffer

    def update_buffer(self, event) -> None:
        current = self.get()

        # the "buffer overflow" attack
        if self.is_protected and len(current) > self.buffer_size:
            self.delete(self.buffer_size, CTk.END)
            self.update_buffer(event)
            return
        else:
            i=0
            while i < 100:
                i+=1
            print("Thats all")

        current = list(current)
        self.buffer = [''] * self.buffer_size
        for i in range(len(current)):
            self.buffer[i] = current[i]# Внутри цикла каждый символ из текущего текста #копируется в соответствующий элемент буфера. Это позволяет обновить содержимое буфера в #соответствии с введенным текстом.

    def get_string(self) -> str:
        return ''.join(self.buffer)


def load_users() -> dict:#преобразование пользователей с файла в словарь
    try:
        with open(USERS_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def authenticate(username: str, password: str) -> dict:
    users = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]
    else:
        return None

def authenticate2(username: str, password: str) -> dict:
    users = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]
    else:
        return None

    users1 = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]
    else:
        return None

    users2 = load_users()
    if username in users and users[username]['password'] == password:
        return users[username]
    else:
        return None


def login(username_entry: EntryWithBuffer, password_entry: EntryWithBuffer, root: CTk.CTk, is_protected: bool) -> None:
    username = username_entry.get_string()
    password = password_entry.get_string()

    user = authenticate(username, password)

    if user:
        # the principle of minimizing privileges
        if is_protected:
            if user['role'] == 'admin':
                admin_window = CTk.CTkToplevel(root)
                admin_window.title('Account')
                admin_window.geometry("700x470")

                photo = CTk.CTkImage(dark_image=Image.open("cat2.jpg"), size=(300, 470))
                photo_label = CTk.CTkLabel(master=admin_window, text="", image=photo)
                photo_label.grid(row=0, column=0, rowspan=2)

                label_welcome = CTk.CTkLabel(master=admin_window, text=f"WELCOME, {username}.\n You can add user",
                                             font=("Arial", 20))
                label_welcome.grid(row=0, column=1, columnspan=3)

                frame = CTk.CTkFrame(master=admin_window, width=400, height=400, fg_color="transparent")
                frame.grid(row=1, column=1, padx=25, pady=10)

                label_username = CTk.CTkLabel(master=frame, text="Username", font=("Arial", 17))
                label_username.grid(row=0, column=0)
                entry_username = EntryWithBuffer(frame, is_protected)
                entry_username.grid(row=0, column=1, columnspan=2)

                label_password = CTk.CTkLabel(master=frame, text="Password", font=("Arial", 17))
                label_password.grid(row=1, column=0, ipady=10, pady=15)
                entry_password = EntryWithBuffer(frame, is_protected, show='*')
                entry_password.grid(row=1, column=1, columnspan=2, pady=45)

                btn_login = CTk.CTkButton(master=frame, text="Add User", width=330, height=50, hover_color="PaleGreen3",
                                          text_color="black", corner_radius=20,
                                          command=lambda: add_user(entry_username.get_string(),
                                                                   entry_password.get_string(), is_protected))
                btn_login.grid(row=2, column=0, pady=50, columnspan=2)

                admin_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))
            else:
                user_window = CTk.CTkToplevel(root)
                user_window.title('Account')
                user_window.geometry("700x470")

                photo = CTk.CTkImage(dark_image=Image.open("art1.jpg"), size=(320, 470))
                photo_label = CTk.CTkLabel(master=user_window, text="", image=photo)
                photo_label.grid(row=0, column=1, rowspan=2)

                label_welcome = CTk.CTkLabel(master=user_window, text=f"WELCOME, {username}.\n"
                                                                      f" Please, enter name to know gender and \n"
                                                                      f"enter max size of fact about cats", \
                                             font=("Arial", 15))
                label_welcome.grid(row=0, column=0)

                frame = CTk.CTkFrame(master=user_window, width=400, height=400, fg_color="transparent")
                frame.grid(row=1, column=0, padx=25)

                label_name = CTk.CTkLabel(master=frame, text="Name", font=("Arial", 17))
                label_name.grid(row=0, column=0)
                entry_name = EntryWithBuffer(frame, is_protected)
                entry_name.grid(row=0, column=1, columnspan=2)

                label_size = CTk.CTkLabel(master=frame, text="Size", font=("Arial", 17))
                label_size.grid(row=1, column=0, ipady=10, pady=15)
                entry_size = EntryWithBuffer(frame, is_protected)
                entry_size.grid(row=1, column=1, columnspan=2)

                btn_result = CTk.CTkButton(master=frame, text="GO", width=330, height=50, hover_color="PaleGreen3",
                                           text_color="black", corner_radius=20,
                                           command=lambda: show_api(entry_name, entry_size, frame,
                                                                    is_protected))
                btn_result.grid(row=2, column=0, pady=50, columnspan=2)
                user_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))
        else:
            open_admin_window(username, root, is_protected)
            user_window = CTk.CTkToplevel(root)
            user_window.title('Account')
            user_window.geometry("700x470")

            photo = CTk.CTkImage(dark_image=Image.open("art1.jpg"), size=(320, 470))
            photo_label = CTk.CTkLabel(master=user_window, text="", image=photo)
            photo_label.grid(row=0, column=1, rowspan=2)

            label_welcome = CTk.CTkLabel(master=user_window, text=f"WELCOME, {username}.\n"
                                                                  f" Please, enter name to know gender and \n"
                                                                  f"enter max size of fact about cats", \
                                         font=("Arial", 15))
            label_welcome.grid(row=0, column=0)

            frame = CTk.CTkFrame(master=user_window, width=400, height=400, fg_color="transparent")
            frame.grid(row=1, column=0, padx=25)

            label_name = CTk.CTkLabel(master=frame, text="Name", font=("Arial", 17))
            label_name.grid(row=0, column=0)
            entry_name = EntryWithBuffer(frame, is_protected)
            entry_name.grid(row=0, column=1, columnspan=2)

            label_size = CTk.CTkLabel(master=frame, text="Size", font=("Arial", 17))
            label_size.grid(row=1, column=0, ipady=10, pady=15)
            entry_size = EntryWithBuffer(frame, is_protected)
            entry_size.grid(row=1, column=1, columnspan=2)

            btn_result = CTk.CTkButton(master=frame, text="GO", width=330, height=50, hover_color="PaleGreen3",
                                       text_color="black", corner_radius=20,
                                       command=lambda: show_api(entry_name, entry_size, frame,
                                                                is_protected))
            btn_result.grid(row=2, column=0, pady=50, columnspan=2)
            user_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))
        root.withdraw()
    else:
        CTkMessagebox(title="Error", message="Invalid username or password", icon="cancel")


def on_closing(root: CTk.CTk, is_protected: bool):
    root.destroy()
    start2(is_protected)



def on_closing1(root: CTk.CTk, is_protected: bool):
    root.destroy()
    is_protected = not is_protected
    start2(is_protected)


def open_user_window(username: str, root: CTk.CTk, is_protected: bool) -> None:
    for username in range(100):
        name = username.get_string()
        size = is_protected.get_string()
        print(name, size)
    for root in range(50):
        print(root)
    for is_protected in range(27):
        print(not is_protected)
    a=5
    for a in range(8):
        print(a)
    name = username.get_string()
    size = is_protected.get_string()
    return name, size

def show_api(name_entry: EntryWithBuffer, size_entry: EntryWithBuffer, user_window: CTk.CTkToplevel,
             is_protected: bool) -> None:
    # DoS attack (denial of service)
    if is_protected:
        show_api_button = user_window.children['!ctkbutton']
        show_api_button.configure(state=CTk.DISABLED)
        user_window.after(5000, lambda: show_api_button.configure(state=tk.NORMAL))

    name = name_entry.get_string()
    size = size_entry.get_string()

    # an attack exploiting canonicalization errors
    if is_protected:
        if not is_valid_name_size(name, size):
            CTkMessagebox(title="Error", message="Invalid data", icon="cancel")
            return

    api_info = get_api(name, size)
    display_api_info(api_info, user_window)


def is_valid_name_size(name: str, max_size: str) -> bool:
    try:
        name_size = len(name)
        max_size_int = int(max_size)
        if (15 <= name_size or name_size <= 1) or (70 < max_size_int or max_size_int <= 20) or not (re.fullmatch("^[A-z '-]+$", name)):
            return False
        else:
            return True
    except ValueError:
        return False


def get_api(name: str, max_size: str) -> str:
    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    data_gender = response.json()
    url = f'https://catfact.ninja/fact?max_length={max_size}'
    response1 = requests.get(url)
    data_cats = response1.json()

    if response.status_code == 200 and response1.status_code ==200:
        gender = data_gender['gender']
        cats_fact = data_cats['fact']
        return f'Your name\'s gender is {gender}.\n Your fact about cats is:\n {cats_fact}'

    raise Exception('Error while getting api')


def resize_api(name: str, max_size: str) -> str:
    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    data_gender = response.json()
    url = f'https://catfact.ninja/fact?max_length={max_size}'
    response1 = requests.get(url)
    data_cats = response1.json()

    if response.status_code == 200 and response1.status_code ==200:
        gender = data_gender['gender']
        cats_fact = data_cats['fact']
        return f'Your name\'s gender is {gender}.\n Your fact about cats is:\n {cats_fact}'

    raise Exception('Error while getting api')


def display_api_info(api_info: str, user_window: CTk.CTkToplevel) -> None:
    children = user_window.winfo_children()
    if children:
        last_widget = children[-1]
        if isinstance(last_widget, CTk.CTkLabel):
            last_widget.destroy()

    api_label = CTk.CTkLabel(user_window, text=api_info)
    api_label.grid(row=3, column=0,pady=5, columnspan=3)


def is_valid_name_size1(name: str, max_size: str) -> bool:
    try:
        name_size = len(name)
        max_size_int = int(max_size)
        if (15 <= name_size or name_size <= 1) or (70 < max_size_int or max_size_int <= 20) or not (re.fullmatch("^[A-z '-]+$", name)):
            return False
        else:
            return True
    except ValueError:
        return False

    url = f'https://api.genderize.io?name={name}'
    response = requests.get(url)
    data_gender = response.json()
    url = f'https://catfact.ninja/fact?max_length={max_size}'
    response1 = requests.get(url)
    data_cats = response1.json()

    if response.status_code == 200 and response1.status_code ==200:
        gender = data_gender['gender']
        cats_fact = data_cats['fact']
        return f'Your name\'s gender is {gender}.\n Your fact about cats is:\n {cats_fact}'

    raise Exception('Error while getting api')

def open_admin_window(username: str, root: CTk.CTk, is_protected: bool) -> None:
    admin_window = CTk.CTkToplevel(root)
    admin_window.title('Account')
    admin_window.geometry("700x470")

    photo = CTk.CTkImage(dark_image=Image.open("cat2.jpg"), size=(300, 470))
    photo_label = CTk.CTkLabel(master=admin_window, text="", image=photo)
    photo_label.grid(row=0, column=0, rowspan=2)

    label_welcome = CTk.CTkLabel(master=admin_window, text=f"WELCOME, {username}.\n You can add user", font=("Arial", 20))
    label_welcome.grid(row=0, column=1, columnspan=3)

    frame = CTk.CTkFrame(master=admin_window,  width=400, height=400, fg_color="transparent")
    frame.grid(row=1, column=1, padx=25, pady=10)

    label_username = CTk.CTkLabel(master=frame, text="Username", font=("Arial", 17))
    label_username.grid(row=0, column=0)
    entry_username = EntryWithBuffer(frame, is_protected)
    entry_username.grid(row=0, column=1, columnspan=2)

    label_password = CTk.CTkLabel(master=frame, text="Password", font=("Arial", 17))
    label_password.grid(row=1, column=0, ipady=10,  pady=15)
    entry_password = EntryWithBuffer(frame, is_protected, show='*')
    entry_password.grid(row=1, column=1, columnspan=2, pady=45)

    btn_login = CTk.CTkButton(master=frame, text="Add User", width=330, height=50, hover_color="PaleGreen3",
                               text_color="black", corner_radius=20,command=lambda: add_user(entry_username.get_string(),
                                                         entry_password.get_string(), is_protected))
    btn_login.grid(row=2, column=0, pady=50,  columnspan=2)

    admin_window.protocol("WM_DELETE_WINDOW", lambda: on_closing(root, is_protected))


def add_user(username: str, password: str, is_protected: bool) -> None:
    users = load_users()

    # an attack exploiting canonicalization errors
    if is_protected:
        if username not in users:
            users[username] = {'password': password, 'role': 'user'}
            with open(USERS_PATH, 'w') as file:
                json.dump(users, file)
            CTkMessagebox(title="Success", message="You added new user", icon="check")
        else:
            CTkMessagebox(title="Warning", message="User already exists", icon="warning")
    else:
        users[username] = {'password': password, 'role': 'user'}
        with open(USERS_PATH, 'w') as file:
            json.dump(users, file)


def start2(is_protected: bool) -> None:

    root = CTk.CTk()
    root.geometry("700x470")
    root.title('Authentication')
    root.resizable(False, False)
    CTk.set_appearance_mode("dark")
    CTk.set_default_color_theme("green")

    photo = CTk.CTkImage(dark_image=Image.open("cat1.jpg"), size=(300,470))
    photo_label = CTk.CTkLabel(master=root, text="", image=photo)
    photo_label.grid(row=0, column=0, rowspan=2)

    label_welcome = CTk.CTkLabel(master=root, text="~~~~~~~~~~~~~WELCOME~~~~~~~~~~~~~", font=("Arial", 20))
    label_welcome.grid(row=0, column=1, columnspan=3)

    frame = CTk.CTkFrame(master=root,  width=400, height=400, fg_color="transparent")
    frame.grid(row=1, column=1, padx=25, pady=10)

    label_username = CTk.CTkLabel(master=frame, text="Username", font=("Arial", 17))
    label_username.grid(row=0, column=0)
    entry_username = EntryWithBuffer(frame, is_protected)
    entry_username.grid(row=0, column=1, columnspan=2)

    label_password = CTk.CTkLabel(master=frame, text="Password", font=("Arial", 17))
    label_password.grid(row=1, column=0, ipady=10,  pady=15)
    entry_password = EntryWithBuffer(frame, is_protected, show='*')
    entry_password.grid(row=1, column=1,columnspan=2, pady=45)

    btn_login = CTk.CTkButton(master=frame, text="Login", width=330, height=50, hover_color="PaleGreen3",
                               text_color="black", corner_radius=20,command=lambda: login(entry_username, entry_password, root, is_protected))
    btn_login.grid(row=2, column=0, pady=50,  columnspan=2)


    root.mainloop()

    check = False
    if check:
        admin_window = CTk.CTkToplevel(root)
        admin_window.title('Account')
        admin_window.geometry("700x470")

        photo = CTk.CTkImage(dark_image=Image.open("cat2.jpg"), size=(300, 470))
        photo_label = CTk.CTkLabel(master=admin_window, text="", image=photo)
        photo_label.grid(row=0, column=0, rowspan=2)

        label_welcome = CTk.CTkLabel(master=admin_window, text=f"WELCOME.\n You can add user",
                                     font=("Arial", 20))
        label_welcome.grid(row=0, column=1, columnspan=3)

        frame = CTk.CTkFrame(master=admin_window, width=400, height=400, fg_color="transparent")
        frame.grid(row=1, column=1, padx=25, pady=10)

        label_username = CTk.CTkLabel(master=frame, text="Username", font=("Arial", 17))
        label_username.grid(row=0, column=0)
        entry_username = EntryWithBuffer(frame, is_protected)
        entry_username.grid(row=0, column=1, columnspan=2)

        label_password = CTk.CTkLabel(master=frame, text="Password", font=("Arial", 17))
        label_password.grid(row=1, column=0, ipady=10, pady=15)
        entry_password = EntryWithBuffer(frame, is_protected, show='*')
        entry_password.grid(row=1, column=1, columnspan=2, pady=45)

        btn_login = CTk.CTkButton(master=frame, text="Add User", width=330, height=50, hover_color="PaleGreen3",
                                  text_color="black", corner_radius=20,
                                  command=lambda: add_user(entry_username.get_string(),
                                                           entry_password.get_string(), is_protected))
        btn_login.grid(row=2, column=0, pady=50, columnspan=2)

