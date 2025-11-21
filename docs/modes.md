# Documentation Index

This directory will contain multiple documentation files for Network Watchdog.

## Files Included

- **get_started.md** – Quick guide to start using Network Watchdog.
- **installation.md** – Full installation guide per OS.
- **modes.md** – Explanation of all monitoring modes.
- **architecture.md** – Internal system design and code flow.

---

## modes.md

# Network Watchdog Modes

Network Watchdog supports several modes for different monitoring needs.

## 1. Normal Mode

Live table of:

- PID
- Process Name
- Remote IP
- Status
- Threat Level

Updated every second.

## 2. Background Mode

Runs monitoring silently:

- Windows uses `pythonw`
- Linux/macOS uses `nohup`

Check background status in menu.

## 3. Log Mode

Continuous, no-clear logging output.
Shows:

- PID
- Process
- Remote IP
- Status
- Classification

Useful for long-term observation.

## 4. Domain Mode

Resolves:

- Remote IP → Domain (fast lookup)

Great for identifying which websites/apps are contacted.

## 5. Diagnostic Mode (Optional)

System-level checks (CPU/RAM/process anomalies).

---
