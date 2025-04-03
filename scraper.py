import requests 
import socket 
import whois 
import threading 
import os 
from bs4 import BeautifulSoup 
from termcolor import colored 
from colorama import init

#Inisialisasi colorama

init(autoreset=True)

def print_banner(): 
 banner = """ 
 ░▒▓███████▓▒░░▒▓██████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░  
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
 ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓███████▓▒░░▒▓████████▓▒░▒▓███████▓▒░░▒▓██████▓▒░ ░▒▓███████▓▒░  
       ░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
       ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ 
                                                                                             
  Made By : Peju3ncer                                                                                           
  """
 print(colored(banner, "cyan"))

def whois_lookup(domain): try: w = whois.whois(domain) print(colored(f"[+] WHOIS Info for {domain}:\n{w}", "green")) except Exception as e: print(colored(f"[-] WHOIS lookup failed: {e}", "red"))

def port_scan(target, ports=[21, 22, 23, 25, 53, 80, 443, 3306, 8080]): print(colored(f"[🔎] Scanning ports on {target}...", "yellow")) for port in ports: try: sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) sock.settimeout(1) if sock.connect_ex((target, port)) == 0: print(colored(f"   [✅] Port {port} is open!", "green")) sock.close() except Exception as e: print(colored(f"   [❌] Error scanning port {port}: {e}", "red"))

def scrape_data(url): print(colored(f"[🔎] Scraping data from {url}...", "yellow")) try: response = requests.get(url) soup = BeautifulSoup(response.text, 'html.parser') for link in soup.find_all('a'): print(colored(f"[+] Found link: {link.get('href')}", "blue")) except Exception as e: print(colored(f"[❌] Scraping error: {e}", "red"))

def main(): print_banner() target = input(colored("[+] Enter target domain: ", "cyan"))

while True:
    print(colored("""

[1] WHOIS Lookup [2] Port Scanner [3] Web Scraper [4] Exit """, "red")) choice = input(colored("[+] Select an option: ", "cyan"))

if choice == "1":
        whois_lookup(target)
    elif choice == "2":
        port_scan(target)
    elif choice == "3":
        url = input(colored("[+] Enter URL to scrape: ", "cyan"))
        scrape_data(url)
    elif choice == "4":
        print(colored("[+] Exiting...", "cyan"))
        break
    else:
        print(colored("[❌] Invalid choice!", "red"))

if name == "main": main()

