import sqlite3

def init_db():
    conn = sqlite3.connect("mail_app.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    email TEXT NOT NULL,
                    smtp_server TEXT NOT NULL,
                    smtp_port INTEGER,
                    password TEXT NOT NULL
                )''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS sent_emails (
                    id INTEGER PRIMARY KEY,
                    sender TEXT,
                    recipient TEXT,
                    subject TEXT,
                    body TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def save_user(email, smtp_server, smtp_port, password):
    conn = sqlite3.connect("mail_app.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO users (email, smtp_server, smtp_port, password) VALUES (?, ?, ?, ?)",
                (email, smtp_server, smtp_port, password))
    conn.commit()
    conn.close()

def save_email(sender, recipient, subject, body):
    conn = sqlite3.connect("mail_app.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO sent_emails (sender, recipient, subject, body) VALUES (?, ?, ?, ?)",
                (sender, recipient, subject, body))
    conn.commit()
    conn.close()