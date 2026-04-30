import re
from collections import defaultdict

THRESHOLD_MEDIUM = 2
THRESHOLD_HIGH = 3


def analyze_log(file_path):
    failed_logins = defaultdict(int)
    successful_logins = defaultdict(int)

    try:
        with open(file_path, "r") as file:
            for line in file:
                ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)

                if ip_match:
                    ip = ip_match.group(1)

                    if "Failed password" in line:
                        failed_logins[ip] += 1

                    elif "Accepted password" in line:
                        successful_logins[ip] += 1

    except FileNotFoundError:
        print("Log file not found.")
        return []

    results = []

    for ip, count in failed_logins.items():
        if count >= THRESHOLD_HIGH:
            risk = "HIGH"
            recommendation = "Block or investigate this IP immediately"
        elif count >= THRESHOLD_MEDIUM:
            risk = "MEDIUM"
            recommendation = "Monitor this IP for additional failed attempts"
        else:
            risk = "LOW"
            recommendation = "No immediate action required"

        results.append({
            "ip": ip,
            "failed_attempts": count,
            "successful_logins": successful_logins[ip],
            "risk": risk,
            "recommendation": recommendation
        })

    return results


def print_report(results):
    print("\n=== AI-Assisted Security Log Analysis Report ===\n")

    if not results:
        print("No suspicious activity detected.\n")
        return

    for result in results:
        print(f"IP Address: {result['ip']}")
        print(f"Failed Attempts: {result['failed_attempts']}")
        print(f"Successful Logins: {result['successful_logins']}")
        print(f"Risk Level: {result['risk']}")
        print(f"Recommendation: {result['recommendation']}")
        print("-" * 50)


def save_report(results, output_file="analysis_report.txt"):
    with open(output_file, "w") as report:
        report.write("AI-Assisted Security Log Analysis Report\n")
        report.write("=" * 50 + "\n\n")

        if not results:
            report.write("No suspicious activity detected.\n")
            return

        for result in results:
            report.write(f"IP Address: {result['ip']}\n")
            report.write(f"Failed Attempts: {result['failed_attempts']}\n")
            report.write(f"Successful Logins: {result['successful_logins']}\n")
            report.write(f"Risk Level: {result['risk']}\n")
            report.write(f"Recommendation: {result['recommendation']}\n")
            report.write("-" * 50 + "\n")


if __name__ == "__main__":
    results = analyze_log("sample_log.txt")
    print_report(results)
    save_report(results)
    print("\nReport saved to analysis_report.txt")
