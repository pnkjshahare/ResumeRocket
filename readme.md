# 🚀 ResumeRocket

**ResumeRocket** is a Python-based automated bulk email sender tool designed for job seekers and recruiters. It sends personalized emails with resume attachments to a list of recipients using Gmail's SMTP service. Ideal for applying to multiple job openings in one go while maintaining professionalism.

---

## 📦 Features

* 🔐 Secure credential management with `.env`
* 📤 Sends emails in **bulk** via Gmail
* 📌 Attaches a resume or any file automatically
* 📧 Loads email body from **HTML file** and subject from **text file**
* 📊 Logs sent emails in a CSV file (`email_log.csv`)
* ✅ Validates email formats
* 📁 Works with `.xlsx` file containing a list of recipients

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

* Python 3.7+
* Gmail account with **App Password** enabled
* Basic knowledge of Python and email etiquette

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

* `email_subject.txt` — Write your email subject line.
* `email_body.html` — Write your email body in HTML (with proper styling).
* `recipients.xlsx` — Add recipient emails under a column named `email`.
* `PANKAJ_SHAHARE_RESUME.pdf` — Replace with your actual resume file.

---

## 🔧 Technical Details

### Architecture Overview

ResumeRocket follows a modular architecture with clear separation of concerns:

* **Email Handler**: Manages SMTP connection and email composition
* **Data Processor**: Handles Excel file reading and email validation
* **Logger**: Tracks email sending status and timestamps
* **Configuration Manager**: Manages environment variables and settings

### Core Technologies

| Technology        | Purpose                           | Version  |
| ----------------- | --------------------------------- | -------- |
| **Python**        | Core programming language         | 3.7+     |
| **smtplib**       | SMTP protocol implementation      | Built-in |
| **pandas**        | Excel file processing             | Latest   |
| **python-dotenv** | Environment variable management   | Latest   |
| **openpyxl**      | Excel file reading engine         | Latest   |
| **email.mime**    | Email composition and attachments | Built-in |

---

## 🚀 Running the Script

```bash
python script.py
```

You'll see logs in the console, and all results will be stored in `email_log.csv`.

---

## 📊 Email Log

After execution, you'll get a CSV file `email_log.csv` with:

| S.No. | Email                                         | Status         | Timestamp           |
| ----- | --------------------------------------------- | -------------- | ------------------- |
| 1     | [example@email.com](mailto:example@email.com) | Sent           | 17-06-2025 14:22:30 |
| 2     | invalid\@email                                | Invalid Format | 17-06-2025 14:22:30 |

---

## 🧠 Tips

* Always test with a small batch first.
* Use a professional HTML email body.
* Avoid spamming — Gmail has limits on outgoing emails (about 500/day for regular accounts).

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
