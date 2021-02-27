import sys
import sqlite3

from PyQt5.QtWidgets import *
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800, 600)
        self.setWindowTitle('Каталог')

        uic.loadUi('main.ui', self)

        self.con = sqlite3.connect('coffee.sqlite')
        self.cur = self.con.cursor()
        self.results = self.cur.execute('SELECT * FROM Coffee').fetchall()
        self.titles = [description[0].capitalize() for description in self.cur.description]
        self.set_results()

    def set_results(self):
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(len(self.titles))
        for i in range(len(self.titles)):
            self.table.setHorizontalHeaderItem(i, QTableWidgetItem(self.titles[i]))
        for i, row in enumerate(self.results):
            self.table.setRowCount(self.table.rowCount() + 1)
            row = list(row)
            for j, item in enumerate(row):
                item = QTableWidgetItem(str(item))
                self.table.setItem(i, j, item)
        self.table.resizeColumnsToContents()

    def closeEvent(self, event):
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
