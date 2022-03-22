from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2
from models.Products import Products


class AddView_Window(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(536, 549)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(110, 170, 400, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(400, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.addProduct = QtWidgets.QPushButton(self.centralwidget)
        self.addProduct.setGeometry(QtCore.QRect(0, 430, 275, 120))
        self.addProduct.setObjectName("addProduct")
        self.otmena = QtWidgets.QPushButton(self.centralwidget)
        self.otmena.setGeometry(QtCore.QRect(270, 430, 275, 120))
        self.otmena.setObjectName("otmena")
        self.spinforRow = QtWidgets.QSpinBox(self.centralwidget)
        self.spinforRow.setGeometry(QtCore.QRect(10, 210, 61, 51))
        self.spinforRow.setObjectName("spinforRow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # подключение кнопки добавления
        self.addProduct.clicked.connect(self.getData)
        # подключение кнопки для добавления строки
        self.spinforRow.valueChanged.connect(self.change)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Window"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Barcode"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.addProduct.setText(_translate("MainWindow", "Добавить в меню "))
        self.otmena.setText(_translate("MainWindow", "Отмена"))

    def change(self):
        self.tableWidget.setRowCount(int(self.spinforRow.text()))


    def getData(self):
        rows = self.tableWidget.rowCount()
        cols = self.tableWidget.columnCount()
        data = []
        for row in range(rows):
            tmp = []
            for col in range(cols):
                try:
                    tmp.append(self.tableWidget.item(row, col).text())
                except:
                    tmp.append("")
            data.append(tmp)
        for i in data:
            print(i)
            db = Products()
            db.add(i[0], i[1], i[2])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AddView_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())