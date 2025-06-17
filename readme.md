# 🚀 ResumeRocket

**ResumeRocket** is a Python-based automated bulk email sender tool designed for job seekers and recruiters. It sends personalized emails with resume attachments to a list of recipients using Gmail's SMTP service. Ideal for applying to multiple job openings in one go while maintaining professionalism.

---

## 📦 Features

- 🔒 Secure credential management with `.env`
- 📤 Sends emails in **bulk** via Gmail
- 📎 Attaches a resume or any file automatically
- 📧 Loads email body from **HTML file** and subject from **text file**
- 📊 Logs sent emails in a CSV file (`email_log.csv`)
- ✅ Validates email formats
- 📁 Works with `.xlsx` file containing a list of recipients

---

## 🛠️ Project Structure

```
ResumeRocket/
│
├── script.py                    # Main Python script
├── recipients.xlsx              # Excel file with 'email' column
├── Your_Resume.pdf              # Your resume to be attached also change in config file
├── email_subject.txt            # Email subject (plain text)
├── email_body.html              # Email body (HTML format)
├── email_log.csv                # Auto-generated email sending log
├── .env                         # Environment variables (credentials)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. ✅ Prerequisites

- Python 3.7+
- Gmail account with **App Password** enabled
- Basic knowledge of Python and email etiquette

---

### 2. 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/ResumeRocket.git
cd ResumeRocket
```

### 3. 🧪 Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt content:**

```
pandas
python-dotenv
openpyxl
```

### 4. 🔐 Configure Environment Variables

Create a `.env` file in the root directory with the following:

```env
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
GMAIL_ACCOUNT_NAME=Your Name or Gmail ID
```

> **Note:** You must use an App Password if 2FA is enabled on your Gmail.

### 5. 📋 Prepare Recipients List

**Create/Edit `recipients.xlsx`:**

- Open the Excel file in Microsoft Excel, Google Sheets, or LibreOffice Calc
- Ensure there's a column header named `email` (case-sensitive)
- Add recipient email addresses one per row under the `email` column
- Optionally, add `name` and `company` columns for better organization

**Example Excel Structure:**

```
| email                     | name          | company        |
|---------------------------|---------------|----------------|
| hr@techcorp.com          | John Smith    | Tech Corp      |
| recruiter@startup.io     | Sarah Johnson | StartupXYZ     |
| jobs@company.com         | Mike Davis    | Big Company    |
| careers@fintech.com      | Lisa Chen     | FinTech Inc    |
```

**📝 Tips for Recipients List:**

- Double-check email addresses for typos
- Remove duplicate entries
- Test with 2-3 emails first before bulk sending
- Keep a backup of your recipients list

### 6. ✍️ Customize Email Content

Edit the following files:

- `email_subject.txt` — Write your email subject line (keep it professional and clear)
- `email_body.html` — Write your email body in HTML format with proper styling
- `PANKAJ_SHAHARE_RESUME.pdf` — Replace with your actual resume file

**Example Email Subject:**

```
Application for Software Developer Position - [Your Name]
```

**Example Email Body Structure:**

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
      }
      .signature {
        margin-top: 20px;
        font-style: italic;
      }
    </style>
  </head>
  <body>
    <p>Dear Hiring Manager,</p>

    <p>
      I hope this email finds you well. I am writing to express my interest in
      potential opportunities at your organization...
    </p>

    <p>
      I have attached my resume for your review. I would welcome the opportunity
      to discuss how my skills and experience align with your needs.
    </p>

    <p>Thank you for your time and consideration.</p>

    <div class="signature">
      <p>
        Best regards,<br />
        Your Name<br />
        Your Phone Number<br />
        Your Email Address
      </p>
    </div>
  </body>
