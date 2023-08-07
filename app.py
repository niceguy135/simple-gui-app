#!/usr/bin/python3
import sys
from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QWidget

#макеты окон
from first_maket_ui import Ui_Form
import addEmployee_maket_ui as addEmplWindow

#интерфейсы для вьюшек и сами вьюшки
from employeModels import EmployeeInterface, EmployeeView
from reportModels import ReportInterface, ReportView

#основные классы сотрудников и отчетов
from logicModels import Employee, Specialist, Report


class AddEmployeeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainWidget = parent

        self.ui = addEmplWindow.Ui_Form()
        self.ui.setupUi(self)

        self.ui.employeeTypeBox.setId(self.ui.isStandart, 1)
        self.ui.employeeTypeBox.setId(self.ui.isStudent, 2)
        self.ui.employeeTypeBox.setId(self.ui.isNurse, 3)
        self.ui.employeeTypeBox.setId(self.ui.isDoctor, 4)

    def createEmployeeTouched(self):
        if self.mainWidget is not None:
            print(self.ui.employeeTypeBox.checkedId())
        


class ProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.addEmployeeWindow = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)

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

        #self.ui.employesTable.setModel(EmployeeInterface(self.employes))


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