#!/usr/bin/python3
import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from first_maket_ui import Ui_Form

class ProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

    def addEmployeePressed(self):
        print("Add Employee")

    def addReportPressed(self):
        print("Report")

    def calcPressed(self):
        print("Calculate")

    def savePressed(self):
        print("Save")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = ProgramWindow()
    mainWindow.show()

    sys.exit(app.exec())