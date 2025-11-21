import time
import psutil
from tools.banner import show_banner

GREEN = "\033[32m"
YELLOW = "\033[33m"
RED = "\033[31m"
CYAN = "\033[36m"
MAGENTA = "\033[35m"
RESET = "\033[0m"


def c(text, color):
    return f"{color}{text}{RESET}"


def print_section(title):
    print()
    print(c("─" * 60, CYAN))
    print(c(f" {title}", MAGENTA))
    print(c("─" * 60, CYAN))


def get_top_cpu(limit=10):
    procs = []
    for p in psutil.process_iter(["pid", "name"]):
        try:
            cpu = p.cpu_percent(interval=0.0)
            procs.append((cpu, p.info["pid"], p.info["name"] or "unknown"))
        except Exception:
            continue

    procs.sort(reverse=True, key=lambda x: x[0])
    return [p for p in procs if p[0] > 0][:limit]


def get_connection_stats():
    ip_count = {}
    open_ports = set()

    try:
        conns = psutil.net_connections(kind="inet")
    except Exception:
        return [], [], []

    for c in conns:
        if c.raddr:
            ip = c.raddr.ip
            ip_count[ip] = ip_count.get(ip, 0) + 1

        if c.status == psutil.CONN_LISTEN and c.laddr:
            open_ports.add(c.laddr.port)

    top_ips = sorted(ip_count.items(), key=lambda x: x[1], reverse=True)[:10]
    repeated = [(ip, cnt) for ip, cnt in top_ips if cnt >= 5]
    open_ports = sorted(open_ports)

    return top_ips, repeated, open_ports


def run_diagnostic():
    show_banner()
    print(c("NETWORK WATCHDOG – DIAGNOSTIC MODE", CYAN))
    print(c(time.strftime("Snapshot at %Y-%m-%d %H:%M:%S"), YELLOW))

    print_section("TOP CPU PROCESSES")
    top_cpu = get_top_cpu()
    if not top_cpu:
        print("No active processes found.")
    else:
        print(f"{'CPU%':>5}  {'PID':>6}  PROCESS")
        print("-" * 40)
        for cpu, pid, name in top_cpu:
            print(f"{cpu:5.1f}  {pid:6}  {name[:30]}")

    print_section("TOP REMOTE IPS BY CONNECTION COUNT")
    top_ips, repeated, open_ports = get_connection_stats()
    if not top_ips:
        print("No active remote connections.")
    else:
        print(f"{'IP':<20} COUNT")
        print("-" * 30)
        for ip, cnt in top_ips:
            print(f"{ip:<20} {cnt}")

    print_section("SUSPICIOUS REPEATED CONNECTIONS (>= 5)")
    if not repeated:
        print(c("None detected. Looks calm.", GREEN))
    else:
        for ip, cnt in repeated:
            print(c(f"[!] {ip} contacted {cnt} times", YELLOW))

    print_section("OPEN LISTENING PORTS (LOCAL)")
    if not open_ports:
        print("No listening ports detected.")
    else:
        ports_str = ", ".join(str(p) for p in open_ports)
        print(f"Open ports: {ports_str}")

    print()
    print(c("Diagnostic snapshot complete.", GREEN))
    print("Press any key to return to menu...")


if __name__ == "__main__":
    run_diagnostic()
