from pyfiglet import figlet_format
from colorama import Fore, Style, init

init(autoreset=True)

def show_banner():
    pcb_top = (
        Fore.YELLOW +
        "╔" + "═" * 25 + "╦" + "═" * 25 + "╗\n" +
        Fore.GREEN +
        "║" + "  •· ··──────···   " + "║" + "   ···──────··· ·•  " + "║\n" +
        "║" + "   ───┐┌──────┐┌──  " + "║" + "   ──┐┌──────┐┌───  " + "║\n" +
        "║" + "   ─┐││┌────┐││┌─   " + "║" + "   ─┐││┌────┐││┌─   " + "║\n"
    )

    pcb_bottom = (
        Fore.GREEN +
        "║" + "   ─┘││└────┘││└─   " + "║" + "   ─┘││└────┘││└─   " + "║\n" +
        "║" + "   ··──────··· •     " + "║" + "    • ···──────···   " + "║\n" +
        Fore.YELLOW +
        "╚" + "═" * 25 + "╩" + "═" * 25 + "╝" +
        Style.RESET_ALL +
        "\n"
    )

    # Print PCB lines
    print(pcb_top)

    # Main Title (always green)
    title = figlet_format("NETWORK WATCHDOG", font="slant")
    print(Fore.GREEN + title)

    print(pcb_bottom)

    # Divider line
    line = Fore.YELLOW + "─" * 60
    print(line)

    # Descriptions
    print(
        f"{Fore.YELLOW}   Secure Network Activity Monitoring Suite\n"
        f"{Fore.GREEN}   Real-time Connections • Safe Local Analysis\n"
        f"{Fore.CYAN}   Developed by: {Fore.WHITE}rayhanrwa"
    )

    print(line + Style.RESET_ALL + "\n")

    # Feature list
    print(
        f"{Fore.GREEN}"
        " • Monitors active network connections\n"
        " • Detects suspicious ports and destinations\n"
        " • Logs summary and detailed events\n"
        " • Works on Windows, Linux, and macOS\n"
    )


if __name__ == '__main__':
    show_banner()
