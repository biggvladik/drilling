import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from first_window import Ui_MainWindow

class ImageDialog(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface from Designer.
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.get_data)

    def get_data(self):
        P =[]
        H=[]
        for row in range(0,self.ui.tableWidget.rowCount()):
            for column in range(0,self.ui.tableWidget.columnCount()):
                if self.ui.tableWidget.item(row,column) == None:
                    pass
                else:
                    if column == 0:
                        P.append(self.ui.tableWidget.item(row, column).text())

                    elif column ==1:
                        H.append(self.ui.tableWidget.item(row, column).text())
        print(P,H)
        return P,H



app = QApplication(sys.argv)
window = ImageDialog()

window.show()
sys.exit(app.exec())

