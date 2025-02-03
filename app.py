import time
import random
import curses
from datetime import datetime

def generate_data():
    
    data = {
        "Packet Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "Source IP": f"192.168.1.{random.randint(1, 254)}",
        "Destination IP": f"192.168.1.{random.randint(1, 254)}",
        "Source Port": random.randint(1000, 9999),
        "Destination Port": random.randint(1000, 9999),
        "Protocol Type": random.choice(['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS']),
        "Packet Length": random.randint(40, 1500),
        "TCP Flags": random.choice(['SYN', 'ACK', 'FIN', 'RST', 'PSH']),
        "Sequence Number (TCP)": random.randint(1000, 999999),
        "Acknowledgment Number (TCP)": random.randint(1000, 999999),
        "Network Interface (NIC)": "wlan1",  # Fixed value
        "Payload (Data)": f"Data {random.randint(1, 1000)}",
        "TTL": random.randint(1, 64),
        "ICMP Type and Code": f"Type {random.randint(0, 255)}, Code {random.randint(0, 255)}",
        "Error and Drop Information": random.choice(['No Errors', 'Packet Drop', 'Error']),
        "Network Traffic Volume": f"{random.randint(10, 5000)} Bps",
        "Session/Flow Data": f"Flow {random.randint(1, 10)}",
        "DNS Queries and Responses": random.choice(['Resolved', 'Unresolved']),
        "Bandwidth Utilization": f"{random.randint(1, 100)}%",
        "Encryption": random.choice(['Encrypted', 'Not Encrypted']),
        "Geolocation Data": f"Lat: {random.uniform(-90, 90):.2f}, Lon: {random.uniform(-180, 180):.2f}",
        "HTTP Request Headers": f"GET /page{random.randint(1, 10)} HTTP/1.1",
        "Authentication Information": f"User {random.choice(['admin', 'guest', 'user'])}",
    }
    return data

def display_network_stats(stdscr):
    # Clear screen
    stdscr.clear()
    
    # Set up the display window
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)  # Non-blocking input
    stdscr.timeout(1000)  # Refresh every second

    # Title and border setup
    stdscr.addstr(0, 0, "==== Network Packet Capture - Stats ====", curses.A_BOLD)
    stdscr.addstr(1, 0, "=" * 50, curses.A_BOLD)
    stdscr.addstr(3, 0, "Press 'q' to Quit", curses.A_BOLD)

    while True:
        data = generate_data()
        
        # Clear screen before drawing new data
        stdscr.clear()
        stdscr.addstr(0, 0, "==== Network Packet Capture - Stats ====", curses.A_BOLD)
        stdscr.addstr(1, 0, "=" * 50, curses.A_BOLD)
        stdscr.addstr(3, 0, "Press 'q' to Quit", curses.A_BOLD)
        stdscr.addstr(4, 0, "-" * 50, curses.A_BOLD)

        
        row = 5
        for key, value in data.items():
            stdscr.addstr(row, 0, f"{key}:")
            stdscr.addstr(row, len(key) + 2, f"{value}")
            row += 1
        
        # Refresh the screen to show the updated stats
        stdscr.refresh()

        # Check for quit key
        key = stdscr.getch()
        if key == ord('q'):  # Press 'q' to quit
            break

        # Simulate continuous stats every 1 second
        time.sleep(1)

def main():
    
    curses.wrapper(display_network_stats)

if __name__ == "__main__":
    main()
