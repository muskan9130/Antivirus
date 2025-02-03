from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel
import sys
from scanner import scan_file

class AntivirusGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Antivirus Scanner")
        layout = QVBoxLayout()
        
        self.label = QLabel("Drop a file to scan", self)
        layout.addWidget(self.label)

        self.scan_button = QPushButton("Select File & Scan", self)
        self.scan_button.clicked.connect(self.scan_file)
        layout.addWidget(self.scan_button)

        self.setLayout(layout)

    def scan_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            result = scan_file(file_path)
            self.label.setText(result)

app = QApplication(sys.argv)
window = AntivirusGUI()
window.show()
sys.exit(app.exec())
import logging

class AntivirusGUI(QWidget):
    def __init__(self):
        super().__init__()
        logging.basicConfig(filename='antivirus.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.initUI()

    def scan_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select File")
        if file_path:
            try:
                result = scan_file(file_path)
                self.label.setText(result)
                logging.info(f'Scanned file: {file_path} - Result: {result}')
            except Exception as e:
                self.label.setText('Error scanning file')
                logging.error(f'Error scanning file: {file_path} - {str(e)}')