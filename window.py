# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1121, 811))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setGeometry(QtCore.QRect(-20, 0, 1131, 831))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 226, 327))
        self.tableWidget.setStyleSheet("QTableWidget {\n"
"                background-color: rgb(187, 255, 216);\n"
"                border: 2px solid black;\n"
"            }\n"
"QHeaderView::section {\n"
"                background-color: rgb(85, 170, 127);\n"
"                color: #333;\n"
"                border: none;\n"
"            }")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 150, 93, 28))
        self.pushButton.setStyleSheet("QPushButton#pushButton {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color: rgb(170, 170, 255);\n"
"}\n"
"QPushButton#pushButton:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget.setGeometry(QtCore.QRect(270, 30, 236, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setStyleSheet("font: bold 14px;\n"
"max-height: 1em;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    border: 2px solid black;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"\n"
"}\n"
":editable {\n"
"    background: white;\n"
"}\n"
"QComboBox:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.tableWidget_3 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_3.setGeometry(QtCore.QRect(270, 130, 119, 177))
        self.tableWidget_3.setStyleSheet("QTableWidget {\n"
"                background-color: rgb(187, 255, 216);\n"
"                border: 2px solid black;\n"
"            }\n"
"QHeaderView::section {\n"
"                background-color: rgb(85, 170, 127);\n"
"                color: #333;\n"
"                border: none;\n"
"            }")
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(1)
        self.tableWidget_3.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(True)
        self.tableWidget_3.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 190, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.layoutWidget_4 = QtWidgets.QWidget(self.frame_2)
        self.layoutWidget_4.setGeometry(QtCore.QRect(270, 90, 181, 24))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_3.setStyleSheet("font: bold 14px;\n"
"max-height: 1em;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    padding: 0 8px;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_4)
        self.label_5.setStyleSheet("font: bold 14px;\n"
"max-height: 1em;")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 400, 744, 214))
        self.tableWidget_2.setStyleSheet("QTableWidget {\n"
"                background-color: rgb(187, 255, 216);\n"
"                border: 2px solid black;\n"
"            }\n"
"QHeaderView::section {\n"
"                background-color: rgb(85, 170, 127);\n"
"                color: #333;\n"
"                border: none;\n"
"            }")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(170, 170, 255))
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 230, 91, 31))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4 {\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    background-color:rgb(170, 170, 255);\n"
"}\n"
"QPushButton#pushButton_4:hover {\n"
"  background-color: #e7e7e7;\n"
"}\n"
"")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(510, 0, 601, 211))
        self.label_6.setStyleSheet("font: bold 12px;\n"
" background-color: rgb(170, 170, 255)\n"
"\n"
"")
        self.label_6.setObjectName("label_6")
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setGeometry(QtCore.QRect(270, 60, 198, 22))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(50, 17))
        self.label_2.setStyleSheet("font: bold 14px;\n"
"max-height: 1em;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(70, 16777215))
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"    border: 2px solid gray;\n"
"    padding: 0 8px;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(80, 0))
        self.label_4.setStyleSheet("font: bold 14px;\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.frame_4 = QtWidgets.QFrame(self.tab_3)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 1021, 651))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setTabletTracking(False)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainWindow", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainWindow", "10"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "P, МПа"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "H,м"))
        self.pushButton.setText(_translate("MainWindow", "Готово"))
        self.label.setText(_translate("MainWindow", "ТИП СКВАЖИНЫ"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Нефтяная"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Газовая"))
        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_3.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_3.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_3.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_3.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Глубина спуска"))
        self.pushButton_2.setText(_translate("MainWindow", "График"))
        self.label_3.setText(_translate("MainWindow", "V цемента"))
        self.label_5.setText(_translate("MainWindow", "м^3"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Диаметр долота, мм"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Диаметр муфты, мм"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Наружный диаметр, мм"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Внутренний диаметр,мм"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Толщина стенки обсадной колонны, мм"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("MainWindow", "Типоразмер обсадной колонны"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("MainWindow", "Глубина спуска обсадной колонны,м"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Направление"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Кондуктор"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Промежуточная"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Промежуточная"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Эксп."))
        self.pushButton_4.setText(_translate("MainWindow", "Расчитать"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ИНСТРУКЦИЯ</p><p>&quot;Готово&quot; - рассчитает глубины спуска</p><p>( Необходимо заполнить 1-ую таблицы и ввести дебит скважины )</p><p>&quot;График&quot; - построит график совмещенных давлений</p><p>( Необходимо заполнить 1-ую таблицу и рассчитать/ввести глубины спуска )</p><p>&quot;Расчитать&quot; - рассчитает диаметры</p><p>( Необходимы глубины спуска и дебит )</p><p>Если ничего не происходит, значит вы ввели что-то не так, или оно сломалось!!</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "ДЕБИТ"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "1 страница"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "3 страница"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "2 страница"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())