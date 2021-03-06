import sys
from PyQt5.QtCore import QSize, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QTableView, QGridLayout, QTableWidget, QTableWidgetItem

from models.Products import Products


class HomeView(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 811, 611))
        self.tabWidget.setMaximumSize(QtCore.QSize(811, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.homeTab = QtWidgets.QWidget()
        self.homeTab.setObjectName("homeTab")
        self.label = QtWidgets.QLabel(self.homeTab)
        self.label.setGeometry(QtCore.QRect(280, 80, 281, 121))
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.homeTab)
        self.label_4.setGeometry(QtCore.QRect(40, 70, 691, 181))
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.homeTab)
        self.label_5.setGeometry(QtCore.QRect(180, 260, 391, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.tabWidget.addTab(self.homeTab, "")



        self.showTab = QtWidgets.QWidget()
        self.showTab.setObjectName("showTab")
        self.productView = QtWidgets.QTableView(self.showTab)
        self.productView.setGeometry(QtCore.QRect(30, 70, 731, 451))
        self.productView.setStyleSheet("")
        self.productView.setObjectName("productView")
        self.label_3 = QtWidgets.QLabel(self.showTab)
        self.label_3.setGeometry(QtCore.QRect(230, 10, 351, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.tabWidget.addTab(self.showTab, "")

        grid_layout = QGridLayout()  # ?????????????? QGridLayout
        self.showTab.setLayout(grid_layout)  # ?????????????????????????? ???????????? ???????????????????? ?? ?????????????????????? ????????????

        table = QTableWidget()  # ?????????????? ??????????????
        table.setColumnCount(3)  # ?????????????????????????? ?????? ??????????????

        # ?????????????????????????? ?????????????????? ??????????????
        table.setHorizontalHeaderLabels(["barcode", "name of product", "price"])


        all_products = self.get_all_products()
        row = len(all_products)
        table.setRowCount(row)  # ?????????????????????????? ???????????? ?? ??????????????


        # ?????????????????????????? ?????????????????????? ?????????????????? ???? ??????????????????
        table.horizontalHeaderItem(0).setToolTip("barcode")
        table.horizontalHeaderItem(1).setToolTip("name of product")
        table.horizontalHeaderItem(2).setToolTip("price")

        # ?????????????????????????? ???????????????????????? ???? ??????????????????
        table.horizontalHeaderItem(0).setTextAlignment(Qt.AlignLeft)
        table.horizontalHeaderItem(1).setTextAlignment(Qt.AlignHCenter)
        table.horizontalHeaderItem(2).setTextAlignment(Qt.AlignRight)
        count_column = 0
        # ??????????????????  ????????????
        for i in all_products:
            table.setItem(count_column, 0, QTableWidgetItem(str(i[1])))
            table.setItem(count_column, 1, QTableWidgetItem(i[2]))
            table.setItem(count_column, 2, QTableWidgetItem(str(i[3])))
            count_column += 1
        # ???????????? ???????????? ?????????????? ???? ??????????????????????
        table.resizeColumnsToContents()
        table.setMinimumSize(QSize(1000, 1000))
        grid_layout.addWidget(table, 0, 0)  # ?????????????????? ?????????????? ?? ??????????


        self.addTab = QtWidgets.QWidget()
        self.addTab.setObjectName("addTab")
        self.tableWidget = QtWidgets.QTableWidget(self.addTab)
        self.tableWidget.setGeometry(QtCore.QRect(120, 70, 600, 200))
        self.tableWidget.setMaximumSize(QtCore.QSize(600, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(17)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(20)
        item.setFont(font)
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.spinforRow = QtWidgets.QSpinBox(self.addTab)
        self.spinforRow.setGeometry(QtCore.QRect(30, 160, 61, 51))
        self.spinforRow.setWrapping(False)
        self.spinforRow.setMinimum(1)
        self.spinforRow.setMaximum(150)
        self.spinforRow.setStepType(QtWidgets.QAbstractSpinBox.DefaultStepType)
        self.spinforRow.setObjectName("spinforRow")
        self.otmena = QtWidgets.QPushButton(self.addTab)
        self.otmena.setGeometry(QtCore.QRect(80, 390, 275, 120))
        self.otmena.setStyleSheet("")
        self.otmena.setObjectName("otmena")
        self.addProduct = QtWidgets.QPushButton(self.addTab)
        self.addProduct.setGeometry(QtCore.QRect(440, 390, 275, 120))
        self.addProduct.setObjectName("addProduct")
        self.tabWidget.addTab(self.addTab, "")


        self.orderTab = QtWidgets.QWidget()
        self.orderTab.setObjectName("orderTab")
        self.label_2 = QtWidgets.QLabel(self.orderTab)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 471, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setLineWidth(12)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.tableWidget_order = QtWidgets.QTableWidget(self.orderTab)
        self.tableWidget_order.setGeometry(QtCore.QRect(10, 80, 780, 251))
        self.tableWidget_order.setMaximumSize(QtCore.QSize(780, 400))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.tableWidget_order.setFont(font)
        self.tableWidget_order.setObjectName("tableWidget_order")
        self.tableWidget_order.setColumnCount(4)
        self.tableWidget_order.setRowCount(100)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_order.setHorizontalHeaderItem(3, item)
        self.tableWidget_order.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_order.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_order.horizontalHeader().setMinimumSectionSize(68)
        self.tableWidget_order.verticalHeader().setDefaultSectionSize(28)
        self.tableWidget_order.verticalHeader().setMinimumSectionSize(28)
        self.submitbtn = QtWidgets.QPushButton(self.orderTab)
        self.submitbtn.setGeometry(QtCore.QRect(460, 340, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.submitbtn.setFont(font)
        self.submitbtn.setObjectName("sumbit")
        self.sum = QtWidgets.QLabel(self.orderTab)

        # self.sum.setAlignment(QtCore.Qt.AlignCenter)
        # self.sum.setObjectName("sum")
        self.spinBox_for_order = QtWidgets.QSpinBox(self.orderTab)
        self.spinBox_for_order.setGeometry(QtCore.QRect(30, 340, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.spinBox_for_order.setFont(font)
        self.spinBox_for_order.setWrapping(False)
        self.spinBox_for_order.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_for_order.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.spinBox_for_order.setMinimum(1)
        self.spinBox_for_order.setMaximum(10)
        self.spinBox_for_order.setObjectName("spinBox_for_order")
        self.pay_btn = QtWidgets.QPushButton(self.orderTab)
        self.pay_btn.setGeometry(QtCore.QRect(460, 450, 321, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pay_btn.setFont(font)
        self.pay_btn.setObjectName("pay_btn")

        self.label_result = QtWidgets.QLabel(self.orderTab)
        self.label_result.setGeometry(QtCore.QRect(200, 350, 400, 60))
        self.label_result.setFont(font)
        self.label_result.setText("0")


        self.tabWidget.addTab(self.orderTab, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # ?????????????????????? ???????????? ????????????????????
        self.addProduct.clicked.connect(self.getData)
        self.text_barcode = QtWidgets.QTextEdit(self.orderTab)
        self.text_barcode.setGeometry(QtCore.QRect(30, 440, 200, 50))
        self.text_barcode.setStyleSheet("font-family: \'Montserrat\';\n"
                                        "font-size: 15px;\n"
                                        "background-color: rgb(238, 238, 236);")
        self.text_barcode.setObjectName("text_barcode")

        # if len(self.text_barcode.toPlainText()) > 1:
        #     self.start_order()
        # ?????????????????????? ???????????? ?????? ???????????????????? ????????????
        self.spinforRow.valueChanged.connect(self.change)
        self.submitbtn.clicked.connect(self.start_order)
        self.c_column = 0
        self.count_money = 0
        # self.product = []
    def start_order(self):

        barcode = self.text_barcode.toPlainText()
        product_ = self.get_product(barcode)
        lst = []
        lst2 = []
        print(product_)
        for i in product_:
            lst.append(list(i))

        for i in lst:
            for j in i:
                lst2.append(j)
        print(type(lst2))
            # for j in i:
            #     lst.append(j)
        # self.name = product[1]
        # self.barcode = product[2]
        # self.price = product[3]
        self.tableWidget_order.setItem(self.c_column, 0, QTableWidgetItem(lst2[1]))
        self.tableWidget_order.setItem(self.c_column, 1, QTableWidgetItem(lst2[2]))
        self.tableWidget_order.setItem(self.c_column, 3, QTableWidgetItem(str(lst2[3])))
        self.count_money += int(lst2[3])
        self.c_column += 1
        self.label_result.setText(str(self.count_money))
        self.text_barcode.setText("")
    def get_product(self, barcode):
        product_obj = Products()
        prod = product_obj.get(barcode)
        return prod


        # self.db = QSqlDatabase.addDatabase("QPSQL")
        # self.db.open()
        #
        # self.model = QSqlTableModel()
        # self.model.setTable("some_table")
        # self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        # self.model.select()
        # self.tableView = QTableView()
        # self.tableView.setModel(self.model)

    def get_all_products(self):
        product = Products()
        all_products = product.get_all()
        return all_products

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ALA TOO "))
        self.label_4.setText(_translate("MainWindow", "Welcome to alatoo "))
        self.label_5.setText(_translate("MainWindow", "What u would like to order ?"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.homeTab), _translate("MainWindow", "Home"))
        self.label_3.setText(_translate("MainWindow", "?????? ????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.showTab), _translate("MainWindow", "Show Product"))
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
        self.otmena.setText(_translate("MainWindow", "???????????????? ?? ???????? "))
        self.addProduct.setText(_translate("MainWindow", "????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.addTab), _translate("MainWindow", "Add Product"))
        self.label_2.setText(_translate("MainWindow", "???????? ????????????"))
        item = self.tableWidget_order.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_order.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Barcode"))
        item = self.tableWidget_order.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_order.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Count"))
        item = self.tableWidget_order.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Price"))
        self.submitbtn.setText(_translate("MainWindow", "Submit"))
        self.pay_btn.setText(_translate("MainWindow", "Pay"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orderTab), _translate("MainWindow", "Order Product"))

    # -------------------------------------------------------------------------------------------------------
    # FOR SHOW PRODUCT



    # -------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------
    # FOR ADD PRODUCT

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
            # print(data)
            db.add(i[0], i[1], i[2])

    # -------------------------------------------------------------------------------------------------------

    # -------------------------------------------------------------------------------------------------------
    # FOR ORDER PRODUCTS

    # -------------------------------------------------------------------------------------------------------

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = HomeView()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
main()