import requests
import time
from colorama import Fore, Style, init
import signal
import sys

# Initialize colorama for colored output
init(autoreset=True)

# Banner box
def print_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.GREEN + "        AIRDROP SCRIPT FA  (t.me/airdropscriptfa)")
    print(Fore.GREEN + "            Forest Army    (t.me/forestarmy)")
    print(Fore.GREEN + "        YouTube - youtube.com/forestarmy")
    print(Fore.YELLOW + "              CashClipBot - Auto Bot")
    print(Fore.CYAN + "=" * 60)

# HTTP headers
HEADERS = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "en-US,en;q=0.9",
    "connection": "keep-alive",
    "host": "clipapp1.com",
    "sec-ch-ua": '"Microsoft Edge";v="137", "Chromium";v="137", "Not/A)Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "sec-fetch-storage-access": "active",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"
}

request_count = 0

# Graceful exit on Ctrl+C
def signal_handler(sig, frame):
    print(Fore.RED + "\nScript stopped by user.")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# Send request with retries
def send_request(id_value, retries=3):
    global request_count
    url = f"https://clipapp1.com/seen?id={id_value}"
    HEADERS["referer"] = f"https://clipapp1.com/?id={id_value}"
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            request_count += 1
            print(Fore.GREEN + f"Request {request_count} sent for ID: {id_value}")
            return
        except Exception as e:
            print(Fore.RED + f"Error for ID {id_value} (Attempt {attempt}/{retries}): {e}")
            time.sleep(2)
    print(Fore.RED + f"Failed to send request for ID {id_value} after {retries} attempts.")
    time.sleep(2)

# Main execution
def main():
    print_banner()
    try:
        with open("user.txt", "r", encoding="utf-8") as f:
            ids = [line.strip() for line in f if line.strip()]
        
        if not ids:
            print(Fore.RED + "No IDs found in user.txt")
            return

        print(Fore.CYAN + f"Loaded {len(ids)} IDs.")
        print(Fore.YELLOW + "Starting request loop...")

        while True:
            for id_value in ids:
                send_request(id_value)
                time.sleep(1)
            print(Fore.YELLOW + f"Total requests sent so far: {request_count}")

    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()
