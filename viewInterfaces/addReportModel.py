from PySide6.QtCore import QAbstractTableModel, Qt

class AddReportInterface(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data


    def rowCount(self, index):
        return len(self._data)


    def columnCount(self, index):
        return 3


    def data(self, index, role):
        if (role == Qt.DisplayRole):
            match(index.column()):
                case 0:
                    return self._data[index.row()][0].uuid
                case 1:
                    return self._data[index.row()][0].fullName
                case 2:
                    return self._data[index.row()][1]
        return None
    

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            match(section):
                case 0:
                    return "UUID"
                case 1:
                    return "ФИО сотрудника"
                case 2:
                    return "Процент зарплаты"

        return None

