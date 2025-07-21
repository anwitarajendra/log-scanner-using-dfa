# 🛡️ Pattern-based Intrusion Detection System using Finite Automata

This is a simple web-based Intrusion Detection System (IDS) built using **Streamlit** and **Python**. It scans log files for suspicious patterns using both **Deterministic Finite Automata (DFA)** and **Regex-based scanning**.

---

## 🚀 Features

- ✅ DFA-based detection of repeated login failures (e.g., 3 consecutive `login failed`)
- ✅ Regex detection of:
  - Unauthorized Access attempts
  - SQL Injection patterns (e.g., `SELECT * FROM ...`)
  - Suspicious IP activity (`192.168.1.X`)
- ✅ Web interface built with Streamlit
- ✅ Works with raw log file text input
- ✅ Deployable on Streamlit Community Cloud, Replit, or locally

---

## 🔧 Technologies Used

- Python 3.x
- Streamlit
- Regular Expressions (`re`)
- DFA logic implemented in Python
- Pyngrok (optional, for localhost tunneling)

---

## 💻 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/dfa-streamlit.git
cd dfa-streamlit
