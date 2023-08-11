#!/usr/bin/python3
import sys
from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QWidget

#макеты окон
from uiFiles.first_maket_ui import Ui_Form

#виджеты
from widgets.addEmplWidget import AddEmployeeWidget

#интерфейсы для вьюшек и сами вьюшки
from viewInterfaces.employeModels import EmployeeInterface
from viewInterfaces.reportModels import ReportInterface, ReportView 


class ProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.addEmployeeWindow = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.empInterface = None
        self.repInterface = None


        self.employes = list()
        self.ui.employesTable.setModel(EmployeeInterface(self.employes))
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)

        self.reports = list()
        self.ui.repotsTable.setModel(ReportInterface(self.reports))
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)


    def addEmployeePressed(self):
        if self.addEmployeeWindow is None:
            self.addEmployeeWindow = AddEmployeeWidget(parent=self)
            self.addEmployeeWindow.show()
        else:
            self.addEmployeeWindow.close()
            self.addEmployeeWindow = None


    def addReportPressed(self):
        self.reports.append(ReportView(totalSum=randint(0,100000),
                                              percent=randint(0,100)))
        self.ui.repotsTable.setModel(ReportInterface(self.reports))


    def calcPressed(self):
        print("Calculate")


    def savePressed(self):
        print("Save")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = ProgramWindow()
    mainWindow.show()

    sys.exit(app.exec())