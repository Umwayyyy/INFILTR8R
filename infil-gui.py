import nmap 
import time  
from tkinter import *  # Import all functions from tkinter for GUI
from tkinter import messagebox, ttk, Text  # Import specific tkinter modules for message boxes, and text
from infilvalidation import *  # Import functions from infilvalidation for IP and port validation

def welcome_box():
    messagebox.showinfo("WELOCME", "Welcome to INFILTR8R!\n\n"
                        "For more information on how to use our port scanner, head over to the 'Help' option in the menu\n\n"
                        "Happy Scanning!! :)")

# Function to display the "About" information
def show_about():
    messagebox.showinfo("About", 
                        "INFILTR8R is a port scanning tool designed to help network administrators and security professionals identify open ports and potential vulnerabilities.\n\n"
                        "Version: 1.2.5\n"
                        "Developed by: INFILTR8R Team\n\n"
                        "For more information, visit our website or contact support at support@infiltr8r.com.")

# Function to display the "Help Desk" information
def show_help_desk():
    messagebox.showinfo("Help Desk", "When inputing an ip address, please be sure to use this format (Ex. 0-255.0-255.0-255.0-255)\n\n"
                        "When inputing a port, you can choosse to do a single port, a port range, or both. Please be sure to use this format (Ex. 20, 22-80, 443)\n\n"
                        "For further assistance, please contact our support team at support@infiltr8r.com.")

# Function to display the "Report" information
def show_report():
    messagebox.showinfo("Report", "If you encounter any issues, please report them to issues@infiltr8r.com.")

# Function to display the "Check for Updates" information
def show_updates():
    messagebox.showinfo("Check for Updates", "You're using the latest version of Infiltr8r.\n"
                        "Version: 1.2.5")

# Function to start the GUI
import nmap
from tkinter import *  # Import tkinter for GUI components
from tkinter import messagebox, ttk, Text  # Import specific tkinter modules
from infilvalidation import *  # Import IP and port validation functions

def start_gui():
    global e1, e2, tree, output_text
    root = Tk()
    root.title('INFILTR8R')

    # -------- Welcome Label ---------------------
    w = Label(root, text='WELCOME TO INFILTR8R')
    w.grid(row=0, column=0, columnspan=2)

    # -------- Navigation Menu ---------------------
    menu = Menu(root)
    root.config(menu=menu)

    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='Save as')
    filemenu.add_command(label='Mail to')
    filemenu.add_command(label='Export')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)

    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
    helpmenu.add_command(label='Help Desk')
    helpmenu.add_command(label='Report')
    helpmenu.add_command(label='Check for updates')

    # --------- IP Address Input -------------------
    Label(root, text='IP Address').grid(row=2, column=0)
    e1 = Entry(root)
    e1.grid(row=2, column=1)

    submit_ip = Button(root, text='Submit', command=lambda: get_ip_address(e1.get(), output_text))
    submit_ip.grid(row=2, column=4)

    # --------- Port Range Input -------------------
    Label(root, text='Ports').grid(row=4, column=0)
    e2 = Entry(root)
    e2.grid(row=4, column=1)

    submit_port = Button(root, text='Submit', command=lambda: port_scanner(e2.get(), e1, tree, output_text))
    submit_port.grid(row=4, column=4)

    # -------- Treeview for displaying scan results -----------
    tree = ttk.Treeview(root, columns=("Port", "State"), show='headings')
    tree.heading("Port", text="Port")
    tree.heading("State", text="State")
    tree.grid(row=5, column=0, columnspan=3)

    # Output Text Area for messages
    output_text = Text(root, height=10, width=50)
    output_text.grid(row=6, column=0, columnspan=3)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    start_gui()
