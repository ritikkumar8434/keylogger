# keylogger
# 🛡️ Keylogger with Email Reporting (Python)

A simple Python-based keylogger designed for academic use that captures keystrokes and automatically sends the log file via email after a certain threshold is reached.

> ⚠️ **Disclaimer**: This project is intended for **educational purposes only**. Unauthorized use of keyloggers is unethical and **illegal**. Do **not** use this code for any malicious or unauthorized monitoring.

---

## 📌 Features

- ⌨️ Captures keyboard input using the `pynput` library
- 🗂️ Logs keystrokes to a file (`data.txt`)
- 📧 Sends keystroke logs to a configured email after every 50 key entries
- 🔄 Automatically restarts logging after sending
- 💡 Demonstrates basic file I/O, threading, and email automation in Python

---

## 📁 Project Structure

keylogger-project/ │ ├── keylogger.py # Main script to log keys and trigger email ├── send_mail.py # Sends logged keys as an email attachment ├── data.txt # Temporary log file storing captured keys

---

## 🚀 How It Works

1. The `keylogger.py` script listens to keyboard input.
2. Each keystroke is saved in `data.txt`.
3. Once 50+ keystrokes are recorded:
   - The log is encoded and attached to an email.
   - The `send_mail.py` script sends this to the configured recipient.
   - The script then exits or restarts based on logic.

---

## 🛠️ Requirements

- Python 3.x
- `pynput` library

Install dependencies:

```bash
pip install pynput
## ⚙️ Setup & Usage
1.Clone the repository:
git clone https://github.com/your-username/keylogger-project.git
cd keylogger-project
2. Configure email in send_mail.py:

Replace with your Gmail & app password:
sender_email = "your_email@gmail.com"
password = "your_app_password"
receiver_email = "recipient_email@gmail.com"
💡 You must enable 2FA and use an App Password for Gmail.

3. Run the keylogger:
python keylogger.py
📬 Example Email Output
Subject: keys from YOUR_COMPUTER_NAME

Attachment: data.text (containing keystrokes)

🧠 Learning Concepts
Event-driven programming with pynput

File handling and text processing

Secure email automation with smtplib

MIME and email formatting in Python

📄 License
This project is open source and available under the MIT License.

🙋‍♂️ Author
Ritik Kumar
[Unnatideep](https://www.linkedin.com/in/unnati-deep//)
Minor Project | MCA Final Year
Feel free to connect or contribute!


