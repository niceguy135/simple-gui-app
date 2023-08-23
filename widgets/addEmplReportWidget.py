import uiFiles.addEmplToReport_maket_ui as addEmplToReport_maket

from PySide6.QtWidgets import QWidget, QHeaderView
from viewInterfaces.addEmplReportModel import AddEmplReportInterface
from viewInterfaces.addReportModel import AddReportInterface


class AddEmployeeToReportWidget(QWidget):
    def __init__(self, mainWid=None, parent=None):
        super().__init__()
        self.mainWidget = mainWid
        self.reportWidget = parent

        self.ui = addEmplToReport_maket.Ui_Form()
        self.ui.setupUi(self)

        self.ui.employeeTable.setModel(AddEmplReportInterface(self.mainWidget.employes))
        self.ui.employeeTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.ui.employeeTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)


    def addEmployee(self):
        if self.ui.employeeTable.selectionModel().hasSelection():
            for selectedRow in self.ui.employeeTable.selectionModel().selectedRows():
                self.reportWidget.selectedEmpls.append([
                    self.mainWidget.employes[selectedRow.row()],
                    self.ui.spinBox.value()
                ])
            self.reportWidget.ui.tableView.setModel(AddReportInterface(self.reportWidget.selectedEmpls))
            self.reportWidget.addEmplWid = None