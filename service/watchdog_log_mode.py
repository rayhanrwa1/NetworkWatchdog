import time
import psutil
import threading
import sys
from tools.banner import show_banner

running = True

def listen_quit():
    global running
    while True:
        key = input().strip().lower()
        if key == "q":
            running = False
            print("\nExiting Log Mode...\n")
            return

def log_mode():
    global running
    print("LOG MODE — Raw Connection Logger")
    print("Press Q anytime to quit.\n")

    t = threading.Thread(target=listen_quit, daemon=True)
    t.start()

    while running:
        for c in psutil.net_connections(kind="inet"):
            if not running:
                break

            if not c.raddr:
                continue

            pid = c.pid if c.pid else "-"
            ip = c.raddr.ip
            status = c.status

            print(f"{pid:6} {ip:18} {status}")

        time.sleep(1)

    sys.exit(0)

if __name__ == "__main__":
    log_mode()
