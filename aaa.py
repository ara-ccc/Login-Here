import tkinter as tk

username = "admin"
password = "wahaha10"

def on_login_click():
    global username, password
    in_username = username_entry.get()
    in_password = password_entry.get()

    if in_username == username and in_password == password:
        result_label.config(text="LOG IN SUCCESSFUL", fg="green")
    else:
        result_label.config(text="LOG IN FAILED. CHECK YOUR USERNAME AND PASSWORD", fg="red")

window = tk.Tk()
window.title("Login Widget - Tkinter")

username_label = tk.Label(window, text="Username:")
username_label.pack(pady=5)

username_entry = tk.Entry(window)
username_entry.pack(pady=5)

password_label = tk.Label(window, text="Password:")
password_label.pack(pady=5)

password_entry = tk.Entry(window, show="*")
password_entry.pack(pady=5)

login_button = tk.Button(window, text="Login", command=on_login_click)
login_button.pack(pady=10)

result_label = tk.Label(window, text="")
result_label.pack(pady=10)

window.mainloop()
