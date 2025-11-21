#!/bin/bash

clear

# Always operate from script directory
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

banner() {
    python3 tools/banner.py
}

pause() {
    echo ""
    read -p "Press ENTER to continue..."
}

menu() {
    clear
    banner
    echo "========================================================="
    echo "                 MAIN MENU (Linux / macOS)"
    echo "========================================================="
    echo "[1] Install Dependencies"
    echo "[2] Run Watchdog (Normal Mode)"
    echo "[3] Run Watchdog (Background Mode)"
    echo "[4] Stop Watchdog"
    echo "[5] View Logs"
    echo "[6] Extra Tools >>"
    echo "[7] Exit"
    echo "========================================================="
    read -p "Choose an option: " c

    case "$c" in
        1) deps ;;
        2) normal ;;
        3) background ;;
        4) stop ;;
        5) logs ;;
        6) extra ;;
        7) exit 0 ;;
        *) echo "Invalid option"; pause; menu ;;
    esac
}

deps() {
    clear
    banner
    echo "Installing dependencies..."
    pip3 install psutil colorama pyfiglet requests > /dev/null
    echo "Done."
    pause
    menu
}

normal() {
    clear
    banner
    echo "Running Network Watchdog (Normal Mode)..."
    echo "Press Q in the app to quit."
    python3 -m service.network_watchdog_service
    pause
    menu
}

background() {
    clear
    banner
    echo "Launching Watchdog in background..."
    nohup python3 -m service.network_watchdog_service > logs/background.log 2>&1 &
    echo "Watchdog is now running in background."
    pause
    menu
}

stop() {
    clear
    banner
    echo "Stopping background watchdog..."
    pkill -f "network_watchdog_service" 2>/dev/null
    echo "Stopped."
    pause
    menu
}

logs() {
    clear
    banner
    echo "=========== ACTIVITY LOG ==========="
    echo ""
    if [ -f logs/activity.log ]; then
        cat logs/activity.log
    else
        echo "No logs found."
    fi
    echo ""
    pause
    menu
}

extra() {
    clear
    banner
    echo "========================================================="
    echo "                        EXTRA TOOLS"
    echo "========================================================="
    echo "[A] Clear Logs"
    echo "[B] Open Logs Folder"
    echo "[C] Show Python Version"
    echo "[D] Run Watchdog (LOG Mode)"
    echo "[E] Run Watchdog (Domain Mode)"
    echo "[F] Restart Background Mode"
    echo "[G] Return"
    echo "========================================================="
    read -p "Choose option: " s

    case "$s" in
        A|a) clear && banner && rm -f logs/*.log && echo "Logs cleared."; pause; extra ;;
        B|b) 
            clear; banner
            if command -v xdg-open >/dev/null; then
                xdg-open logs/
            else
                open logs/
            fi
            extra ;;
        C|c) clear; banner; python3 --version; pause; extra ;;
        D|d) clear; banner; python3 -m service.watchdog_log_mode; pause; extra ;;
        E|e) clear; banner; python3 -m service.watchdog_domain_mode; pause; extra ;;
        F|f) stop; background; extra ;;
        G|g) menu ;;
        *) echo "Invalid option"; pause; extra ;;
    esac
}

menu
