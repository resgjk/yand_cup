import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.add.clicked.connect(self.add_fnc)
        self.change.clicked.connect(self.change_fnc)
        self.update_table()

    def update_table(self):
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        self.result = self.cur.execute("SELECT * FROM Coffee").fetchall()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))

        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def add_fnc(self):
        self.add_form = Add_Form()
        self.add_form.show()

    def change_fnc(self):
        self.change_form = Change_Form()
        self.change_form.show()


class Add_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("edit.ui", self)
        self.save.clicked.connect(self.save_fnc)

    def save_fnc(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"INSERT INTO Coffee(Название, Степень, Вид, Вкус, Цена, Объем)"
                    f"VALUES('{self.name.text()}', '{self.st.text()}', "
                    f"'{self.vid.text()}', '{self.vkus.text()}', ''{self.price.text()}'', '{self.ob.text()}')")
        con.commit()
        con.close()
        ex.add_form.close()
        ex.update_table()


class Change_Form(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("edit.ui", self)
        self.save.clicked.connect(self.save_fnc)
        self.name.setText(ex.result[ex.tableWidget.currentRow()][1])
        self.st.setText(ex.result[ex.tableWidget.currentRow()][2])
        self.vid.setText(ex.result[ex.tableWidget.currentRow()][3])
        self.vkus.setText(ex.result[ex.tableWidget.currentRow()][4])
        self.price.setText(str(ex.result[ex.tableWidget.currentRow()][5]))
        self.ob.setText(str(ex.result[ex.tableWidget.currentRow()][6]))

    def save_fnc(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        cur.execute(f"UPDATE Coffee SET Название = '{self.name.text()}',"
                    f"Объем = '{self.ob.text()}',"
                    f"Степень = '{self.st.text()}',"
                    f"Вид = '{self.vid.text()}',"
                    f"Вкус = '{self.vkus.text()}',"
                    f"Цена = '{self.price.text()}' WHERE id = {ex.result[ex.tableWidget.currentRow()][0]}")
        con.commit()
        con.close()
        ex.change_form.close()
        ex.update_table()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec_())
