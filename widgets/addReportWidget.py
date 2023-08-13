import uiFiles.addReport_maket_ui as addReportWindow

from PySide6.QtWidgets import QWidget, QHeaderView
from logicModels import Report

from viewInterfaces.addReportModel import AddReportInterface

from .addEmplReportWidget import AddEmployeeToReportWidget



class AddReportWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainWidget = parent
        self.addEmplWid = None

        self.ui = addReportWindow.Ui_Form()
        self.ui.setupUi(self)

        self.selectedEmpls = list()
        self.ui.tableView.setModel(AddReportInterface(self.selectedEmpls))
        self.ui.tableView.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

    
    def addEmployee(self):
        if self.addEmplWid is None:
            self.addEmplWid = AddEmployeeToReportWidget(mainWid=self.mainWidget, parent=self)
            self.addEmplWid.show()
        else:
            self.addEmplWid.close()
            self.addEmplWid = None

    
    def deleteEmployee(self):
        if self.ui.tableView.selectionModel().hasSelection():
            for selectedRow in self.ui.tableView.selectionModel().selectedRows():
                del self.selectedEmpls[selectedRow.row()]
        self.ui.tableView.setModel(AddReportInterface(self.selectedEmpls))


    def createReport(self):
        if self.mainWidget is not None:
            self.mainWidget.reports.append(Report(
                reportName = self.ui.reportEdit.text(),
                totalEarn = self.ui.totalEarnSpin.value(),
                percPay = self.ui.percPaySpin.value(),
                percConsum = self.ui.percConsumSpin.value(),
                employeeList=self.selectedEmpls
            ))
            self.mainWidget.addReportWindow = None