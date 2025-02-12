import sys
import os
import hashlib
import shutil
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit
from PyQt6.QtGui import QDragEnterEvent, QDropEvent
from PyQt6.QtCore import Qt
from scanner import scan_path

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

    def scanPath(self, path):
        results = scan_path(path)
        self.resultText.append(results)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AntivirusGUI()
    window.show()
    sys.exit(app.exec())
