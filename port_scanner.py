import socket
import os
import sys
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

# Clear the screen based on OS
os.system('cls' if os.name == 'nt' else 'clear')

# Ask for input
remoteServer = input("Enter a remote host to scan: ")

# Resolve hostname
try:
    remoteServerIP = socket.gethostbyname(remoteServer)
except socket.gaierror:
    print("Invalid hostname! Exiting...")
    sys.exit()

# Print banner
print("_" * 60)
print(f"Scanning remote host {remoteServerIP}")
print("_" * 60)

# Start timer
t1 = datetime.now()

# Function to scan a single port
def scan_port(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(0.2)  # Reduce timeout for faster results
            if sock.connect_ex((remoteServerIP, port)) == 0:
                print(f"Port {port}: Open")
    except Exception as e:
        pass  # Ignore errors to prevent slowdowns

# Number of threads (adjust based on system performance)
MAX_THREADS = 100

# Use ThreadPoolExecutor for multi-threading
with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
    executor.map(scan_port, range(1, 5000))

# End timer
t2 = datetime.now()

# Print total scan time
print(f"Scanning complete in: {t2 - t1}")
