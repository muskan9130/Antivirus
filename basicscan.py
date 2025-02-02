import hashlib
import os

# Sample database of known malware hashes
MALWARE_HASHES = {
    "5d41402abc4b2a76b9719d911017c592",  # Example hash
    "e99a18c428cb38d5f260853678922e03"
}

def calculate_file_hash(file_path):
    """Calculate SHA256 hash of a file."""
    hasher = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(4096):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def scan_directory(directory):
    """Scan all files in a directory and check for malware."""
    print(f"Scanning directory: {directory}\n")
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hash = calculate_file_hash(file_path)
            if file_hash in MALWARE_HASHES:
                print(f"⚠️ Malware detected: {file_path}")
            else:
                print(f"✔ Safe: {file_path}")

if __name__ == "__main__":
    directory_to_scan = input("Enter directory to scan: ")
    scan_directory(directory_to_scan)
