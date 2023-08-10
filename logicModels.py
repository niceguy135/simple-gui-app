from enum import Enum


class EmployeeType(Enum):
    STD = 1
    STUDENT = 2
    NURSE = 3
    DOC = 4


class Employee():
    _curUUID = 1    

    def __init__(self, empType, name="Безымянный", room="Без кабинета", bonus=0, fixPay=0):
        self.uuid = self._curUUID
        self.empType = empType
        self.fullName = name
        self.room = room
        self.bonus = bonus
        self.fixPay = fixPay
        self.total = 0

        Employee._curUUID += 1
    

    def calculatePayment(self):
        pass


class Specialist(Employee):
    def __init__(self, empType, name="Безымянный", room="Без кабинета", bonus=0, fixPay=0, taxValue=0, workingDays=0):
        super().__init__(empType, name, room, bonus, fixPay)

        self.taxValue = taxValue
        self.workingDays = workingDays
        self.reportList = list()


    def recalculateTaxs(self):
        pass


class Report():
    _curUUID = 1


    def __init__(self, reportName, totalEarn, percPay, percConsum):
        self.uuid = Report._curUUID
        self.reportName = reportName
        self.totalEarn = totalEarn
        self.percPay = percPay
        self.percConsum = percConsum
        self.employeeList = list()

        Report._curUUID += 1


    def calcClearPayment(self):
        pass