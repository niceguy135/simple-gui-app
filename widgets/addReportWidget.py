import uiFiles.addReport_maket_ui as addReportWindow

from PySide6.QtWidgets import QWidget
from logicModels import Report
from viewInterfaces.employeModels import EmployeeInterface

from .addEmplReportWidget import AddEmployeeToReportWidget


class AddReportWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainWidget = parent
        self.addEmplWid = None
        
        self.selectedEmpls = list()

        self.ui = addReportWindow.Ui_Form()
        self.ui.setupUi(self)

    
    def addEmployee(self):
        if self.addEmplWid is None:
            self.addEmplWid = AddEmployeeToReportWidget(mainWid=self.mainWidget, parent=self)
            self.addEmplWid.show()
        else:
            self.addEmplWid.close()
            self.addEmplWid = None

    
    def deleteEmployee(self):
        pass


    def createReport(self):
        if self.mainWidget is not None:
            self.mainWidget.reports.append(Report(
                reportName = self.ui.reportEdit.text(),
                totalEarn = self.ui.totalEarnSpin.value(),
                percPay = self.ui.percPaySpin.value(),
                percConsum = self.ui.percConsumSpin.value()
            ))
            self.mainWidget.ui.employesTable.setModel(EmployeeInterface(self.mainWidget.reports))