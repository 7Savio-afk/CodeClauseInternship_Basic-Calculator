import tkinter as tk
from tkinter import messagebox
from db import register_user, get_user, store_sent_email
from email_utils import send_email

class MailApp:
    def _init_(self, master):
        self.master = master
        self.master.title("Mail Application")
        self.show_login()

    def show_login(self):
        self.clear_window()
        tk.Label(self.master, text="Email").pack()
        self.email_entry = tk.Entry(self.master)
        self.email_entry.pack()

        tk.Label(self.master, text="Password").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        tk.Button(self.master, text="Login", command=self.login).pack()
        tk.Button(self.master, text="Register", command=self.show_register).pack()

    def show_register(self):
        self.clear_window()
        tk.Label(self.master, text="Email").pack()
        self.reg_email = tk.Entry(self.master)
        self.reg_email.pack()

        tk.Label(self.master, text="Password").pack()
        self.reg_pass = tk.Entry(self.master, show="*")
        self.reg_pass.pack()

        tk.Label(self.master, text="SMTP Server").pack()
        self.reg_smtp = tk.Entry(self.master)
        self.reg_smtp.pack()

        tk.Label(self.master, text="SMTP Port").pack()
        self.reg_port = tk.Entry(self.master)
        self.reg_port.pack()

        tk.Button(self.master, text="Register", command=self.register).pack()
        tk.Button(self.master, text="Back to Login", command=self.show_login).pack()

    def show_email_sender(self):
        self.clear_window()
        tk.Label(self.master, text="To").pack()
        self.to_entry = tk.Entry(self.master)
        self.to_entry.pack()

        tk.Label(self.master, text="Subject").pack()
        self.sub_entry = tk.Entry(self.master)
        self.sub_entry.pack()

        tk.Label(self.master, text="Body").pack()
        self.body_entry = tk.Text(self.master, height=10)
        self.body_entry.pack()

        tk.Button(self.master, text="Send Email", command=self.send_email_action).pack()

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        user = get_user(email, password)
        if user:
            self.current_user = user
            self.show_email_sender()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    def register(self):
        email = self.reg_email.get()
        password = self.reg_pass.get()
        smtp = self.reg_smtp.get()
        port = int(self.reg_port.get())
        if register_user(email, password, smtp, port):
            messagebox.showinfo("Success", "User Registered")
            self.show_login()
        else:
            messagebox.showerror("Error", "User already exists")

    def send_email_action(self):
        to_email = self.to_entry.get()
        subject = self.sub_entry.get()
        body = self.body_entry.get("1.0", tk.END)
        _, email, password, smtp, port = self.current_user
        success = send_email(smtp, port, email, password, to_email, subject, body)
        if success:
            store_sent_email(email, to_email, subject, body)
            messagebox.showinfo("Success", "Email sent!")
        else:
            messagebox.showerror("Error", "Failed to send email")

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()