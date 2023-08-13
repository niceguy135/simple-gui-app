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
                    return self._data[index.row()][1]
                case 3:
                    return float(self._data[index.row()][0].totalEarn) * \
                        (float(self._data[index.row()][1])/100)

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
