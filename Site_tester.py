import os
import time
import requests
from colorama import Fore, init

# Initialize colorama
init(autoreset=True)

def clear_console():
    """This function clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_screen():
    """This function displays the loading screen."""
    intro_text = [
        Fore.RED + "Hello, this script was written by the creator of Satan, an Iranian hacker.",
        Fore.RED + "Please note that this script is for research purposes only and should not be available to anyone.",
        Fore.RED + "Please use it properly. We do not take any responsibility.",
        Fore.RED + "Loading..."
    ]
    
    for line in intro_text:
        print(line)
    for i in range(10, 0, -1):
        print(Fore.RED + f"{i} seconds remaining...")
        time.sleep(1)

clear_console()
loading_screen()

user_input = input(Fore.YELLOW + "Press 'y' to continue: ")
if user_input.lower() != 'y':
    print(Fore.RED + "Exiting the program...")
    exit()

T4 = [
    "ss", "js", "images", "fonts", "ocs", "assets", "pages",
    "videos", "audio", "uploads", "downloads", "scripts", "styles",
    "layouts", "templates", "includes", "data", "files", "media",
    "gallery", "resources", "backups", "news", "articles", "projects",
    "apps", "mobile", "desktop", "panel", "admin", "theme", "plugins",
    "errors", "logs", "cache", "temp", "archives", "log", "shop",
    "products", "art", "checkout", "orders", "accounts", "profile",
    "messages", "notifications", "events", "calendar", "search", "contact",
    "forms", "about", "team", "services", "careers", "contact-us",
    "support", "faq", "terms", "privacy", "policy", "legal", "sign-in",
    "sign-up", "forgot-password", "reset-password", "dashboard", 
    "settings", "references", "notifications", "messages", "invites",
    "friends", "connections", "followers", "following", "likes",
    "dislikes", "events", "locations", "map", "apps", "search",
    "bookmarks", "history", "watchlist", "favorites", "recommendations",
    "trending", "recently-viewed", "top-rated", "new-arrivals",
    "promotions", "discounts", "feature", "best-sellers", "trending-now",
    "special-offers", "clearance"
]

print(Fore.BLUE + "Creator of Satan")
print(Fore.BLUE + """
⠀⠀⠀⠀⠀⠀⢀⡠⠖⠚⠋⠉⠉⠉⠉⠉⠉⠙⠒⢦⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⠞⠉⠀⠀⠀⢠⣾⣿⡦⡀⠀⣴⣾⣧⣀⠀⠀
⠀⠀⠀⢠⡏⠀⠀⠀⠀⠀⠀⣉⣁⣀⣀⣤⣿⣿⣿⣿⣦⠀
⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠙⢻⣿⣿⣿⣿⣿⠀
⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠉⠉⠙⡟⠀
⠀⢸⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀
⠀⢈⡏⠀            ⣤⡀⡀⠳⡄⠀⠀⠀
⠀⣸⡴⠀⠀⠀⠀⠀⠀⡀⢠⡄⣄⣷⣿⣷⣷⣠⡘⣆⠀⠀
⢠⣿⣧⡞⣠⡄⣰⣇⣼⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀
⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣧
⠋⠁⣿⡿⠟⣿⣿⣿⡿⣿⣿⣿⠋⠻⣿⣿⠏⠉⠻⣿⠀⠉
⠀⠀⠈⠀⠀⠙⣿⡿⠁⠈⣿⠏⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")

T1 = input(Fore.YELLOW + "URL: ")
if not T1:
    raise ValueError("URL cannot be empty!")

for page in T4:
    try:
        response = requests.get(f"https://{T1}/{page}")
        if response.status_code == 200:
            print(Fore.GREEN + "[+] " + Fore.WHITE + f"Success: {T1}/{page} is accessible.")
        else:
        	print(Fore.RED + "[+] " + Fore.WHITE + f"Error: {T1}/{page} is not accessible.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "[!] " + Fore.WHITE + f"Error: {e}")