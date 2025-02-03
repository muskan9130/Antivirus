import psutil
import time

def monitor_processes():
    print("🔍 Monitoring running processes...\n")
    while True:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'connections']):
            try:
                if proc.info['cpu_percent'] > 50 or len(proc.info['connections']) > 5:
                    print(f"⚠ Suspicious Process: {proc.info['name']} (PID: {proc.info['pid']})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
                
        time.sleep(5)
