# 🚀 AI-Assisted Log Analyzer (SOC Simulation)

An AI-inspired security log analyzer that detects brute-force login attempts, assigns risk levels, and generates actionable security recommendations.

---

## 📌 Overview

This project simulates a **Security Operations Center (SOC) log analysis workflow** using Python.

It demonstrates how modern security systems can:

- Detect brute-force login attempts  
- Analyze authentication logs  
- Assign **risk levels (LOW / MEDIUM / HIGH)**  
- Generate automated investigation reports  

---

## ⚠️ Problem

Brute-force attacks are a common cybersecurity threat where attackers repeatedly attempt to guess user credentials.

Manual log analysis is:

- Time-consuming  
- Error-prone  
- Not scalable  

---

## 💡 Solution

This Python-based analyzer automates detection by:

- Parsing SSH authentication logs  
- Extracting IP addresses using regex  
- Counting failed login attempts  
- Assigning **risk levels based on behavior**
- Generating a structured **security report**

---

## 🧠 Detection Logic

| Failed Attempts | Risk Level |
|---------------|-----------|
| ≥ 3           | 🔴 HIGH   |
| ≥ 2           | 🟠 MEDIUM |
| < 2           | 🟢 LOW    |

---

## 🧪 Example Output

IP Address: 192.168.1.10
Failed Attempts: 3
Risk Level: HIGH
Recommendation: Block or investigate this IP immediately

IP Address: 10.0.0.5
Failed Attempts: 2
Risk Level: MEDIUM
Recommendation: Monitor this IP for additional failed attempts

<img width="1271" height="1240" alt="image" src="https://github.com/user-attachments/assets/05a45415-fea8-4f5a-92ed-3d40de4be627" />


---

## 📸 Execution Output

<img width="1271" height="1240" alt="image" src="https://github.com/user-attachments/assets/e6e11521-a4e7-424f-b1d2-f533af1dd2c6" />

---

## ⚙️ How to Run

```bash
git clone https://github.com/Dipan-Khatri/AI-Assisted-Log-Analyzer.git
cd AI-Assisted-Log-Analyzer
python analyzer.py

---

## 🏢 Real-World Application

This type of detection logic is used in:

- SIEM platforms (Splunk, ELK)
- SOC environments for threat detection
- Automated security monitoring systems

This project reflects how analysts transition from **raw logs → actionable intelligence**.

## ✅ ADD 1: Sample Log Input (VERY IMPORTANT)

This shows real understanding.

## 🧾 Sample Log Input
Mar 10 10:15:32 server sshd[1024]: Failed password for invalid user admin from 192.168.1.10 port 22 ssh2

Mar 10 10:15:35 server sshd[1025]: Failed password for invalid user root from 192.168.1.10 port 22 ssh2

Mar 10 10:15:40 server sshd[1026]: Failed password for invalid user guest from 192.168.1.10 port 22 ssh2

Mar 10 10:16:10 server sshd[1030]: Failed password for invalid user test from 10.0.0.5 port 22 ssh2



