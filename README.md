# Python Antivirus with PyQt6

## Overview
This project is a simple antivirus scanner built using Python and PyQt6. It allows users to scan files and folders for known malware by checking file hashes against a malware database. The UI provides an easy drag-and-drop feature and pop-up alerts for scan results.

## Features
✅ **Drag & Drop File Scanning**  
✅ **Select File or Folder for Scanning**  
✅ **Detects Known Malware using Hash Matching**  
✅ **Quarantine Infected Files**  
✅ **Log Scan Results for Review**  
✅ **Modern & User-Friendly GUI**  

## Installation
1. **Clone this repository**
   ```bash
   git clone https://github.com/your-repo/python-antivirus.git
   cd python-antivirus
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the antivirus scanner:
```bash
python main.py
```

## How It Works
- **File Selection:** Users can drag & drop a file or folder, or select via the browse button.
- **Hash Calculation:** The script calculates SHA-256 hashes of the selected files.
- **Malware Detection:** It compares the hashes against a predefined database of known malware hashes.
- **Alerts & Logs:** If malware is found, the file is quarantined, and an alert popup appears.

## Project Structure
```
Antivirus-Project/
│── main.py          # PyQt6 GUI for file scanning
│── scanner.py       # Core malware detection logic
│── quarantine/      # Stores infected files
│── logs/            # Stores scan results
│── database/        # Malware hash signatures
│── assets/          # UI icons, images
│── README.md        # Project documentation
│── requirements.txt # Dependencies list
```

## Future Enhancements
🔹 **Real-time Scanning** - Monitor files for threats automatically.  
🔹 **Machine Learning Detection** - Detect unknown malware using AI.  
🔹 **Integration with VirusTotal API** - Check files against an online threat database.  
🔹 **Process Monitoring** - Detect and stop suspicious processes.  

## Contributions
Feel free to **fork, and submit pull requests!** Contributions are welcome. 🚀


