from enum import Enum
from datetime import datetime, timedelta
import calendar

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
        if self.fixPay > self.total:
            self.total = self.fixPay

        self.total += self.bonus


class Specialist(Employee):

    _curMonth = datetime.now().month
    _curYear = datetime.now().year
    _lastMonthDay = calendar.monthrange(_curYear, _curMonth)[1]

    def __init__(self, empType, name="Безымянный", room="Без кабинета", bonus=0, fixPay=0, taxValue=0, workingDays=0):
        super().__init__(empType, name, room, bonus, fixPay)

        self.taxValue = taxValue
        self.workingDays = workingDays


    def calculatePayment(self):
        super().calculatePayment()
        self._recalculateTaxs()


    def _recalculateTaxs(self):
        
        firstMonthDay = datetime(Specialist._curYear, Specialist._curMonth, 1)
        lastMonthDay = datetime(Specialist._curYear, Specialist._curMonth, Specialist._lastMonthDay)

        dates = (firstMonthDay + timedelta(idx + 1)
                for idx in range((lastMonthDay - firstMonthDay).days))
        
        res = sum(1 for day in dates if day.weekday() < 5)

        self.total -= self.taxValue * (self.workingDays / res)


class Report():
    _curUUID = 1


    def __init__(self, reportName, totalEarn, percPay, percConsum, employeeList=list()):
        self.uuid = Report._curUUID
        self.reportName = reportName
        self.totalEarn = totalEarn
        self.percPay = percPay
        self.percConsum = percConsum
        self.employeeList = employeeList.copy()

        Report._curUUID += 1


    def calcClearPayment(self, emplPercent):
        return ((self.totalEarn * (self.percConsum / 100)) * (self.percPay / 100)) * (emplPercent / 100)
    