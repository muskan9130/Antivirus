import time
import scanner  # Import your scanner module
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "/Users/deep/Downloads"  # Change this to the folder you want to monitor

class FileMonitor(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"🔍 New file detected: {event.src_path}")
            result = scanner.scan_path(event.src_path)  # Scan the new file
            print(result)

def start_monitoring():
    print(f"🚀 Monitoring {WATCH_FOLDER} for new files...")
    event_handler = FileMonitor()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_FOLDER, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitoring()
