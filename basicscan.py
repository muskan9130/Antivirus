import hashlib
import os
import shutil


# Sample database of known malware hashes
MALWARE_HASHES = {
    "5d41402abc4b2a76b9719d911017c592",  # Example hash
    "e99a18c428cb38d5f260853678922e03"
}

LOG_FILE = "scan_log.txt"
QUARANTINE_DIR = "quarantine"

def log_message(message):
    """Log messages to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")
    print(message)

def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        log_message(f"Error reading {file_path}: {e}")
        return None

def quarantine_file(file_path):
    """Move infected file to quarantine directory."""
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
    try:
        shutil.move(file_path, os.path.join(QUARANTINE_DIR, os.path.basename(file_path)))
        log_message(f"🚨 Quarantined: {file_path}")
    except Exception as e:
        log_message(f"Error quarantining {file_path}: {e}")

def scan_directory(directory):
    """Scan all files in a directory and check for malware."""
    log_message(f"Scanning directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash in MALWARE_HASHES:
                log_message(f"⚠️ Malware detected: {file_path}")
                quarantine_file(file_path)
            else:
                log_message(f"✔ Safe: {file_path}")

if __name__ == "__main__":
    directory_to_scan = input("Enter directory to scan: ")
    scan_directory(directory_to_scan)
    print("Process done")
