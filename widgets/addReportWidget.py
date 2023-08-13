import uiFiles.addReport_maket_ui as addReportWindow

from PySide6.QtWidgets import QWidget
from logicModels import Report
from viewInterfaces.employeModels import EmployeeInterface


class AddEmployeeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainWidget = parent

        self.ui = addReportWindow.Ui_Form()
        self.ui.setupUi(self)

    def createReportTouched(self):
        if self.mainWidget is not None:
            self.mainWidget.reports.append(Report(
                reportName = self.ui.reportEdit.text(),
                totalEarn = self.ui.totalEarnSpin.value(),
                percPay = self.ui.percPaySpin.value(),
                percConsum = self.ui.percConsumSpin.value()
            ))
            self.mainWidget.ui.employesTable.setModel(EmployeeInterface(self.mainWidget.reports))