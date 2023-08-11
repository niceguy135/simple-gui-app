from PySide6.QtCore import QAbstractTableModel, Qt
from logicModels import EmployeeType

class EmployeeInterface(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data


    def rowCount(self, index):
        return len(self._data)


    def columnCount(self, index):
        return 7


    def data(self, index, role):
        if (role == Qt.DisplayRole):
            match(index.column()):
                case 0:
                    return self._data[index.row()].fullName
                case 1:
                    match(self._data[index.row()].empType):
                        case EmployeeType.STD:
                            return "Обычный"
                        case EmployeeType.STUDENT:
                            return "Студент"
                        case EmployeeType.NURSE:
                            return "Медсестра"
                        case EmployeeType.DOC:
                            return "Доктор"
                case 2:
                    return self._data[index.row()].room if \
                        self._data[index.row()].room != '' else "Не применимо"
                case 3:
                    return self._data[index.row()].bonus
                case 4:
                    if hasattr(self._data[index.row()], "workingDays"):
                        return self._data[index.row()].workingDays
                    else:
                        return "Безразницы"
                case 5:
                    return self._data[index.row()].fixPay if \
                        self._data[index.row()].fixPay > 0 else "Не фиксировано"
                case 6:
                    return self._data[index.row()].total

        return None
    

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            match(section):
                case 0:
                    return "ФИО"
                case 1:
                    return "Разряд"
                case 2:
                    return "Кабинет"
                case 3:
                    return "Бонус"
                case 4:
                    return "Колич. дней"
                case 5:
                    return "Фикс. ЗП"
                case 6:
                    return "Итог"

        return None

