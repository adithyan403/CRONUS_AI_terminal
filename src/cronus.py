
import os
import sys
import time
import platform
import datetime
import subprocess

# --- Configuration ---
VERSION = "1.0.0-ALPHA"
USER_NAME = os.getlogin()
HOSTNAME = platform.node()

# --- Colors (ANSI Escape Codes) ---
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# --- Utils ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer(text, speed=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def print_banner():
    banner = f"""{Colors.CYAN}
   CRONUS AI  |  SYSTEM INITIALIZED  |  v{VERSION}
   =================================================
 ██████╗██████╗  ██████╗ ███╗   ██╗██╗   ██╗███████╗
██╔════╝██╔══██╗██╔═══██╗████╗  ██║██║   ██║██╔════╝
██║     ██████╔╝██║   ██║██╔██╗ ██║██║   ██║███████╗
██║     ██╔══██╗██║   ██║██║╚██╗██║██║   ██║╚════██║
╚██████╗██║  ██║╚██████╔╝██║ ╚████║╚██████╔╝███████║
 ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝
    {Colors.ENDC}"""
    print(banner)
    print(f"{Colors.HEADER}Logged in as: {USER_NAME}@{HOSTNAME}{Colors.ENDC}\n")

# --- Commands ---
def cmd_help():
    print(f"\n{Colors.BOLD}AVAILABLE COMMANDS:{Colors.ENDC}")
    commands = {
        "help": "Display this help message",
        "status": "Show system status and diagnostics",
        "scan": "Scan environment (Simulation)",
        "clear": "Clear the terminal screen",
        "exit": "Terminate Cronus session"
    }
    for cmd, desc in commands.items():
        print(f"  {Colors.GREEN}{cmd.ljust(10)}{Colors.ENDC} : {desc}")
    print()

def cmd_status():
    print(f"\n{Colors.BOLD}SYSTEM DIAGNOSTICS:{Colors.ENDC}")
    print(f"  OS Mode      : {platform.system()} {platform.release()}")
    print(f"  Architecture : {platform.machine()}")
    print(f"  Processor    : {platform.processor()}")
    print(f"  Python Ver   : {platform.python_version()}")
    print(f"  Time         : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  {Colors.GREEN}STATUS       : ONLINE{Colors.ENDC}")
    print()

def cmd_scan():
    print(f"\n{Colors.CYAN}Initiating Network & System Scan...{Colors.ENDC}")
    time.sleep(0.5)
    items = ["Memory Integrity", "Network Latency", "Process Threads", "Peripheral Check"]
    for item in items:
        sys.stdout.write(f"  checking {item}...")
        sys.stdout.flush()
        time.sleep(0.3)
        sys.stdout.write(f" {Colors.GREEN}[OK]{Colors.ENDC}\n")
    print(f"{Colors.GREEN}Scan Complete. No anomalies detected.{Colors.ENDC}\n")

# --- Main Loop ---
def main():
    clear_screen()
    print_banner()
    
    # Intro animation
    type_writer(f"{Colors.GREEN}> Establishing neural link... CONNECTED.{Colors.ENDC}", 0.01)
    
    while True:
        try:
            # Custom prompt
            prompt = f"{Colors.BLUE}cronus@{HOSTNAME}{Colors.ENDC}:{Colors.WARNING}~{Colors.ENDC}$ "
            sys.stdout.write(prompt)
            sys.stdout.flush()
            user_input = input().strip()
            
            if not user_input:
                continue
                
            command = user_input.lower().split()[0]
            
            if command == "exit":
                print(f"\n{Colors.WARNING}Terminating session... Goodbye.{Colors.ENDC}")
                time.sleep(1)
                break
            elif command == "clear":
                clear_screen()
                print_banner()
            elif command == "help":
                cmd_help()
            elif command == "status":
                cmd_status()
            elif command == "scan":
                cmd_scan()
            else:
                print(f"{Colors.FAIL}Error: Command '{command}' not recognized.{Colors.ENDC}")
                
        except KeyboardInterrupt:
            print(f"\n{Colors.WARNING}Terminating session... Goodbye.{Colors.ENDC}")
            break
        except Exception as e:
            print(f"{Colors.FAIL}System Error: {e}{Colors.ENDC}")

if __name__ == "__main__":
    main()
