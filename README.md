# Network Watchdog

Real-time network activity monitor for Windows, Linux, and macOS.

---

## 🛰 Overview

Network Watchdog helps you inspect active network connections, classify traffic, detect suspicious endpoints, and run monitoring services in foreground or background mode.

It includes:

* Normal monitoring mode
* Log mode (event-style output)
* Domain-resolver mode
* Background service mode
* Windows `.bat` control panel
* Linux/macOS `.sh` control panel
* Threat classification engine
* Banner-based UI for terminal aesthetics

---

## 📁 Project Structure

```
NetworkWatchdog/
│
├── service/
│   ├── network_watchdog_service.py
│   ├── net_monitor.py
│   ├── watchdog_log_mode.py
│   ├── watchdog_domain_mode.py
│   ├── logger.py
│   ├── notifier.py
│   └── threat_detector.py
│
├── tools/
│   └── banner.py
│
├── logs/
│   └── activity.log
│
├── NetworkWatchdogInstaller.bat
├── NetworkWatchdogInstaller.sh
└── README.md
```

---

## 🚀 Get Started

Choose your operating system below.

### **Windows**

1. Open **PowerShell** or **CMD**.
2. Navigate to the project directory.
3. Run:

   ```bat
   .\NetworkWatchdogInstaller.bat
   ```
4. Use the menu (Normal Mode, Background Mode, Logs, Tools, etc.).

### **Linux / macOS**

1. Open terminal.
2. Give execute permission:

   ```bash
   chmod +x NetworkWatchdogInstaller.sh
   ```
3. Run the installer:

   ```bash
   ./NetworkWatchdogInstaller.sh
   ```

---

## 📦 Installation

Dependencies will be installed automatically via the installer, but manually you can install:

### Python Dependencies

```
psutil
colorama
pyfiglet
win10toast  (Windows only)
requests
```

Manual install:

```bash
pip install psutil colorama pyfiglet requests
```

Windows toast notifications require:

```bash
pip install win10toast
```

---

## 🖥 Modes

### **Normal Mode**

Live connection monitor with status markers and threat classification.

### **Background Mode**

Runs silently:

* Windows → `pythonw`
* Linux/macOS → `nohup`

### **Log Mode**

Outputs continuous event logs without clearing the screen.

### **Domain Mode**

Resolves remote IP → domain (fast mode).

### **Threat Engine**

Classifies connections into:

* AMAN
* WARNING
* DANGER
  based on IP prefix heuristics.

---

## 🧪 Diagnostic Tools

Located inside **Extra Tools** menu:

* Clear logs
* Open logs folder
* Show Python version
* Restart background service
* Launch log/domain mode

---

## 📄 Shell Scripts

Script available for Linux/macOS:

* Automatic menu
* Background service launcher
* Log viewer
* Extra tools

---

## 🛠 Development Notes

* Python modules use relative imports (`service.*`, `tools.*`).
* Banner system uses `pyfiglet` and `colorama` for styling.
* Network inspection uses `psutil.net_connections()`.
* Background mode is designed to survive terminal closure.

---

## 📚 Documentation

| File | Description |
|------|-------------|
| [`docs/get_started.md`](./docs/get_started.md) | Quick start guide |
| [`docs/installation.md`](./docs/installation.md) | Installation & environment setup |
| [`docs/modes.md`](./docs/modes.md) | Watchdog mode explanations |
| [`docs/architecture.md`](./docs/architecture.md) | Full system architecture & flowchart |

---

## 📝 License

This project is licensed under the **MIT License**.  
See the full license here: [LICENSE](./LICENSE)

---

## 👨‍💻 Author

**rayhanrwa** – Network security tools & experimentation.
