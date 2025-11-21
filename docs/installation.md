# Documentation Index

This directory will contain multiple documentation files for Network Watchdog.

## Files Included

* **get_started.md** – Quick guide to start using Network Watchdog.
* **installation.md** – Full installation guide per OS.
* **modes.md** – Explanation of all monitoring modes.
* **architecture.md** – Internal system design and code flow.

---

## installation.md

# Installation Guide

## 1. Windows Installation

1. Install Python 3.
2. Ensure `pip` is in PATH.
3. Run:

```bat
NetworkWatchdogInstaller.bat
```

4. Select **Install Dependencies**.

Dependencies installed:

```
psutil
colorama
pyfiglet
requests
win10toast (Windows only)
```

## 2. Linux / macOS Installation

```bash
chmod +x NetworkWatchdogInstaller.sh
./NetworkWatchdogInstaller.sh
```

Select **Install Dependencies**.

Dependencies installed:

```
pip3 install psutil colorama pyfiglet requests
```

Logs are stored in:

```
logs/activity.log
```

---