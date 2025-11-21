# Documentation Index

This directory will contain multiple documentation files for Network Watchdog.

## Files Included

- **get_started.md** – Quick guide to start using Network Watchdog.
- **installation.md** – Full installation guide per OS.
- **modes.md** – Explanation of all monitoring modes.
- **architecture.md** – Internal system design and code flow.

---

## architecture.md

# Architecture Overview

Network Watchdog's structure is modular.

## Core Components

### `net_monitor.py`

- Calls `psutil.net_connections()`
- Extracts PID, local/remote IPs, ports, status
- Sends results to classification engine

### `threat_detector.py`

- Classifies traffic using prefix heuristics
- Levels: AMAN / WARNING / DANGER

### `logger.py`

- Writes to `logs/activity.log`
- Formats events

### `notifier.py`

- Windows toast notifications
- Terminal fallback for Linux/macOS

### `banner.py`

- Handles ASCII art and color themes

## Control Scripts

### Windows

`NetworkWatchdogInstaller.bat` handles menus and launching.

### Linux/macOS

`NetworkWatchdogInstaller.sh` provides identical functionality.

---

All documentation files above can be expanded based on your project's features.
