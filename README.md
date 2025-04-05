# keylogger
🛡️ Keylogger with Email Reporting (Python)
This project is a simple Python-based keylogger that logs keystrokes from the user's keyboard and sends them to a specified email address after a set threshold is reached. It is designed as a minor academic project to demonstrate the concepts of system-level event handling, file I/O, and secure email automation.

📌 Features
✅ Captures keyboard input using the pynput library

✅ Logs each keypress to a text file (data.txt)

✅ Sends the logged data as an email attachment when 50+ keys are recorded

✅ Utilizes Python’s smtplib and email modules for email delivery

✅ Automatically restarts logging after sending data

📁 Project Structure
keylogger.py – Core logic for capturing keystrokes and checking the log length

send_mail.py – Handles formatting and sending the email with the log file as an attachment

data.txt – Temporary log file for captured keystrokes

🚀 How It Works
The script monitors keyboard activity.

Each keystroke is saved in a local file.

Once the file contains 50+ keystrokes, the program:

Attaches the log file to an email

Sends it to the pre-configured recipient

Stops the current session

⚠️ Disclaimer
This project is intended for educational purposes only. Unauthorized use of keyloggers is unethical and illegal. Do not use this code for any malicious or unauthorized monitoring.

🔧 Requirements
Python 3.x

pynput (pip install pynput)

🛠️ Setup
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/keylogger-project.git
cd keylogger-project
Install dependencies:

bash
Copy
Edit
pip install pynput
Update the email credentials and recipient in send_mail.py:

python
Copy
Edit
sender_email = "your_email@gmail.com"
password = "your_app_password"
receiver_email = "recipient_email@gmail.com"
Run the script:

bash
Copy
Edit
python keylogger.py
