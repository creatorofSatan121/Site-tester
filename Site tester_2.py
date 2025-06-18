import os
import time
import requests
from colorama import Fore, init

# راه‌اندازی colorama
init(autoreset=True)

def clear_console():
    """این تابع کنسول را پاک می‌کند."""
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_screen():
    """این تابع صفحه لودینگ را نمایش می‌دهد."""
    intro_text = [
        Fore.RED + "سلام، این اسکریپت توسط سازنده شیطان، یک هکر ایرانی نوشته شده است.",
        Fore.RED + "لطفاً توجه داشته باشید که این اسکریپت فقط برای اهداف پژوهشی است و نباید در دسترس کسی باشد.",
        Fore.RED + "لطفاً از آن به درستی استفاده کنید. ما هیچ گونه مسئولیتی نداریم.",
        Fore.RED + "در حال بارگذاری..."
    ]
    
    for line in intro_text:
        print(line)
    for i in range(10, 0, -1):
        print(Fore.RED + f"{i} ثانیه باقی مانده...")
        time.sleep(1)

clear_console()
loading_screen()

user_input = input(Fore.YELLOW + "برای ادامه 'y' را فشار دهید: ")
if user_input.lower() != 'y':
    print(Fore.RED + "خروج از برنامه...")
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

print(Fore.BLUE + "سازنده شیطان")
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
    raise ValueError("URL نمی‌تواند خالی باشد!")

for page in T4:
    try:
        response = requests.get(f"https://{T1}/{page}")
        if response.status_code == 200:
        	print(Fore.GREEN + "[+] " + Fore.WHITE + f"موفقیت: {T1}/{page} در دسترس است.")
        else:
            print(Fore.RED + "[+] " + Fore.WHITE + f"خطا: {T1}/{page} در دسترس نیست.")
    except requests.exceptions.RequestException as e:
        print(Fore.RED + "[!] " + Fore.WHITE + f"خطا: {e}")