# 🛡️ Phishing Simulation Toolkit by Gitesh

**⚠️ Educational Use Only — For Cybersecurity Training & Awareness**

This CLI-based phishing simulation tool helps ethical hackers and security trainers demonstrate how phishing attacks are conducted, including:

- Cloning real websites
- Capturing credentials in a sandbox
- Exposing the site using Ngrok (or LAN/IP)
- Raising awareness about **URL spoofing & fake login pages**

---

## 📦 Features

- 📄 Clone websites with **HTTrack**
- 🐍 Serve fake login page using **Flask**
- 🔐 Capture submitted usernames/passwords
- 🌐 Share phishing site over the internet using **Ngrok**
- 🧪 View logs, clear logs, and manage everything with a **CLI**

---

## ⚠️ Warning About Fake Domains

This toolkit simulates phishing scenarios where attackers use fake or lookalike domains such as:

- `faceb00k.com`
- `facebook-login.verify.page`
- `facebook.com.signin-security.info`

These are **not real Facebook domains**, and are used for **educational purposes only** to help users identify phishing attempts.

---

## 🚨 Disclaimer

> This software is intended **only for educational, research, and ethical hacking purposes** within authorized environments like CTFs, labs, or training sessions.

- ❌ **Do not** use it to deceive, impersonate, or collect real credentials
- ✅ Always get **written permission** before simulating phishing attacks on others
- ⚖️ You are solely responsible for how you use this software

---

## 🛠️ Getting Started

```bash
git clone https://github.com/kakashi145/phish-toolkit.git
cd phish-toolkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 main.py
