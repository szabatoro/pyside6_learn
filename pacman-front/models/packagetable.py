from PySide6.QtCore import QAbstractTableModel, Qt

class UpdateTable(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data 
        self._headers = ["Package", "Installed Version", "New Version", "Repo"]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):  
        if role == Qt.DisplayRole: 
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole): 
        if role == Qt.DisplayRole: 
            if orientation == Qt.Horizontal: 
                return self._headers[section]
            else:
                return str(section + 1)
        return None

class InstallTable(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self._headers = ["Package", "Version", "Repo"]

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):  
        if role == Qt.DisplayRole: 
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole): 
        if role == Qt.DisplayRole: 
            if orientation == Qt.Horizontal: 
                return self._headers[section]
            else:
                return str(section + 1)
        return None