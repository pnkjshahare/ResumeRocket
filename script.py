import re
import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
from datetime import datetime
from config import (
    SENDER_EMAIL,
    SENDER_PASSWORD,
    GMAIL_ACCOUNT_NAME,
    RESUME_PATH,
    RECIPIENTS_FILE,
    LOG_FILE,
    SUBJECT_FILE,
    BODY_FILE
)

# --- Load Subject and Email Body ---
try:
    with open(SUBJECT_FILE, "r", encoding="utf-8") as f:
        subject = f.read().strip()
except Exception as e:
    print(f"❌ Error reading subject file: {e}")
    exit()

try:
    with open(BODY_FILE, "r", encoding="utf-8") as f:
        email_body = f.read()
except Exception as e:
    print(f"❌ Error reading email body file: {e}")
    exit()

# --- Load & Clean Recipients ---
try:
    recipients = pd.read_excel(RECIPIENTS_FILE)
    recipients = recipients[recipients['email'].notna()]
    recipients = recipients[recipients['email'].astype(str).str.strip() != '']
except Exception as e:
    print(f"❌ Error reading or cleaning recipients file: {e}")
    exit()

# --- Setup SMTP ---
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(SENDER_EMAIL, SENDER_PASSWORD)

# --- Regex for email validation ---
email_pattern = re.compile(r"[^@]+@[^@]+\.[^@]+")

# --- Initialize Log ---
log_data = []
sent_count = 0
total_count = len(recipients)

# --- Process Each Recipient ---
for idx, row in recipients.iterrows():
    serial_no = idx + 1
    receiver_email = str(row.get('email')).strip()

    if not receiver_email or not email_pattern.fullmatch(receiver_email):
        print(f"{serial_no}/{total_count} ⚠️ Skipping invalid email: {receiver_email}")
        log_data.append([serial_no, receiver_email, "Invalid Format", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
        continue

    # Create Email
    msg = MIMEMultipart()
    msg['From'] = GMAIL_ACCOUNT_NAME
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(email_body, 'html'))

    # Attach Resume
    try:
        with open(RESUME_PATH, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(RESUME_PATH)}')
            msg.attach(part)
    except Exception as e:
        print(f"{serial_no}/{total_count} ❌ Error attaching resume: {receiver_email} | {e}")
        log_data.append([serial_no, receiver_email, f"Attachment Error: {e}", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
        continue

    # Send Email
    try:
        server.send_message(msg)
        sent_count += 1
        print(f"{serial_no}/{total_count} ✅ Email sent to {receiver_email} ({sent_count} total sent)")
        log_data.append([serial_no, receiver_email, "Sent", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
    except smtplib.SMTPRecipientsRefused:
        print(f"{serial_no}/{total_count} ❌ Address refused: {receiver_email}")
        log_data.append([serial_no, receiver_email, "Refused", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])
    except Exception as e:
        print(f"{serial_no}/{total_count} ❌ Failed to send to {receiver_email}: {e}")
        log_data.append([serial_no, receiver_email, f"Error: {e}", datetime.now().strftime("%d-%m-%Y %H:%M:%S")])

# --- Save Log ---
df_log = pd.DataFrame(log_data, columns=["S.No.", "Email", "Status", "Timestamp"])
if os.path.exists(LOG_FILE):
    try:
        existing_log = pd.read_csv(LOG_FILE)
        combined_log = pd.concat([existing_log, df_log], ignore_index=True)
    except Exception as e:
        print(f"⚠️ Failed to read existing log. Creating new one: {e}")
        combined_log = df_log
else:
    combined_log = df_log

try:
    combined_log.to_csv(LOG_FILE, index=False)
    print(f"\n📄 Log saved to '{LOG_FILE}'")
except Exception as e:
    print(f"❌ Failed to save log: {e}")

# --- Close Server ---
server.quit()
print(f"✅ Total emails successfully sent: {sent_count}/{total_count}")
