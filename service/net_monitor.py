import time
import psutil
import threading
import sys

from service.logger import log_info, log_warning, log_danger
from service.notifier import notify
from tools.banner import show_banner


SCAN_INTERVAL = 1

DANGER_PREFIX = [
    "5.", "31.", "37.", "45.", "77.", "78.", "79.", "80.",
    "81.", "82.", "83.", "84.", "85.", "86.",
    "91.", "92.", "93.", "94.", "95."
]

WARNING_PREFIX = [
    "101.", "103.", "110.", "111.", "112.", "113."
]

PROCESS_CACHE = {}

running = True  


def listen_quit():
    global running
    while True:
        key = input().strip().lower()
        if key == "q":
            running = False
            print("\nExiting Network Watchdog...\n")
            return


def color(text, code):
    return f"\033[{code}m{text}\033[0m"


GREEN = "32"
YELLOW = "33"
RED = "31"


def marker(status):
    return color("●", GREEN) if status == "ESTABLISHED" else color("●", YELLOW)


def get_process_name(pid):
    if pid in PROCESS_CACHE:
        return PROCESS_CACHE[pid]
    try:
        name = psutil.Process(pid).name()
    except:
        name = "unknown"
    PROCESS_CACHE[pid] = name
    return name


def classify(ip):
    if ip.startswith("127.") or ip.startswith("::1"):
        return "AMAN", None
    for p in DANGER_PREFIX:
        if ip.startswith(p):
            return "DANGER", f"IP region risiko tinggi ({p}*)"
    for p in WARNING_PREFIX:
        if ip.startswith(p):
            return "WARNING", f"IP prefix tidak umum ({p}*)"
    return "AMAN", None


def monitor_network_loop():
    global running

    print("Press Q anytime to quit.\n")
    log_info("Network Watchdog Log Mode started.")
    notify("Network Watchdog", "Log Mode Active")

    t = threading.Thread(target=listen_quit, daemon=True)
    t.start()

    print("\n=== NETWORK WATCHDOG LOG MODE (LIVE LOG, NO CLEAR) ===\n")

    while running:
        try:
            for c in psutil.net_connections(kind="inet"):
                if not running:
                    break

                if not c.raddr:
                    continue

                pid = str(c.pid) if c.pid else "-"
                pname = get_process_name(c.pid)
                ip = c.raddr.ip
                status = c.status

                level, reason = classify(ip)

                color_code = (
                    GREEN if level == "AMAN"
                    else YELLOW if level == "WARNING"
                    else RED
                )

                print(
                    f"{pid:6}  "
                    f"{pname[:18]:18}  "
                    f"{ip:18}  "
                    f"{marker(status)}  "
                    f"{color(level, color_code)}"
                )

                if level == "DANGER":
                    log_danger(f"{ip} → {reason}")
                    notify("NW - DANGER", f"{ip} → {reason}")

                elif level == "WARNING":
                    log_warning(f"{ip} → {reason}")

            time.sleep(SCAN_INTERVAL)

        except Exception as e:
            print("[ERROR]", e)

    sys.exit(0) 