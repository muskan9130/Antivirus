from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil
import os
import time

BACKUP_FOLDER = "file_backups"
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

class RansomwareDetector(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            backup_path = os.path.join(BACKUP_FOLDER, os.path.basename(event.src_path))
            shutil.copy(event.src_path, backup_path)
            print(f"⚠ Possible ransomware detected! Backup created: {backup_path}")

def start_ransomware_detection():
    observer = Observer()
    observer.schedule(RansomwareDetector(), path=".", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()