import re
from collections import defaultdict

THRESHOLD = 3

def analyze_log(file_path):
    failed_logins = defaultdict(int)

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "Failed password" in line:
                    ip_match = re.search(r'from (\d+\.\d+\.\d+\.\d+)', line)
                    if ip_match:
                        ip = ip_match.group(1)
                        failed_logins[ip] += 1
    except FileNotFoundError:
        print("Log file not found.")
        return []

    suspicious_ips = [
        (ip, count)
        for ip, count in failed_logins.items()
        if count >= THRESHOLD
    ]

    return suspicious_ips


def print_report(results):
    print("\n=== Security Log Analysis Report ===\n")

    if not results:
        print("No suspicious activity detected.\n")
        return

    print("Suspicious IP Addresses:")
    for ip, count in results:
        print(f"- {ip} | {count} failed login attempts")

    print("\nRecommended Action:")
    print("Consider blocking or monitoring flagged IP addresses.\n")


if __name__ == "__main__":
    results = analyze_log("sample_log.txt")
    print_report(results)