import tkinter as tk
from db import init_db
from ui import MailApp

if __name__ == "__main__":
    init_db()
    root = tk.Tk()
    app = MailApp(root)
    root.mainloop()