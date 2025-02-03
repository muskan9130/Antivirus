import hashlib
import json

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            hasher.update(f.read())
        return hasher.hexdigest()
    except FileNotFoundError:
        return None

def scan_file(filepath):
    with open("database/malware_signatures.json", "r") as file:
        MALWARE_HASHES = json.load(file)
    
    file_hash = get_file_hash(filepath)
    if file_hash in MALWARE_HASHES:
        return "⚠ Malware Detected!"
    return "✅ File is Safe."