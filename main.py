import sys
import traceback

from PyQt5.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from window import Ui_MainWindow
from CPG import CPG
from well_construction import construction
intervals = 0
from wk import Well
class ImageDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.get_data)
        self.ui.pushButton_2.clicked.connect(self.get_graph)
        self.ui.comboBox.currentTextChanged.connect(self.check_label)
        self.well = None
        self.ui.pushButton_4.clicked.connect(self.calculate_table)
        self.check_label()

        try:
            self.test_table()
        except:
            print(traceback.format_exc())

    def get_data(self):
        try:
            P =[]
            H=[]
            for row in range(0,self.ui.tableWidget.rowCount()):
                for column in range(0,self.ui.tableWidget.columnCount()):
                    if self.ui.tableWidget.item(row,column) == None:
                        pass
                    else:
                        if column == 0:
                            P.append(float(self.ui.tableWidget.item(row, column).text()))

                        elif column ==1:
                            H.append(float(self.ui.tableWidget.item(row, column).text()))
            self.well  = Well(H, P, self.ui.comboBox.currentText(), int(self.ui.lineEdit.text()))
            self.well.coefficients()
            self.well.compatible_conditions()
            intervals = self.well.condi[0]
            for i in range(len(intervals)):
                self.ui.tableWidget_3.setItem(0, i, QTableWidgetItem(str(intervals[i])))

        except:
            print(traceback.format_exc())


    def get_graph(self):
        try:
            intervals = []

            for column in range(4):
                item = self.ui.tableWidget_3.item(column, 0)
                if item is not None:
                    intervals.append(float(item.text()))
            self.well.condi[0] = intervals
        except:
            print(traceback.format_exc())
        try:
            self.well.graphic()
        except:
            print(traceback.format_exc())

    def check_label(self):
        if self.ui.comboBox.currentText() == 'Нефтяная':
            self.ui.label_4.setText('т/сутки')
        else:
            self.ui.label_4.setText('м^3/сутки')


    def calculate_table(self):
        try:
            # Меняем интервалы в классе, если их изменили
            data = self.well.construction()
            self.ui.lineEdit_2.setText(str(self.well.cementing()))

            print(data)

            N = [ i for i in data[0].values()]
            K = [ i for i in data[1].values()]
            E = [ i for i in data[-1].values()]
            P_1 = False
            P_2 = False
            if len(data) ==4:
                P_1 = [ i for i in data[2].values()]

            if len(data) ==5:
                P_1 = [ i for i in data[2].values()]
                P_2 = [i for i in data[3].values()]

            for column in range(0, self.ui.tableWidget_2.columnCount()):
                for row in range(0, self.ui.tableWidget_2.rowCount()):
                    if column == 0:
                        print(type(row))
                        self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(N[row])))

                    elif column == 1:
                        self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(K[row])))
                    elif column == 4:
                        self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(E[row])))

                    elif column == 2 and P_1:
                        self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(P_1[row])))

                    elif column == 3 and P_2:
                        self.ui.tableWidget_2.setItem(row, column, QTableWidgetItem(str(P_2[row])))
        except:
            print(traceback.format_exc())


    def test_table(self):
        H = [200, 500, 900, 1400, 1800, 2000, 2340, 2700, 2950, 3300]
        Pre = [2.1, 6.05, 7.96, 12.56, 18, 29.67, 27.31, 30.93, 31.42, 37.09]

        for row in range(len(H)):
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(str(H[row])))


        for row in range(len(Pre)):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(Pre[row])))
















app = QApplication(sys.argv)
window = ImageDialog()
window.show()
sys.exit(app.exec())






