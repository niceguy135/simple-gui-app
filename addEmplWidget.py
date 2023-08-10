import addEmployee_maket_ui as addEmplWindow

from PySide6.QtWidgets import QWidget
from logicModels import Employee, Specialist, EmployeeType
from employeModels import EmployeeInterface


class ClassFactory():
    def __init__(self, parentWid):
        self.parentWid = parentWid


    def createEmployee(self):
        constructor = self._get_constructor()
        return constructor()


    def _get_constructor(self):
        if self.parentWid.ui.employeeTypeBox.checkedId() == 1:
            return self._create_standart
        elif self.parentWid.ui.employeeTypeBox.checkedId() > 1:
            return self._create_specialist


    def _create_standart(self):
        return Employee(
                        empType = EmployeeType.STD,
                        name = self.parentWid.ui.fullNameEdit.text(),
                        room = self.parentWid.ui.roomEdit.text(),
                        fixPay = int(self.parentWid.ui.fixPayPin.value())
                        )


    def _create_specialist(self):
        match(self.parentWid.ui.employeeTypeBox.checkedId()):
            case 2:
                curType = EmployeeType.STUDENT
            case 3:
                curType = EmployeeType.NURSE
            case 4:
                curType = EmployeeType.DOC
        return Specialist(
                        empType = curType,
                        name = self.parentWid.ui.fullNameEdit.text(),
                        room = self.parentWid.ui.roomEdit.text(),
                        fixPay = int(self.parentWid.ui.fixPayPin.value()),
                        taxValue = int(self.parentWid.ui.startValueBox.value()),
                        workingDays = int(self.parentWid.ui.workedDaysBox.value())
                    )


class AddEmployeeWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.mainWidget = parent
        self.factory = ClassFactory(self)

        self.ui = addEmplWindow.Ui_Form()
        self.ui.setupUi(self)

        self.ui.employeeTypeBox.setId(self.ui.isStandart, 1)
        self.ui.employeeTypeBox.setId(self.ui.isStudent, 2)
        self.ui.employeeTypeBox.setId(self.ui.isNurse, 3)
        self.ui.employeeTypeBox.setId(self.ui.isDoctor, 4)

    def createEmployeeTouched(self):
        if self.mainWidget is not None:
            self.mainWidget.employes.append(self.factory.createEmployee())
            self.mainWidget.ui.employesTable.setModel(EmployeeInterface(self.mainWidget.employes))