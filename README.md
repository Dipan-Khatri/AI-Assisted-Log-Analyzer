# AI-Assisted-Log-Analyzer
AI-assisted security log analyzer that detects brute-force login attempts and flags suspicious IP addresses.
## Overview
This project simulates a Security Operations Center (SOC) log analysis workflow.  
It was developed using AI-assisted coding tools to demonstrate how automation can help detect brute-force login attempts in authentication logs.

## Problem
Brute-force attacks are a common cybersecurity threat where attackers repeatedly attempt to guess user credentials.

Manually reviewing logs is inefficient and error-prone.

## Solution
This Python-based log analyzer:
- Parses SSH authentication logs
- Detects repeated failed login attempts
- Flags suspicious IP addresses
- Generates a simple security report
- Recommends monitoring or blocking flagged IPs

## Technologies Used
- Python
- Regular Expressions (re)
- Collections (defaultdict)
- AI-assisted development workflow

## Sample Detection Logic
Any IP address with **3 or more failed login attempts** is flagged as suspicious.

## Example Output
=== Security Log Analysis Report ===

Suspicious IP Addresses:

192.168.1.10 | 3 failed login attempts---

## How to Run

1. Clone the repository:
2. 2. Navigate into the folder:

3. Run the analyzer:


## Why This Project Matters

This project demonstrates:

- Practical log parsing skills  
- Security threat detection logic  
- Understanding of brute-force attack patterns  
- Clean Python structure  
- Automation mindset aligned with SOC workflows  

---

## Future Improvements

- Add command-line arguments for custom log file input  
- Export flagged IPs to CSV  
- Integrate with firewall APIs for automated blocking  
- Add real-time log monitoring  
- Build a web dashboard  

---

## Author

**Dipan Khatri**  
Cybersecurity Enthusiast | Aspiring SOC Analyst  
GitHub: https://github.com/Dipan-Khatri
