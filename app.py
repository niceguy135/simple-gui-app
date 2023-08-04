#!/usr/bin/python3
import sys
from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

from first_maket_ui import Ui_Form
from models import EmployeeInterface, Employee


class ProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.employes = list()
        self.employeeModel = EmployeeInterface(self.employes)
        self.ui.employesTable.setModel(self.employeeModel)

    def addEmployeePressed(self):
        self.employes.append(Employee(room=randint(0,1000), percent=randint(0,100)))
        self.ui.employesTable.setModel(EmployeeInterface(self.employes))
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