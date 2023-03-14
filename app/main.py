import sys
from PyQt6.QtWidgets import QApplication, QMainWindow,QTableWidgetItem
from first_window import Ui_MainWindow
from CPG import CPG
from well_construction import construction
H_intervals = 0
intervals = 0
class ImageDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.get_data)
        self.ui.pushButton_2.clicked.connect(self.get_graph)
        self.ui.comboBox.currentTextChanged.connect(self.check_label)
        self.ui.pushButton_3.clicked.connect(self.calculate_table)

    def get_data(self):
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
        print(H,P)
        return H,P

    def get_graph(self):
        global H_intervals
        global intervals
        H,P = self.get_data()
        H_intervals, intervals, graph = CPG(H,P)
        self.ui.lineEdit_2.setText(str(intervals))

    def check_label(self):
        if self.ui.comboBox.currentText() == 'Нефтяная':
            self.ui.label_4.setText('т/сутки')
        else:
            self.ui.label_4.setText('м^3/сутки')


    def calculate_table(self):
        # Q = int(self.ui.lineEdit.text())
        # print(H_intervals,intervals,Q)
        # data = construction(H_intervals,intervals,Q,'Oil')
        # print(data)

        data = [{'H_intervals': 40, 'Db': 320, 'Dm': 269.9, 'D': 244.5, 'd': 224.5, 's': 10.0, 'size': 245},
                {'H_intervals': 2000, 'Db': 222.3, 'Dm': 187.7, 'D': 168.3, 'd': 144.1, 's': 12.1, 'size': 168},
                {'H_intervals': 3450, 'Db': 139.7, 'Dm': 127, 'D': 114.3, 'd': 101.5, 's': 6.4, 'size': 114}]

        N = data[0]
        K = data[1]
        E = data[-1]
        count = 1
        for column in range(0, self.ui.tableWidget_2.columnCount()):
            for row in range(0, self.ui.tableWidget_2.rowCount()):
                self.ui.tableWidget_2.setItem(row,column,QTableWidgetItem(str(count)))
                if column == 0:
                    if row == 0:










app = QApplication(sys.argv)
window = ImageDialog()

window.show()



print(window.ui.comboBox.currentText())
sys.exit(app.exec())






