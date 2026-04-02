#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════╗
║  █████╗ ██████╗ ███╗   ███╗██╗   ██╗ ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗     ║
║ ██╔══██╗██╔══██╗████╗ ████║╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗    ║
║ ███████║██████╔╝██╔████╔██╝ ╚████╔╝ ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝    ║
║ ██╔══██║██╔══██╗██║╚██╔╝██║  ╚██╔╝  ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗    ║
║ ██║  ██║██║  ██║██║ ╚═╝ ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║    ║
║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ║
║                            ARMYCREATOR V1.0                         ║
║                      GMAIL MASS CREATOR — ANONYMOUS EDITION        ║
║                           CRPT.ZDX | DARK-AI VVIP                   ║
╚═══════════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import json
import random
import string
import requests
import threading
import subprocess
from datetime import datetime
from colorama import init, Fore, Style, Back
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pyotp
import phonenumbers
from fake_useragent import UserAgent

init(autoreset=True)

# ========== KONFIGURASI ==========
VERSION = "ARMYCREATOR V1.0"
CREATOR = "CRPT.ZDX"
PRICE_PER_EMAIL = 3000  # Rupiah
# =================================

class ArmyCreator:
    def __init__(self):
        self.driver = None
        self.accounts = []
        self.proxy_list = []
        self.sms_api_key = None
        self.captcha_api_key = None
        self.current_proxy = None
        self.success_count = 0
        self.fail_count = 0
        
    def print_banner(self):
        banner = f"""
{Fore.RED}{Style.BRIGHT}
╔════════════════════════════════════════════════════════════════════════════╗
║  █████╗ ██████╗ ███╗   ███╗██╗   ██╗ ██████╗██████╗ ███████╗ █████╗ ████████╗ ██████╗ ██████╗ ║
║ ██╔══██╗██╔══██╗████╗ ████║╚██╗ ██╔╝██╔════╝██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗║
║ ███████║██████╔╝██╔████╔██╝ ╚████╔╝ ██║     ██████╔╝█████╗  ███████║   ██║   ██║   ██║██████╔╝║
║ ██╔══██║██╔══██╗██║╚██╔╝██║  ╚██╔╝  ██║     ██╔══██╗██╔══╝  ██╔══██║   ██║   ██║   ██║██╔══██╗║
║ ██║  ██║██║  ██║██║ ╚═╝ ██║   ██║   ╚██████╗██║  ██║███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║║
║ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝║
╚════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
{Fore.CYAN}{Style.BRIGHT}
╔════════════════════════════════════════════════════════════════════════════╗
║  {Fore.YELLOW}ARMYCREATOR V1.0 — GMAIL MASS CREATOR — ANONYMOUS EDITION{Fore.CYAN}                          ║
║  {Fore.WHITE}Creator: {Fore.RED}CRPT.ZDX{Fore.WHITE} | {Fore.WHITE}Dark-Ai VVIP | {Fore.WHITE}Mode: {Fore.RED}FULL AUTO{Fore.CYAN}                     ║
║  {Fore.WHITE}Price: {Fore.GREEN}Rp 3.000/email{Fore.WHITE} | {Fore.WHITE}Target Market: {Fore.GREEN}READY{Fore.CYAN}                              ║
║  {Fore.WHITE}Time Window: {Fore.RED}7 HOURS REMAINING{Fore.WHITE} | {Fore.WHITE}Status: {Fore.GREEN}CRITICAL{Fore.CYAN}                            ║
╚════════════════════════════════════════════════════════════════════════════╝
{Style.RESET_ALL}
        """
        print(banner)
        
    def main_menu(self):
        """Main menu dengan semua opsi"""
        while True:
            print(f"\n{Fore.CYAN}{'='*60}")
            print(f"  {Fore.YELLOW}ARMYCREATOR V1.0 — MAIN MENU")
            print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
            print(f"""
{Fore.GREEN}[1]{Fore.WHITE} 🚀 CREATE SINGLE ACCOUNT
{Fore.GREEN}[2]{Fore.WHITE} 💥 MASS CREATE (BULK)
{Fore.GREEN}[3]{Fore.WHITE} ⚙️  SET PASSWORD
{Fore.GREEN}[4]{Fore.WHITE} 📧 SET EMAIL FORMAT
{Fore.GREEN}[5]{Fore.WHITE} 🔧 SET PROXY
{Fore.GREEN}[6]{Fore.WHITE} 📱 SET SMS SERVICE
{Fore.GREEN}[7]{Fore.WHITE} 🤖 SET CAPTCHA SERVICE
{Fore.GREEN}[8]{Fore.WHITE} 📊 VIEW STATISTICS
{Fore.GREEN}[9]{Fore.WHITE} 💰 PRICE & PROFIT
{Fore.GREEN}[10]{Fore.WHITE} 📁 EXPORT ACCOUNTS
{Fore.GREEN}[11]{Fore.WHITE} 🔄 IMPORT ACCOUNTS
{Fore.GREEN}[12]{Fore.WHITE} 🧹 CLEAR SESSION
{Fore.GREEN}[13]{Fore.WHITE} ℹ️  ABOUT
{Fore.GREEN}[0]{Fore.WHITE} ❌ EXIT
            """)
            
            choice = input(f"{Fore.YELLOW}[?] Select option: {Fore.GREEN}")
            
            if choice == "1":
                self.create_single_account()
            elif choice == "2":
                self.mass_create()
            elif choice == "3":
                self.set_password_menu()
            elif choice == "4":
                self.set_email_format()
            elif choice == "5":
                self.set_proxy()
            elif choice == "6":
                self.set_sms_service()
            elif choice == "7":
                self.set_captcha_service()
            elif choice == "8":
                self.view_stats()
            elif choice == "9":
                self.price_menu()
            elif choice == "10":
                self.export_accounts()
            elif choice == "11":
                self.import_accounts()
            elif choice == "12":
                self.clear_session()
            elif choice == "13":
                self.about()
            elif choice == "0":
                print(f"{Fore.RED}[!] Exiting...{Style.RESET_ALL}")
                sys.exit(0)
            else:
                print(f"{Fore.RED}[!] Invalid option!{Style.RESET_ALL}")
                
    def set_password_menu(self):
        """Menu setting password"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}PASSWORD CONFIGURATION")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"""
{Fore.GREEN}[1]{Fore.WHITE} Use custom password for all accounts
{Fore.GREEN}[2]{Fore.WHITE} Auto-generate random password
{Fore.GREEN}[3]{Fore.WHITE} Use password list from file
{Fore.GREEN}[4]{Fore.WHITE} Back to main menu
        """)
        
        choice = input(f"{Fore.YELLOW}[?] Select: {Fore.GREEN}")
        
        if choice == "1":
            custom_pass = input(f"{Fore.YELLOW}[?] Enter password: {Fore.GREEN}")
            with open("config.json", "w") as f:
                json.dump({"password_mode": "custom", "password": custom_pass}, f)
            print(f"{Fore.GREEN}[+] Password set to: {custom_pass}{Style.RESET_ALL}")
        elif choice == "2":
            length = input(f"{Fore.YELLOW}[?] Password length (default 12): {Fore.GREEN}")
            length = int(length) if length else 12
            with open("config.json", "w") as f:
                json.dump({"password_mode": "random", "length": length}, f)
            print(f"{Fore.GREEN}[+] Random password mode activated (length: {length}){Style.RESET_ALL}")
        elif choice == "3":
            file_path = input(f"{Fore.YELLOW}[?] Password list file path: {Fore.GREEN}")
            if os.path.exists(file_path):
                with open("config.json", "w") as f:
                    json.dump({"password_mode": "file", "file": file_path}, f)
                print(f"{Fore.GREEN}[+] Password list loaded: {file_path}{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] File not found!{Style.RESET_ALL}")
    
    def set_email_format(self):
        """Set format email"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}EMAIL FORMAT CONFIGURATION")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"""
{Fore.GREEN}[1]{Fore.WHITE} username@gmail.com (random)
{Fore.GREEN}[2]{Fore.WHITE} username+number@gmail.com
{Fore.GREEN}[3]{Fore.WHITE} firstname.lastname@gmail.com
{Fore.GREEN}[4]{Fore.WHITE} Custom format
{Fore.GREEN}[5]{Fore.WHITE} Back to main menu
        """)
        
        choice = input(f"{Fore.YELLOW}[?] Select: {Fore.GREEN}")
        
        if choice == "1":
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["email_format"] = "random"
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] Email format: random username{Style.RESET_ALL}")
        elif choice == "2":
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["email_format"] = "plus"
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] Email format: username+number@gmail.com{Style.RESET_ALL}")
        elif choice == "3":
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["email_format"] = "fullname"
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] Email format: firstname.lastname@gmail.com{Style.RESET_ALL}")
        elif choice == "4":
            custom = input(f"{Fore.YELLOW}[?] Custom format (use {Fore.GREEN}{{username}}{Fore.YELLOW} as placeholder): {Fore.GREEN}")
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["email_format"] = "custom"
                config["custom_format"] = custom
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] Custom format saved: {custom}{Style.RESET_ALL}")
    
    def set_proxy(self):
        """Setup proxy configuration"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}PROXY CONFIGURATION")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"""
{Fore.GREEN}[1]{Fore.WHITE} Use local IP (default)
{Fore.GREEN}[2]{Fore.WHITE} Use proxy list from file
{Fore.GREEN}[3]{Fore.WHITE} Use rotating proxies
{Fore.GREEN}[4]{Fore.WHITE} Test proxies
{Fore.GREEN}[5]{Fore.WHITE} Back to main menu
        """)
        
        choice = input(f"{Fore.YELLOW}[?] Select: {Fore.GREEN}")
        
        if choice == "2":
            file_path = input(f"{Fore.YELLOW}[?] Proxy list file path: {Fore.GREEN}")
            if os.path.exists(file_path):
                with open(file_path) as f:
                    self.proxy_list = [line.strip() for line in f if line.strip()]
                print(f"{Fore.GREEN}[+] Loaded {len(self.proxy_list)} proxies{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] File not found!{Style.RESET_ALL}")
        elif choice == "3":
            file_path = input(f"{Fore.YELLOW}[?] Proxy list file path: {Fore.GREEN}")
            if os.path.exists(file_path):
                with open(file_path) as f:
                    self.proxy_list = [line.strip() for line in f if line.strip()]
                print(f"{Fore.GREEN}[+] Rotating proxy mode: {len(self.proxy_list)} proxies{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}[!] File not found!{Style.RESET_ALL}")
        elif choice == "4":
            self.test_proxies()
    
    def test_proxies(self):
        """Test proxy connectivity"""
        print(f"{Fore.YELLOW}[+] Testing proxies...{Style.RESET_ALL}")
        working = []
        for proxy in self.proxy_list[:10]:  # Test first 10
            try:
                response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
                if response.status_code == 200:
                    working.append(proxy)
                    print(f"{Fore.GREEN}[✓] Working: {proxy}{Style.RESET_ALL}")
            except:
                print(f"{Fore.RED}[✗] Failed: {proxy}{Style.RESET_ALL}")
        
        print(f"{Fore.GREEN}[+] Working proxies: {len(working)}/{len(self.proxy_list[:10])}{Style.RESET_ALL}")
        self.proxy_list = working
    
    def set_sms_service(self):
        """Setup SMS verification service"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}SMS VERIFICATION SERVICE")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"""
{Fore.GREEN}[1]{Fore.WHITE} SMSPool (US/UK numbers)
{Fore.GREEN}[2]{Fore.WHITE} 5SIM (Worldwide)
{Fore.GREEN}[3]{Fore.WHITE} SMSPVA (Russian numbers)
{Fore.GREEN}[4]{Fore.WHITE} TextVerified (Premium)
{Fore.GREEN}[5]{Fore.WHITE} Manual input (testing)
{Fore.GREEN}[6]{Fore.WHITE} Back to main menu
        """)
        
        choice = input(f"{Fore.YELLOW}[?] Select: {Fore.GREEN}")
        
        if choice == "1":
            api_key = input(f"{Fore.YELLOW}[?] SMSPool API Key: {Fore.GREEN}")
            self.sms_api_key = api_key
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["sms_service"] = "smspool"
                config["sms_api_key"] = api_key
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] SMSPool configured!{Style.RESET_ALL}")
        elif choice == "2":
            api_key = input(f"{Fore.YELLOW}[?] 5SIM API Key: {Fore.GREEN}")
            self.sms_api_key = api_key
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["sms_service"] = "5sim"
                config["sms_api_key"] = api_key
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] 5SIM configured!{Style.RESET_ALL}")
        elif choice == "5":
            print(f"{Fore.YELLOW}[!] Manual mode: You'll need to enter codes manually{Style.RESET_ALL}")
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["sms_service"] = "manual"
                f.seek(0)
                json.dump(config, f)
    
    def set_captcha_service(self):
        """Setup CAPTCHA solving service"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}CAPTCHA SOLVING SERVICE")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        print(f"""
{Fore.GREEN}[1]{Fore.WHITE} 2Captcha
{Fore.GREEN}[2]{Fore.WHITE} Anti-Captcha
{Fore.GREEN}[3]{Fore.WHITE} DeathByCaptcha
{Fore.GREEN}[4]{Fore.WHITE} Manual solve
{Fore.GREEN}[5]{Fore.WHITE} Back to main menu
        """)
        
        choice = input(f"{Fore.YELLOW}[?] Select: {Fore.GREEN}")
        
        if choice in ["1", "2", "3"]:
            api_key = input(f"{Fore.YELLOW}[?] API Key: {Fore.GREEN}")
            self.captcha_api_key = api_key
            services = {"1": "2captcha", "2": "anticaptcha", "3": "deathbycaptcha"}
            with open("config.json", "r+") as f:
                config = json.load(f)
                config["captcha_service"] = services[choice]
                config["captcha_api_key"] = api_key
                f.seek(0)
                json.dump(config, f)
            print(f"{Fore.GREEN}[+] CAPTCHA service configured!{Style.RESET_ALL}")
        elif choice == "4":
            print(f"{Fore.YELLOW}[!] Manual mode: You'll need to solve captchas manually{Style.RESET_ALL}")
    
    def create_single_account(self):
        """Create single Gmail account"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}CREATING SINGLE ACCOUNT")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        # Setup driver
        if not self.setup_driver():
            print(f"{Fore.RED}[!] Driver setup failed!{Style.RESET_ALL}")
            return
        
        # Generate account details
        first_name = self.generate_name()
        last_name = self.generate_name()
        password = self.get_password()
        email = self.generate_email(first_name, last_name)
        
        print(f"{Fore.GREEN}[+] First Name: {first_name}")
        print(f"[+] Last Name: {last_name}")
        print(f"[+] Email: {email}")
        print(f"[+] Password: {password}{Style.RESET_ALL}")
        
        # Create account
        success = self.create_gmail_account(first_name, last_name, email, password)
        
        if success:
            self.success_count += 1
            account_data = {
                "email": email,
                "password": password,
                "first_name": first_name,
                "last_name": last_name,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.accounts.append(account_data)
            self.save_account(account_data)
            print(f"{Fore.GREEN}[✓] Account created successfully!{Style.RESET_ALL}")
        else:
            self.fail_count += 1
            print(f"{Fore.RED}[✗] Account creation failed!{Style.RESET_ALL}")
        
        self.driver.quit()
        
    def mass_create(self):
        """Mass create multiple accounts"""
        print(f"\n{Fore.CYAN}{'='*60}")
        print(f"  {Fore.YELLOW}MASS ACCOUNT CREATION")
        print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
        
        count = input(f"{Fore.YELLOW}[?] How many accounts to create? {Fore.GREEN}")
        try:
            count = int(count)
        except:
            print(f"{Fore.RED}[!] Invalid number!{Style.RESET_ALL}")
            return
        
        print(f"{Fore.YELLOW}[!] Creating {count} accounts...{Style.RESET_ALL}")
        print(f"{Fore.RED}[!] WARNING: This will use {count * 3000} credits (Rp {count * 3000:,}){Style.RESET_ALL}")
        
        confirm = input(f"{Fore.YELLOW}[?] Confirm? (y/n): {Fore.GREEN}")
        if confirm.lower() != 'y':
            return
        
        for i in range(count):
            print(f"\n{Fore.CYAN}[+] Creating account {i+1}/{count}{Style.RESET_ALL}")
            
            if not self.setup_driver():
                print(f"{Fore.RED}[!] Driver setup failed, skipping...{Style.RESET_ALL}")
                continue
            
            first_name = self.generate_name()
            last_name = self.generate_name()
            password = self.get_password()
            email = self.generate_email(first_name, last_name)
            
            success = self.create_gmail_account(first_name, last_name, email, password)
            
            if success:
                self.success_count += 1
                account_data = {
                    "email": email,
                    "password": password,
                    "first_name": first_name,
                    "last_name": last_name,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                self.accounts.append(account_data)
                self.save_account(account_data)
                print(f"{Fore.GREEN}[✓] Account {i+1} created!{Style.RESET_ALL}")
            else:
                self.fail_count += 1
                print(f"{Fore.RED}[✗] Account {i+1} failed!{Style.RESET_ALL}")
            
            self.driver.quit()
            time.sleep(random.randint(30, 60))  # Delay between accounts
            
        print(f"\n{Fore.GREEN}[+] Mass creation completed!{Style.RESET_ALL}")
        print(f"{Fore.GREEN}[+] Success: {self.success_count} | Failed: {self.fail_count}{Style.RESET_ALL}")
    
    def setup_driver(self):
        """Setup Chrome driver with proxy and stealth"""
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            
            # Random user agent
            ua = UserAgent()
        chrome_options.add_argument('--user-data-dir')
