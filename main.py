import sys
import os
import hashlib
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QMessageBox
from PyQt6.QtGui import QDragEnterEvent, QDropEvent, QFont
from PyQt6.QtCore import Qt
from scanner import scan_path

class AntivirusGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Python Antivirus")
        self.setGeometry(100, 100, 600, 500)
        self.setAcceptDrops(True)
        self.setStyleSheet("background-color: #2C3E50; color: white;")

        layout = QVBoxLayout()

        self.label = QLabel("Drag and drop a file or folder to scan")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        layout.addWidget(self.label)

        self.scanButton = QPushButton("Select File/Folder")
        self.scanButton.setStyleSheet("background-color: #3498DB; color: white; font-size: 14px; padding: 10px;")
        self.scanButton.clicked.connect(self.selectFileOrFolder)
        layout.addWidget(self.scanButton)

        self.resultText = QTextEdit()
        self.resultText.setReadOnly(True)
        self.resultText.setFont(QFont("Courier", 12))
        self.resultText.setStyleSheet("background-color: #34495E; color: #ECF0F1; padding: 10px;")
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
        path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if not path:
            path = QFileDialog.getExistingDirectory(self, "Select Folder")
        
        if path:
            self.scanPath(path)

    def scanPath(self, path):
        results = scan_path(path)
        self.resultText.append(results)
        
        if "⚠️ Malware detected" in results:
            self.showPopup("Warning", "Virus detected! The file has been quarantined.", QMessageBox.Icon.Warning)
        else:
            self.showPopup("Safe", "No threats detected.", QMessageBox.Icon.Information)

    def showPopup(self, title, message, icon):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setIcon(icon)
        msg.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntivirusGUI()
    window.show()
    sys.exit(app.exec())
