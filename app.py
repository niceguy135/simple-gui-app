import sys
from random import randint

from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QWidget

#макеты окон
from uiFiles.first_maket_ui import Ui_Form

#виджеты
from widgets.addEmplWidget import AddEmployeeWidget
from widgets.addReportWidget import AddReportWidget

#интерфейсы для вьюшек и сами вьюшки
from viewInterfaces.employeModels import EmployeeInterface
from viewInterfaces.reportModels import ReportInterface


class ProgramWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.addEmployeeWindow = None
        self.addReportWindow = None

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

        self.selectedReports = None


    def addEmployeePressed(self):
        if self.addEmployeeWindow is None:
            self.addEmployeeWindow = AddEmployeeWidget(parent=self)
            self.addEmployeeWindow.show()
        else:
            self.addEmployeeWindow.close()
            self.addEmployeeWindow = None


    def addReportPressed(self):
        if self.addReportWindow is None:
            self.addReportWindow = AddReportWidget(parent=self)
            self.addReportWindow.show()
        else:
            self.addReportWindow.close()
            self.addReportWindow = None


    def calcPressed(self):
        for employee in self.employes:
            employee.total = 0

        for report in self.reports:
            for employee, percent in report.employeeList:
                employee.total += report.calcClearPayment(percent)

        for employee in self.employes:
            employee.calculatePayment()

        self.ui.employesTable.setModel(EmployeeInterface(self.employes))

    def savePressed(self):
        print("Save")


    def rowSelected(self):
        if self.ui.employesTable.selectionModel().hasSelection():
            del self.selectedReports
            self.selectedReports = list()

            for selectedRow in self.ui.employesTable.selectionModel().selectedRows():
                selectedEmpl = self.employes[selectedRow.row()]
                for curReport in self.reports:
                    for curEmpl, curPerc in curReport.employeeList:
                        if curEmpl.uuid == selectedEmpl.uuid:
                            self.selectedReports.append((curReport, curPerc))
            
            self.ui.repotsTable.setModel(ReportInterface(self.selectedReports))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = ProgramWindow()
    mainWindow.show()

    sys.exit(app.exec())