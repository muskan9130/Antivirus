from scanner import scan_file
from behavior_monitor import monitor_processes
from ransomware import start_ransomware_detection
from web_protection import check_url
from sandbox import run_in_sandbox
from ml_model import scan_with_ml
import threading

def main():
    print("🔹 Antivirus System Running...\n")
    
    # Start behavior monitoring in a separate thread
    behavior_thread = threading.Thread(target=monitor_processes, daemon=True)
    behavior_thread.start()

    # Start ransomware detection
    ransomware_thread = threading.Thread(target=start_ransomware_detection, daemon=True)
    ransomware_thread.start()

    while True:
        choice = input("\n1. Scan File\n2. Scan URL\n3. Run in Sandbox\n4. Machine Learning Scan\n5. Exit\nChoose: ")
        
        if choice == "1":
            file = input("Enter file path: ")
            print(scan_file(file))
        
        elif choice == "2":
            url = input("Enter URL: ")
            print(check_url(url))
        
        elif choice == "3":
            file = input("Enter file path: ")
            run_in_sandbox(file)
        
        elif choice == "4":
            file = input("Enter file path: ")
            print(scan_with_ml(file))
        
        elif choice == "5":
            print("Exiting Antivirus...")
            break

if __name__ == "__main__":
    main()
