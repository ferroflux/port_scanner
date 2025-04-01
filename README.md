# Port Scanner

## Overview
This is a fast and efficient **port scanner** built using Python. It utilizes **multi-threading** to scan multiple ports simultaneously, significantly reducing scan time compared to traditional sequential scanning.

## Features
- Scans a range of ports on a target host.
- Uses **multi-threading** for faster results.
- Identifies **common services** (e.g., HTTP, SSH, FTP) based on well-known port numbers.
- Handles invalid hostnames and socket errors gracefully.

## Prerequisites
- Python 3.x
- No additional libraries are required (uses Python's standard library).

## Usage

1. **Clone the Repository or Copy the Script**
   ```sh
   git clone https://github.com/your-repo/port_scanner.git
   cd port_scanner
   ```

2. **Run the Script**
   ```sh
   python port_scanner.py
   ```

3. **Enter the Target Host**
   - You can enter an **IP address** (e.g., `192.168.1.1`) or a **domain name** (e.g., `example.com`).

4. **Output Example**
   ```
   Scanning remote host 192.168.1.1
   ----------------------------------------------
   Port 22: Open 
   Port 80: Open 
   Port 443: Open 
   Scanning complete in: 5.23 seconds
   ```

## How It Works
- The script creates **multiple threads** using `ThreadPoolExecutor`.
- Each thread attempts to connect to a different port **simultaneously**.
- If a port is **open**, it prints the port number along with the **associated service name** (if available).

## Configuration
- You can create a `PORT_SERVICES` dictionary to include port-to-service mappings.
- The `MAX_THREADS` variable controls the number of **parallel scans** (default is 100). Adjust based on system performance.

## License
This project is licensed under the **MIT License**.
