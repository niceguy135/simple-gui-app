import sys
import os
import platform
import xlsxwriter

from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QHeaderView, QMenu, QFileDialog
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
        self.ui.employesTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.employesTable.setModel(EmployeeInterface(self.employes))
        self.ui.employesTable.customContextMenuRequested.connect(self.CustomContextMenuEmpl)
        

        self.ui.employesTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        self.ui.employesTable.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)


        self.reports = list()
        self.ui.repotsTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.repotsTable.setModel(ReportInterface(self.reports))
        self.ui.repotsTable.customContextMenuRequested.connect(self.CustomContextMenuReport)
        
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.repotsTable.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)

        self.selectedReports = list()

        self.emplMenu = QMenu(self)
        self.deleteEmplOpt = self.emplMenu.addAction("Удалить")
        self.deleteEmplOpt.triggered.connect(self.DeleteSelectedEmpl)

        self.reportMenu = QMenu(self)
        self.deleteReportOpt = self.reportMenu.addAction("Удалить")
        self.deleteReportOpt.triggered.connect(self.DeleteSelectedReport)


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
        self.calcPressed()

        fileName, filterName = QFileDialog.getSaveFileName(self,
                                               "Куда сохранить Excel файл?",
                                               os.path.join(os.path.dirname(os.path.realpath(__file__)), "saved_Excels"),
                                               "*.xlsx",
                                               "*.xlsx")

        if platform.system() == "Windows":
            workbook = xlsxwriter.Workbook(fileName)
        else:
            workbook = xlsxwriter.Workbook("".join([fileName, filterName[1:]]))

        worksheet = workbook.add_worksheet("Зарплаты сотрудникам")
        
        row = 0
        col = 0
        
        for employee in self.employes:
            worksheet.write(row, col, employee.fullName)
            worksheet.write(row, col + 1, employee.total)
            row += 1
        
        workbook.close()


    def rowSelected(self):
        if self.ui.employesTable.selectionModel().hasSelection():
            self.selectedReports.clear()

            for selectedRow in self.ui.employesTable.selectionModel().selectedRows():
                selectedEmpl = self.employes[selectedRow.row()]
                for curReport in self.reports:
                    for curEmplPerc in curReport.employeeList:
                        if curEmplPerc[0].uuid == selectedEmpl.uuid:
                            self.selectedReports.append([curReport, curEmplPerc])
            
            self.ui.repotsTable.setModel(ReportInterface(self.selectedReports))

    
    def CustomContextMenuEmpl(self, point):
        self.emplMenu.exec(self.ui.employesTable.mapToGlobal(point))


    def CustomContextMenuReport(self, point):
        self.reportMenu.exec(self.ui.repotsTable.mapToGlobal(point))

    
    def DeleteSelectedEmpl(self):
        if self.ui.employesTable.selectionModel().hasSelection():

            for selectedRow in self.ui.employesTable.selectionModel().selectedRows():
                removingEmpl = self.employes.pop(selectedRow.row())

                for curReport in self.reports:
                    for ind, curEmplPerc in enumerate(curReport.employeeList):
                        if curEmplPerc[0].uuid == removingEmpl.uuid:
                            curReport.employeeList.pop(ind)
        
            self.ui.employesTable.setModel(EmployeeInterface(self.employes))


    def DeleteSelectedReport(self):
        if self.ui.repotsTable.selectionModel().hasSelection():
            selcetedEmplRow = self.ui.employesTable.selectionModel().selectedRows()
            selectedEmpl = self.employes[selcetedEmplRow[0].row()]

            for selectedRow in self.ui.repotsTable.selectionModel().selectedRows():
                deletedReport = self.selectedReports.pop(selectedRow.row())

                for report in self.reports:
                    if report.uuid == deletedReport[0].uuid:
                        for ind, employee in enumerate(report.employeeList):
                            if employee[0].uuid == selectedEmpl.uuid:
                                report.employeeList.pop(ind)

            self.ui.repotsTable.setModel(ReportInterface(self.selectedReports))
    

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = ProgramWindow()
    mainWindow.show()

    sys.exit(app.exec())