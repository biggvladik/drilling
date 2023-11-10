import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidget, QTableWidgetItem
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Создаем кнопку и таблицу
        self.button = QPushButton("Создать PDF файл", self)
        self.button.clicked.connect(self.create_pdf)

        self.table_widget = QTableWidget(3, 3)
        self.table_widget.setItem(0, 0, QTableWidgetItem("1"))
        self.table_widget.setItem(0, 1, QTableWidgetItem("2"))
        self.table_widget.setItem(0, 2, QTableWidgetItem("3"))
        self.table_widget.setItem(1, 0, QTableWidgetItem("4"))
        self.table_widget.setItem(1, 1, QTableWidgetItem("5"))
        self.table_widget.setItem(1, 2, QTableWidgetItem("6"))
        self.table_widget.setItem(2, 0, QTableWidgetItem("7"))
        self.table_widget.setItem(2, 1, QTableWidgetItem("8"))
        self.table_widget.setItem(2, 2, QTableWidgetItem("9"))

        self.setCentralWidget(self.table_widget)
        self.setGeometry(300, 300, 400, 300)

    def create_pdf(self):
        # Получаем данные таблицы и создаем PDF файл
        data = []
        for row in range(self.table_widget.rowCount()):
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item is not None:
                    data.append(item.text())

        pdf_file = "example.pdf"

        c = canvas.Canvas(pdf_file, pagesize=letter)

        # Записываем данные в PDF файл
        x = 50
        y = 750
        for item in data:
            c.drawString(x, y, item)
            y -= 20
            if y < 50:
                c.showPage()
                y = 750

        c.save()

        print("PDF файл создан!")

        self.close()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
