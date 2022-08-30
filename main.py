import sys
import sqlite3
import csv

# подключение дизайна
from laborexchange import Ui_MainWindow
from show_prof import ShowProf
from add_prof import AddProf
from delete_prof import DeleteProf

from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from PyQt5.QtGui import QPixmap


class NoResult(Exception):
    pass


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """Подключение базы данных, дизайна и диалоговых окон.
        Обновление комбобокса. Обновление редактора."""

        super().__init__()
        self.setupUi(self)

        pixmap = QPixmap('биржа.jpg')
        self.label_pixmap.setPixmap(pixmap)

        self.titles = ["id", "Profession", "Salary", "Experience", "Date"]

        self.chb_screen.nextCheckState()

        self.btn_addprof.clicked.connect(self.addprof)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.btn_form.clicked.connect(self.run)
        self.btn_add.clicked.connect(self.add_vacantprof)
        self.btn_deleteprof.clicked.connect(self.deleteprof)
        self.btn_add_edit.clicked.connect(self.add_edit)
        self.btn_delete_edit.clicked.connect(self.delete_edit)

        self.showprof = ShowProf()
        self.addprof = AddProf()
        self.deleteprof = DeleteProf()

        self.con = sqlite3.connect("labor exchange.db")
        self.cur = self.con.cursor()

        self.update_cb()

        self.tableWidget.itemChanged.connect(self.item_changed)

    def update_cb(self):
        result = self.cur.execute(f"""SELECT Profession FROM Professions
                                      order by Profession""").fetchall()
        for i in result:
            self.combobox_prof.addItem(i[0])
            self.combobox_prof_add.addItem(i[0])
            self.deleteprof.comboBox.addItem(i[0])

        self.fill_tableWidget()

    def fill_tableWidget(self):
        self.tableWidget.blockSignals(True)

        result = self.cur.execute("""SELECT * FROM VacantProfessions""").fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(5)

        self.tableWidget.setHorizontalHeaderLabels([i[1] for i in self.cur.execute(
            """PRAGMA table_info('VacantProfessions');""").fetchall()])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                val = 0 if val is None else val
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        header = self.tableWidget.horizontalHeader()
        header.ResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        self.tableWidget.blockSignals(False)

    def item_changed(self, item):
        """Редактор базы данных."""

        self.cur.execute(f"""UPDATE VacantProfessions
                             SET {self.titles[item.column()]} = '{item.text()}'
                             WHERE id = 
                             {self.tableWidget.item(self.tableWidget.selectedItems()[0].row(), 0).text()}""")

        self.con.commit()

        self.fill_tableWidget()

    def run(self):
        """Поиск в базе данных. И проверка чекбоксов в Настройках."""

        try:
            self.exp = 0 if self.le_exp.text() == "" else self.le_exp.text()

            self.salary = 10000 if self.le_wsalary.text() == "" else self.le_wsalary.text()

            self.year = 1 if self.calendarWidget.selectedDate().year() == "" \
                else self.calendarWidget.selectedDate().year()

            self.month = "01" if self.calendarWidget.selectedDate().month() == "" \
                else self.calendarWidget.selectedDate().month()

            self.day = "01" if self.calendarWidget.selectedDate().day() == "" \
                else self.calendarWidget.selectedDate().day()

            self.result = self.cur.execute(f"""
                                        SELECT * FROM VacantProfessions
                                        WHERE (Salary >= {self.salary}) AND
                                        (Profession = '{self.combobox_prof.currentText()}')
                                        AND (Date >= '{self.day}.{self.month}.{self.year}') AND
                                        (Experience <= {self.exp})""").fetchall()

            if not self.result:
                raise NoResult("Нет в наличии")

            if self.chb_screen.checkState():
                self.run_show_screen()

            if self.chb_console.checkState():
                self.run_console()

            if self.chb_csv.checkState():
                self.run_csv()

        except sqlite3.OperationalError:
            # QMessageBox.critical(self, "Ошибка ", "Неверно введены данные", QMessageBox.Ok)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Неправильно введены данные")
            msg.setWindowTitle("Error")
            msg.exec_()

        except NoResult as e:
            # QMessageBox.critical(self, "Ошибка ", e, QMessageBox.Ok)

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Нет результата")
            msg.setWindowTitle("Error")
            msg.exec_()

    def run_show_screen(self):
        """Создаем rows and columns, даём названия columns из базы данных,
        Заполняем таблицу элементами из базы данных и выводим её."""

        ex = self.showprof

        ex.tableWidget.setRowCount(len(self.result))
        ex.tableWidget.setColumnCount(len(self.result[0]))

        ex.tableWidget.setHorizontalHeaderLabels([i[1] for i in self.cur.execute(
            """PRAGMA table_info('VacantProfessions');""").fetchall()])

        for i, elem in enumerate(self.result):
            for j, val in enumerate(elem):
                val = 0 if val is None else val
                ex.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

        header = ex.tableWidget.horizontalHeader()
        header.ResizeMode(QHeaderView.ResizeToContents)
        header.setStretchLastSection(True)

        ex.show()

    def run_console(self):
        """Вывод в консоль."""

        columns = [i[1] for i in self.cur.execute(
            """PRAGMA table_info('VacantProfessions');""").fetchall()]

        print("", *columns, sep="\t")

        for i, elem in enumerate(self.result):
            print(i, *elem, sep="\t")

    def run_csv(self):
        """Запись в csv-file."""
        csv_name = "results.csv" if self.le_csv.text() == "" else self.le_csv.text()

        with open(csv_name, mode="w", newline="", encoding="utf8") as csvfile:
            writer = csv.writer(
                csvfile, delimiter=';', quotechar='"',
                quoting=csv.QUOTE_MINIMAL)

            writer.writerow([i[1] for i in self.cur.execute(
                """PRAGMA table_info('VacantProfessions');""").fetchall()])

            for i, elem in enumerate(self.result):
                # elem = list(elem[:-1]) + ["/".join(elem[-1].split("."))]
                writer.writerow(elem)

    def add_edit(self):
        """Добавление в редакторе."""
        self.cur.execute(f"""INSERT INTO VacantProfessions(Date) VALUES('1.1.2000')""")

        self.con.commit()
        self.fill_tableWidget()

    def delete_edit(self):
        """Удаление в редакторе."""
        try:
            self.cur.execute(
                f"""DELETE from VacantProfessions where id =
                {self.tableWidget.item(self.tableWidget.selectedItems()[0].row(), 0).text()}""")

            self.con.commit()
            self.fill_tableWidget()

        except sqlite3.OperationalError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Неправильно введены данные")
            msg.setWindowTitle("Error")
            msg.exec_()

    def addprof(self):
        """Вывод окна, ввод данных для добавления в базу данных и
           принятия решения."""
        ex = self.addprof
        ex.show()

        ex.buttonBox.accepted.connect(self.accept_addprof)
        ex.buttonBox.rejected.connect(self.reject_addprof)

    def accept_addprof(self):
        """При соглашении buttonbox выполняется данная программа."""
        try:
            ex = self.addprof

            edu = ex.le_edu.text()
            prof = ex.le_prof.text()

            self.cur.execute(f"""INSERT INTO Professions(Profession, Education)
                                 VALUES('{prof}', '{edu}')""")
            self.con.commit()

            self.update_cb()

            self.reject_addprof()

        except sqlite3.OperationalError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Неправильно введены данные")
            msg.setWindowTitle("Error")
            msg.exec_()

        except sqlite3.IntegrityError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Профессия имеется в базе данных")
            msg.setWindowTitle("Error")
            msg.exec_()

    def reject_addprof(self):
        """При отказе окно закрывается."""
        self.addprof.close()

    def deleteprof(self):
        """Вывод окна, ввод данных для удаления из базы данных и
           принятия решения."""
        ex = self.deleteprof
        ex.show()

        ex.buttonBox.accepted.connect(self.accept_deleteprof)
        ex.buttonBox.rejected.connect(self.reject_deleteprof)

    def accept_deleteprof(self):
        """При соглашении buttonbox выполняется данная программа."""
        try:
            ex = self.deleteprof

            prof = ex.comboBox.currentText()

            self.cur.execute(f"""DELETE from Professions
                                where Profession = '{prof}'""")

            self.cur.execute(f"""DELETE from VacantProfessions
                                            where Profession = '{prof}'""")

            self.con.commit()

            self.update_cb()

            self.reject_deleteprof()

        except sqlite3.OperationalError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Неправильно введены данные")
            msg.setWindowTitle("Error")
            msg.exec_()

    def reject_deleteprof(self):
        """При отказе окно закрывается."""
        self.deleteprof.close()

    def add_vacantprof(self):
        """Добавление вакатной профессии в базу данных"""
        try:
            exp = self.le_exp_addprof.text()
            salary = self.le_wsalary_addprof.text()
            prof = self.combobox_prof_add.currentText()

            year = self.calendarWidget_addprof.selectedDate().year()
            month = self.calendarWidget_addprof.selectedDate().month()
            day = self.calendarWidget_addprof.selectedDate().day()

            self.cur.execute(f"""INSERT INTO VacantProfessions(Profession, Salary, Experience, Date)
                                 VALUES('{prof}', '{salary}', '{exp}',
                                 '{day}.{month}.{year}')""")
            self.con.commit()

            self.fill_tableWidget()

        except sqlite3.OperationalError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Ошибка!")
            msg.setInformativeText("Неправильно введены данные")
            msg.setWindowTitle("Error")
            msg.exec_()

    def closeEvent(self, event):
        """Отключение от базы данных."""
        self.con.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
