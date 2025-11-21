import datetime
import os

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "activity.log")

os.makedirs(LOG_DIR, exist_ok=True)

def _write(level, message):
    t = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{t}] [{level}] {message}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def log_info(msg):
    _write("INFO", msg)

def log_warning(msg):
    _write("WARNING", msg)

def log_danger(msg):
    _write("DANGER", msg)
