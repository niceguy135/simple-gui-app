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
                    return self._data[index.row()].name
                case 1:
                    return self._data[index.row()].totalSumReport
                case 2:
                    return self._data[index.row()].percent
                case 3:
                    return self._data[index.row()].result

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


class ReportView():
    __dictionary = dict(name="Unknow report",
                 totalSumReport=0,
                 percent=0)

    def __init__(self, **kargs):
        self.__dict__.update(self.__dictionary)
        self.__dict__.update(kargs)
        self.result = 0
