import time
import psutil
import threading
import sys
import socket

from tools.banner import show_banner

running = True

def listen_quit():
    global running
    while True:
        key = input().strip().lower()
        if key == "q":
            running = False
            print("\nExiting Domain Mode...\n")
            return

def resolve_domain(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "-"

def domain_mode():
    global running

    print("DOMAIN MODE — Fast Domain Resolver")
    print("Press Q anytime to quit.\n")

    t = threading.Thread(target=listen_quit, daemon=True)
    t.start()

    while running:
        print("\nActive Connections (Auto-refresh 1s)\n")
        print("PID    IP                 DOMAIN                       STATUS")
        print("----------------------------------------------------------------------")

        try:
            for c in psutil.net_connections(kind="inet"):
                if not running:
                    break

                if not c.raddr:
                    continue

                pid = c.pid if c.pid else "-"
                ip = c.raddr.ip
                status = c.status
                domain = resolve_domain(ip)

                print(f"{str(pid):6} {ip:18} {domain[:27]:27} {status}")

        except Exception as e:
            print("[ERROR]", e)

        time.sleep(1)

    sys.exit(0)


if __name__ == "__main__":
    domain_mode()
