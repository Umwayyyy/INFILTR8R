import nmap
import time
from tkinter import END

# Function to validate individual ports and port ranges
def is_valid_port_or_range(port):
    if port.isdigit():
        return 1 <= int(port) <= 65535
    elif '-' in port:
        try:
            start_port, end_port = map(int, port.split('-'))
            return 1 <= start_port <= 65535 and 1 <= end_port <= 65535 and start_port < end_port
        except ValueError:
            return False
    return False

# Function to handle multiple ports/ranges input
def parse_ports_input(port_ranges):
    port_ranges_list = port_ranges.replace(" ", "").split(',')
    valid_ports = []
    for port_range in port_ranges_list:
        if is_valid_port_or_range(port_range):
            valid_ports.append(port_range)
        else:
            return None
    return valid_ports

# Port scanning function integrated with GUI
def port_scanner(port_input, ip_entry, tree, output_text):
    nm = nmap.PortScanner()
    target_ip = ip_entry.get()  # Get the IP address from the GUI Entry widget

    # Validate and parse the port input
    scan_targets = parse_ports_input(port_input)
    if not scan_targets:
        output_text.insert(END, "Invalid port input. Use single ports or ranges (e.g., 30, 80-100).\n")
        return

    # Start scanning for each valid port/range
    for scan_target in scan_targets:
        output_text.insert(END, f"Scanning {target_ip} for ports {scan_target}...\n")
        nm.scan(target_ip, scan_target)

        # Check if any TCP ports are open and display results
        if 'tcp' in nm[target_ip]:
            ports_to_be_scanned = [(port, nm[target_ip]['tcp'][port]['state']) for port in nm[target_ip]['tcp']]
            for port, state in ports_to_be_scanned:
                tree.insert("", END, values=(port, state))  # Populate Treeview widget
                output_text.insert(END, f"Port {port} is {state}\n")
                time.sleep(0.3)  # Optional delay for readability
        else:
            output_text.insert(END, f"No TCP ports open for {scan_target}.\n")
