import ipaddress

SUSPICIOUS_PORTS_DANGER = {4444, 1337, 3389, 23, 135, 445}
SUSPICIOUS_PORTS_WARNING = {21, 22, 1433, 3306}
SUSPICIOUS_PROCESS_NAME = {"bitcoin-miner.exe", "miner.exe", "rat.exe"}

def classify_connection(proc_name, laddr, raddr, status):
    if not raddr:
        return None

    remote_ip, remote_port = raddr
    local_ip, local_port = laddr if laddr else ("0.0.0.0", 0)

    level = None
    reason = []

    if remote_port in SUSPICIOUS_PORTS_DANGER:
        level = "DANGER"
        reason.append(f"suspicious remote port {remote_port}")
    elif remote_port in SUSPICIOUS_PORTS_WARNING:
        level = level or "WARNING"
        reason.append(f"unusual remote port {remote_port}")

    if proc_name and proc_name.lower() in SUSPICIOUS_PROCESS_NAME:
        level = "DANGER"
        reason.append(f"suspicious process name {proc_name}")

    try:
        ip_obj = ipaddress.ip_address(remote_ip)
        if not ip_obj.is_private:
            pass
    except Exception:
        pass

    if status not in {"ESTABLISHED", "CLOSE_WAIT", "TIME_WAIT"}:
        level = level or "INFO"
        reason.append(f"unusual status {status}")

    if not level or not reason:
        return None

    return level, ", ".join(reason), {
        "proc_name": proc_name,
        "local_ip": local_ip,
        "local_port": local_port,
        "remote_ip": remote_ip,
        "remote_port": remote_port,
        "status": status,
    }
