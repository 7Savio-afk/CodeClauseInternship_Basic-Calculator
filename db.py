import sqlite3

def init_db():
    conn = sqlite3.connect('mail_app.db')
    c = conn.cursor()

    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 email TEXT UNIQUE,
                 password TEXT,
                 smtp_server TEXT,
                 smtp_port INTEGER)''')

    # Sent emails table
    c.execute('''CREATE TABLE IF NOT EXISTS sent_emails (
                 id INTEGER PRIMARY KEY,
                 user_email TEXT,
                 to_email TEXT,
                 subject TEXT,
                 body TEXT,
                 sent_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()

def register_user(email, password, smtp_server, smtp_port):
    conn = sqlite3.connect('mail_app.db')
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (email, password, smtp_server, smtp_port) VALUES (?, ?, ?, ?)",
                  (email, password, smtp_server, smtp_port))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_user(email, password):
    conn = sqlite3.connect('mail_app.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = c.fetchone()
    conn.close()
    return user

def store_sent_email(user_email, to_email, subject, body):
    conn = sqlite3.connect('mail_app.db')
    c = conn.cursor()
    c.execute("INSERT INTO sent_emails (user_email, to_email, subject, body) VALUES (?, ?, ?, ?)",
              (user_email, to_email, subject, body))
    conn.commit()
    conn.close()