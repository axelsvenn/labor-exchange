# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'laborexchange.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(981, 548)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.combobox_prof = QtWidgets.QComboBox(self.tab)
        self.combobox_prof.setObjectName("combobox_prof")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combobox_prof)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_wsalary = QtWidgets.QLineEdit(placeholderText="10000")
        self.le_wsalary.setObjectName("le_wsalary")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_wsalary)
        self.le_exp = QtWidgets.QLineEdit(placeholderText="0")
        self.le_exp.setObjectName("le_exp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_exp)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.tab)
        self.calendarWidget.setObjectName("calendarWidget")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.calendarWidget)
        self.label_exp = QtWidgets.QLabel(self.tab)
        self.label_exp.setObjectName("label_exp")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_exp)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_form = QtWidgets.QPushButton(self.tab)
        self.btn_form.setObjectName("btn_form")
        self.horizontalLayout.addWidget(self.btn_form)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_4)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.combobox_prof_add = QtWidgets.QComboBox(self.tab_4)
        self.combobox_prof_add.setObjectName("combobox_prof_add")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combobox_prof_add)
        self.label_12 = QtWidgets.QLabel(self.tab_4)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.le_wsalary_addprof = QtWidgets.QLineEdit(self.tab_4)
        self.le_wsalary_addprof.setObjectName("le_wsalary_addprof")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_wsalary_addprof)
        self.le_exp_addprof = QtWidgets.QLineEdit(self.tab_4)
        self.le_exp_addprof.setObjectName("le_exp_addprof")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_exp_addprof)
        self.label_13 = QtWidgets.QLabel(self.tab_4)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.calendarWidget_addprof = QtWidgets.QCalendarWidget(self.tab_4)
        self.calendarWidget_addprof.setObjectName("calendarWidget_addprof")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.calendarWidget_addprof)
        self.label_exp_3 = QtWidgets.QLabel(self.tab_4)
        self.label_exp_3.setObjectName("label_exp_3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_exp_3)
        self.verticalLayout_13.addLayout(self.formLayout_3)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.btn_add = QtWidgets.QPushButton(self.tab_4)
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout_9.addWidget(self.btn_add)
        self.verticalLayout_13.addLayout(self.horizontalLayout_9)
        self.verticalLayout_15.addLayout(self.verticalLayout_13)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.btn_addprof = QtWidgets.QPushButton(self.tab_4)
        self.btn_addprof.setObjectName("btn_addprof")
        self.horizontalLayout_10.addWidget(self.btn_addprof)
        self.btn_deleteprof = QtWidgets.QPushButton(self.tab_4)
        self.btn_deleteprof.setObjectName("btn_deleteprof")
        self.horizontalLayout_10.addWidget(self.btn_deleteprof)
        self.formLayout_4.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.label_14 = QtWidgets.QLabel(self.tab_4)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_14)
        self.verticalLayout_15.addLayout(self.formLayout_4)
        self.verticalLayout_16.addLayout(self.verticalLayout_15)
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout_5.addWidget(self.tableWidget)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_add_edit = QtWidgets.QPushButton(self.tab_3)
        self.btn_add_edit.setObjectName("btn_add_edit")
        self.verticalLayout_4.addWidget(self.btn_add_edit)
        self.btn_delete_edit = QtWidgets.QPushButton(self.tab_3)
        self.btn_delete_edit.setObjectName("btn_delete_edit")
        self.verticalLayout_4.addWidget(self.btn_delete_edit)
        self.horizontalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.le_csv = QtWidgets.QLineEdit(self.tab_2)
        self.le_csv.setObjectName("le_csv")
        self.gridLayout_3.addWidget(self.le_csv, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.chb_screen = QtWidgets.QCheckBox(self.tab_2)
        self.chb_screen.setObjectName("chb_screen")
        self.gridLayout_3.addWidget(self.chb_screen, 0, 0, 1, 1)
        self.chb_csv = QtWidgets.QCheckBox(self.tab_2)
        self.chb_csv.setObjectName("chb_csv")
        self.gridLayout_3.addWidget(self.chb_csv, 2, 0, 1, 1)
        self.chb_console = QtWidgets.QCheckBox(self.tab_2)
        self.chb_console.setObjectName("chb_console")
        self.gridLayout_3.addWidget(self.chb_console, 1, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_2.addWidget(self.label_15)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_pixmap = QtWidgets.QLabel(self.tab_2)
        self.label_pixmap.setText("")
        self.label_pixmap.setObjectName("label_pixmap")
        self.horizontalLayout_3.addWidget(self.label_pixmap)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 981, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "?????????????????? ?????????? ??????????"))
        self.label_3.setText(_translate("MainWindow", "???????????????? ??????????????????"))
        self.label_2.setText(_translate("MainWindow", "???????????????? ????"))
        self.label.setText(_translate("MainWindow", "???????? (???????????????????????????? ??)"))
        self.label_exp.setText(_translate("MainWindow", "?????????????????????????? ???? ???????????? ????"))
        self.btn_form.setText(_translate("MainWindow", "????????????????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "??????????"))
        self.label_11.setText(_translate("MainWindow", "???????????????????????? ??????????????????"))
        self.label_12.setText(_translate("MainWindow", "???????????????????????? ????????????????"))
        self.label_13.setText(_translate("MainWindow", "???????? ????????????????????"))
        self.label_exp_3.setText(_translate("MainWindow", "?????????????????????? ????????"))
        self.btn_add.setText(_translate("MainWindow", "????????????????"))
        self.btn_addprof.setText(_translate("MainWindow", "???????????????? ??????????????????"))
        self.btn_deleteprof.setText(_translate("MainWindow", "?????????????? ??????????????????"))
        self.label_14.setText(_translate("MainWindow", "???????????? ?? ??????????????????????:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "????????????????????"))
        self.btn_add_edit.setText(_translate("MainWindow", "????????????????"))
        self.btn_delete_edit.setText(_translate("MainWindow", "??????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "????????????????"))
        self.chb_screen.setText(_translate("MainWindow", "???????????????? ???? ??????????"))
        self.chb_csv.setText(_translate("MainWindow", "???????????? ?? file"))
        self.chb_console.setText(_translate("MainWindow", "?????????? ?? ??????????????"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "??????????????????"))
