import sys
import hashlib
import os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtCore import Qt

# Sample malware hash database
MALWARE_HASHES = {
    "5d41402abc4b2a76b9719d911017c592",
    "e99a18c428cb38d5f260853678922e03"
}

class AntivirusGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Python Antivirus")
        self.setGeometry(100, 100, 500, 400)
        self.setAcceptDrops(True)
        
        layout = QVBoxLayout()
        
        self.label = QLabel("Drag and drop a file or folder to scan")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)
        
        self.scanButton = QPushButton("Select File/Folder")
        self.scanButton.clicked.connect(self.selectFileOrFolder)
        layout.addWidget(self.scanButton)
        
        self.resultText = QTextEdit()
        self.resultText.setReadOnly(True)
        layout.addWidget(self.resultText)
        
        self.setLayout(layout)
    
    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event: QDropEvent):
        for url in event.mimeData().urls():
            path = url.toLocalFile()
            self.scanPath(path)
    
    def selectFileOrFolder(self):
        path = QFileDialog.getExistingDirectory(self, "Select Folder") or QFileDialog.getOpenFileName(self, "Select File")[0]
        if path:
            self.scanPath(path)
    
    def calculateFileHash(self, file_path):
        hasher = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                while chunk := f.read(4096):
                    hasher.update(chunk)
            return hasher.hexdigest()
        except Exception as e:
            return None
    
    def scanPath(self, path):
        self.resultText.append(f"Scanning: {path}\n")
        
        if os.path.isdir(path):
            for root, _, files in os.walk(path):
                for file in files:
                    self.scanFile(os.path.join(root, file))
        else:
            self.scanFile(path)
    
    def scanFile(self, file_path):
        file_hash = self.calculateFileHash(file_path)
        if file_hash:
            if file_hash in MALWARE_HASHES:
                self.resultText.append(f"<span style='color:red;'>⚠ Malware detected: {file_path}</span>")
            else:
                self.resultText.append(f"<span style='color:green;'>✔ Safe: {file_path}</span>")
        else:
            self.resultText.append(f"<span style='color:orange;'>❌ Error scanning: {file_path}</span>")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntivirusGUI()
    window.show()
    sys.exit(app.exec())
