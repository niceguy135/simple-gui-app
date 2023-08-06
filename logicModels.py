class Employee():
    _curUUID = 1    

    def __init__(self, name, bonus, fixPay):
        self.uuid = self.curUUID
        self.fullName = name
        self.bonus = bonus
        self.fixPay = fixPay
        self.total = 0

        Employee._curUUID += 1
    

    def calculatePayment(self):
        pass


class Specialist(Employee):
    def __init__(self, name, bonus, fixPay, taxValue, workingDays):
        super().__init__(name, bonus, fixPay)

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