</html>
```

---

## 🔧 Technical Details

### Architecture Overview

ResumeRocket follows a modular architecture with clear separation of concerns:

- **Email Handler**: Manages SMTP connection and email composition
- **Data Processor**: Handles Excel file reading and email validation
- **Logger**: Tracks email sending status and timestamps
- **Configuration Manager**: Manages environment variables and settings

### Core Technologies

| Technology        | Purpose                           | Version  |
| ----------------- | --------------------------------- | -------- |
| **Python**        | Core programming language         | 3.7+     |
| **smtplib**       | SMTP protocol implementation      | Built-in |
| **pandas**        | Excel file processing             | Latest   |
| **python-dotenv** | Environment variable management   | Latest   |
| **openpyxl**      | Excel file reading engine         | Latest   |
| **email.mime**    | Email composition and attachments | Built-in |

### Key Components

#### 1. SMTP Configuration

```python
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
TLS_ENABLED = True
```

#### 2. Email Validation

- **Regex Pattern**: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}# 🚀 ResumeRocket

**ResumeRocket** is a Python-based automated bulk email sender tool designed for job seekers and recruiters. It sends personalized emails with resume attachments to a list of recipients using Gmail's SMTP service. Ideal for applying to multiple job openings in one go while maintaining professionalism.

---

## 📦 Features

- 🔒 Secure credential management with `.env`
- 📤 Sends emails in **bulk** via Gmail
- 📎 Attaches a resume or any file automatically
- 📧 Loads email body from **HTML file** and subject from **text file**
- 📊 Logs sent emails in a CSV file (`email_log.csv`)
- ✅ Validates email formats
- 📁 Works with `.xlsx` file containing a list of recipients

---

## 🛠️ Project Structure

```
ResumeRocket/
│
├── script.py                    # Main Python script
├── recipients.xlsx              # Excel file with 'email' column
├── PANKAJ_SHAHARE_RESUME.pdf    # Your resume to be attached
├── email_subject.txt            # Email subject (plain text)
├── email_body.html              # Email body (HTML format)
├── email_log.csv                # Auto-generated email sending log
├── .env                         # Environment variables (credentials)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. ✅ Prerequisites

- Python 3.7+
- Gmail account with **App Password** enabled
- Basic knowledge of Python and email etiquette

---

### 2. 📁 Clone the Repository

```bash
git clone https://github.com/yourusername/ResumeRocket.git
cd ResumeRocket
```

### 3. 🧪 Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt content:**

```
pandas
python-dotenv
openpyxl
```

### 4. 🔐 Configure Environment Variables

Create a `.env` file in the root directory with the following:

```env
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
GMAIL_ACCOUNT_NAME=Your Name or Gmail ID
```

> **Note:** You must use an App Password if 2FA is enabled on your Gmail.

### 5. ✍️ Customize Email

Edit:

- `email_subject.txt` — Write your email subject line.
- `email_body.html` — Write your email body in HTML (with proper styling).
- `recipients.xlsx` — Add recipient emails under a column named `email`.
- `PANKAJ_SHAHARE_RESUME.pdf` — Replace with your actual resume file.

- **Validation Method**: Real-time validation before sending
- **Error Handling**: Invalid emails are logged but don't stop the process

#### 3. File Processing

- **Supported Formats**: `.xlsx` (Excel), `.html` (email body), `.txt` (subject)
- **Attachment Support**: PDF, DOC, DOCX, TXT, and other common formats
- **Encoding**: UTF-8 for all text files

#### 4. Security Features

- **Environment Variables**: Sensitive credentials stored in `.env`
- **App Password Support**: Compatible with Gmail 2FA
- **No Credential Logging**: Passwords never written to log files

### Performance Specifications

| Metric                   | Value               | Notes                         |
| ------------------------ | ------------------- | ----------------------------- |
| **Processing Speed**     | ~5-10 emails/minute | Depends on attachment size    |
| **Gmail Daily Limit**    | 500 emails/day      | For regular accounts          |
| **Max Attachment Size**  | 25MB                | Gmail limitation              |
| **Memory Usage**         | ~50-100MB           | For typical resume files      |
| **Supported Recipients** | Unlimited           | Limited by Excel row capacity |

