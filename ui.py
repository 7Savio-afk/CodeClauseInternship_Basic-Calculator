import tkinter as tk
from tkinter import messagebox
from db import save_user, save_email, init_db
from mailer import send_email

def launch_ui():
    def save_config():
        save_user(email_entry.get(), server_entry.get(), int(port_entry.get()), password_entry.get())
        messagebox.showinfo("Saved", "Configuration saved successfully")

    def send():
        success, msg = send_email(
            email_entry.get(), password_entry.get(),
            server_entry.get(), int(port_entry.get()),
            to_entry.get(), subject_entry.get(), body_text.get("1.0", tk.END)
        )
        if success:
            save_email(email_entry.get(), to_entry.get(), subject_entry.get(), body_text.get("1.0", tk.END))
            messagebox.showinfo("Success", msg)
        else:
            messagebox.showerror("Error", msg)

    window = tk.Tk()
    window.title("Python Mail App")
    window.geometry("500x600")

    tk.Label(window, text="Email:").pack()
    email_entry = tk.Entry(window, width=50)
    email_entry.pack()

    tk.Label(window, text="Password:").pack()
    password_entry = tk.Entry(window, width=50, show="*")
    password_entry.pack()

    tk.Label(window, text="SMTP Server:").pack()
    server_entry = tk.Entry(window, width=50)
    server_entry.pack()

    tk.Label(window, text="Port:").pack()
    port_entry = tk.Entry(window, width=50)
    port_entry.insert(0, "587")
    port_entry.pack()

    tk.Button(window, text="Save Config", command=save_config).pack(pady=5)

    tk.Label(window, text="To:").pack()
    to_entry = tk.Entry(window, width=50)
    to_entry.pack()

    tk.Label(window, text="Subject:").pack()
    subject_entry = tk.Entry(window, width=50)
    subject_entry.pack()

    tk.Label(window, text="Body:").pack()
    body_text = tk.Text(window, height=10, width=50)
    body_text.pack()

    tk.Button(window, text="Send Email", command=send).pack(pady=10)

    window.mainloop()