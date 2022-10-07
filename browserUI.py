import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt6.uic import loadUi
from PyQt6.QtGui import QPixmap
from data_extraction import get_filePath


class Browser(QDialog):
    def __init__(self):
        super(Browser, self).__init__()
        loadUi("fileBrowser.ui", self)
        self.selectImage.clicked.connect(self.getfile)
        self.fileName.textChanged.connect(self.displayImage)
        self.dataExtract.clicked.connect(self.sendFile)

    def getfile(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Open file', '/home', "Image files (*.jpg *.png, *.jpeg)")
        self.fileName.setText(fname[0])
        self.displayImage()

    # Display theselected image in the imageFilePreview object
    def displayImage(self):
        self.imageFilePreview.setPixmap(QPixmap(self.sendFile()))

    # Send file location to function in main.py

    def sendFile(self):
        get_filePath(self.fileName.text())
        return self.fileName.text()

    #


app = QApplication(sys.argv)
browser = Browser()
widget = QtWidgets.QStackedWidget()
widget.addWidget(browser)
widget.setFixedWidth(640)
widget.setFixedHeight(480)
widget.show()
sys.exit(app.exec())