### Error Handling

#### Exception Types

- **SMTP Errors**: Connection timeouts, authentication failures
- **File Errors**: Missing files, corrupted Excel sheets
- **Email Format Errors**: Invalid recipient addresses
- **Attachment Errors**: File size limits, corrupted attachments

#### Logging Levels

```python
ERROR   # Critical failures (SMTP auth, missing files)
WARNING # Invalid emails, large attachments
INFO    # Successful sends, progress updates
DEBUG   # Detailed execution flow
```

### Data Flow

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   recipients    │───▶│   Validation     │───▶│   Email Queue   │
│   .xlsx         │    │   & Processing   │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   .env          │───▶│   Configuration  │    │   SMTP Handler  │◀──┘
│   credentials   │    │   Manager        │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │                        │
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   HTML/TXT      │───▶│   Email          │    │   Log Writer    │◀──┘
│   content       │    │   Composer       │    │   (CSV)         │
└─────────────────┘    └──────────────────┘    └─────────────────┘
```

### API Rate Limits

#### Gmail SMTP Limits

- **Regular Account**: 500 emails/day
- **Google Workspace**: 2000 emails/day
- **Rate**: ~1 email/10 seconds (recommended)
- **Concurrent Connections**: 1 (single-threaded)

### File Structure Requirements

#### Excel File Format

```
| email                    | name (optional) | company (optional) |
|--------------------------|-----------------|-------------------|
| recruiter@company.com    | John Doe        | Tech Corp         |
| hr@startup.com           | Jane Smith      | StartupXYZ        |
```

#### Environment File Template

```env
# Gmail SMTP Configuration
SENDER_EMAIL=your.email@gmail.com
SENDER_PASSWORD=your_16_character_app_password
GMAIL_ACCOUNT_NAME=Your Full Name

# Optional: Custom SMTP Settings
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
```

### Troubleshooting

#### Common Issues & Solutions

| Issue                     | Cause                | Solution                       |
| ------------------------- | -------------------- | ------------------------------ |
| **Authentication Failed** | Wrong app password   | Generate new app password      |
| **File Not Found**        | Incorrect file paths | Check file names and locations |
| **Email Not Sent**        | SMTP timeout         | Check internet connection      |
| **Invalid Email Format**  | Malformed addresses  | Validate Excel data            |
| **Attachment Too Large**  | File > 25MB          | Compress or use cloud links    |

### Future Enhancements

- **Multi-threading**: Parallel email processing
- **Template Engine**: Dynamic email personalization
- **Database Support**: PostgreSQL/MySQL integration
- **Web Interface**: Django/Flask dashboard
- **Scheduling**: Cron job automation
- **Analytics**: Open/click tracking

---

## 🚀 Running the Script

```bash
python script.py
```

You'll see logs in the console, and all results will be stored in `email_log.csv`.

---

## 📊 Email Log

After execution, you'll get a CSV file `email_log.csv` with:

| S.No. | Email             | Status         | Timestamp           |
| ----- | ----------------- | -------------- | ------------------- |
| 1     | example@email.com | Sent           | 17-06-2025 14:22:30 |
| 2     | invalid@email     | Invalid Format | 17-06-2025 14:22:30 |

---

## 🧠 Tips

- Always test with a small batch first.
- Use a professional HTML email body.
- Avoid spamming — Gmail has limits on outgoing emails (about 500/day for regular accounts).

---

## 🛡️ Disclaimer

This tool is for educational/job-seeking purposes only. Spamming or misuse may violate Gmail Terms of Service and result in account suspension.

---

## ✨ Author

**Pankaj Shahare**

🌐 [Portfolio](https://your-portfolio-link.com) • 📧 [Email](mailto:your-email@gmail.com) • 💼 [LinkedIn](https://linkedin.com/in/your-profile) • 🐙 [GitHub](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/ResumeRocket/issues).

---

## ⭐ Show your support

Give a ⭐️ if this project helped you!
