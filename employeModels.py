from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

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
                    return self._data[index.row()].name
                case 1:
                    return self._data[index.row()].room
                case 2:
                    return self._data[index.row()].percent
                case 3:
                    return self._data[index.row()].staticPay
                case 4:
                    return self._data[index.row()].days
                case 5:
                    return self._data[index.row()].bonus
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
                    return "Кабинет"
                case 2:
                    return "Процент"
                case 3:
                    return "Фикс. зарплата"
                case 4:
                    return "Колич. дней"
                case 5:
                    return "Надбавка"
                case 6:
                    return "Итог"

        return None


class Employee():
    __dictionary = dict(name="Unknow",
                 room=0,
                 percent=0,
                 staticPay=0,
                 days=0,
                 bonus=0)

    def __init__(self, **kargs):
        self.__dict__.update(self.__dictionary)
        self.__dict__.update(kargs)
        self.total = 0
