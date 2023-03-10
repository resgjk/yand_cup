from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(575, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(90, 20, 451, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.name = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.name.setObjectName("name")
        self.verticalLayout.addWidget(self.name)
        self.st = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.st.setObjectName("st")
        self.verticalLayout.addWidget(self.st)
        self.vid = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.vid.setObjectName("vid")
        self.verticalLayout.addWidget(self.vid)
        self.vkus = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.vkus.setObjectName("vkus")
        self.verticalLayout.addWidget(self.vkus)
        self.price = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.price.setObjectName("price")
        self.verticalLayout.addWidget(self.price)
        self.ob = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.ob.setObjectName("ob")
        self.verticalLayout.addWidget(self.ob)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 51, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 21, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 210, 31, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 260, 31, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 320, 41, 16))
        self.label_6.setObjectName("label_6")
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(210, 410, 141, 41))
        self.save.setObjectName("save")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "????????????????"))
        self.label_2.setText(_translate("MainWindow", "??????????????"))
        self.label_3.setText(_translate("MainWindow", "??????"))
        self.label_4.setText(_translate("MainWindow", "????????"))
        self.label_5.setText(_translate("MainWindow", "????????"))
        self.label_6.setText(_translate("MainWindow", "??????????"))
        self.save.setText(_translate("MainWindow", "??????????????????"))
