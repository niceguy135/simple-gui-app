import uiFiles.addEmplToReport_maket_ui as addEmplToReport_maket

from PySide6.QtWidgets import QWidget, QHeaderView
from viewInterfaces.addEmplReportModel import AddEmplReportInterface


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
            print(self.ui.employeeTable.selectionModel().selectedRows())