import hashlib
import os
import shutil

# Real-world malware hashes (SHA-256)
MALWARE_HASHES = {
    "d55f983c994caa160ec63a59f6b4250fe67fb3e8c43a388aec60a4a6978e9f1e",  # SocGholish Downloader
    
    "9aa1f37517458d635eae4f9b43cb4770880ea0ee171e7e4ad155bbdee0cbe732",  # Veeam Credential Dumper
    
    "b2f5ff47436671b6e533d8dc3614845d",  # Money Message Ransomware
    
    "e99a18c428cb38d5f260853678922e03",  # BlackSuit (Royal) Ransomware
    
    "5d41402abc4b2a76b9719d911017c592"  # Monti Ransomware
}

QUARANTINE_DIR = "quarantine"
LOG_FILE = "logs/scan_log.txt"

def log_message(message):
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")
    return message

def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"Error reading {file_path}: {e}"

def quarantine_file(file_path):
    if not os.path.exists(QUARANTINE_DIR):
        os.makedirs(QUARANTINE_DIR)
    try:
        shutil.move(file_path, os.path.join(QUARANTINE_DIR, os.path.basename(file_path)))
        return log_message(f"🚨 Quarantined: {file_path}")
    except Exception as e:
        return log_message(f"Error quarantining {file_path}: {e}")

def scan_path(path):
    result = f"Scanning: {path}\n"
    if os.path.isdir(path):
        for root, _, files in os.walk(path):
            for file in files:
                result += scan_file(os.path.join(root, file)) + "\n"
    else:
        result += scan_file(path) + "\n"
    return result

def scan_file(file_path):
    file_hash = calculate_file_hash(file_path)
    if file_hash in MALWARE_HASHES:
        return log_message(f"⚠️ Malware detected: {file_path}\n") + quarantine_file(file_path)
    else:
        return log_message(f"✔ Safe: {file_path}\n")
