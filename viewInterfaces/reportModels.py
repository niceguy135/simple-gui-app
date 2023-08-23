from PySide6.QtCore import QAbstractTableModel, Qt

class ReportInterface(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data


    def rowCount(self, index):
        return len(self._data)


    def columnCount(self, index):
        return 4


    def data(self, index, role):
        if (role == Qt.DisplayRole):
            match(index.column()):
                case 0:
                    return self._data[index.row()][0].reportName
                case 1:
                    return self._data[index.row()][0].totalEarn
                case 2:
                    return self._data[index.row()][1][1]
                case 3:
                    return self._data[index.row()][0].calcClearPayment(
                        self._data[index.row()][1][1]
                    )

        return None
    

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        """ Set the headers to be displayed. """

        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            match(section):
                case 0:
                    return "Название отчета"
                case 1:
                    return "Общая сумма"
                case 2:
                    return "Процент для выбранного сотрудника"
                case 3:
                    return "Итог без перерассчета"

        return None
    

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        
        return super().flags(index) | Qt.ItemIsEditable


    def setData(self, index, value, role):
        if role == Qt.EditRole:
            
            match(index.column()):
                case 0:
                    self._data[index.row()][0].reportName = str(value)
                case 1:
                    self._data[index.row()][0].totalEarn = int(value)
                case 2:
                    self._data[index.row()][1][1] = int(value)

            self.dataChanged.emit(index, index, (Qt.DisplayRole, ))
            return True

        return False
