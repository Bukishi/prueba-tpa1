# Form implementation generated from reading ui file 'Ejercicio2.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 501)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalFrame = QtWidgets.QFrame(parent=self.centralwidget)
        self.horizontalFrame.setObjectName("horizontalFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.horizontalFrame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(parent=self.horizontalFrame)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1, QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.formStackedWidget = QtWidgets.QStackedWidget(parent=self.horizontalFrame)
        self.formStackedWidget.setObjectName("formStackedWidget")
        self.formStackedWidgetPage1 = QtWidgets.QWidget()
        self.formStackedWidgetPage1.setObjectName("formStackedWidgetPage1")
        self.formLayout = QtWidgets.QFormLayout(self.formStackedWidgetPage1)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_4)
        self.lineEdit = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit)
        self.label_5 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_7)
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(parent=self.formStackedWidgetPage1)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=self.formStackedWidgetPage1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.lineEdit_6)
        self.formStackedWidget.addWidget(self.formStackedWidgetPage1)
        self.gridLayout.addWidget(self.formStackedWidget, 0, 1, 2, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.horizontalFrame)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Nombre Usuario"))
        self.label_2.setText(_translate("MainWindow", "Texto descripcion usuario"))
        self.lineEdit_2.setText(_translate("MainWindow", "valor 1"))
        self.label_3.setText(_translate("MainWindow", "Atributo 1"))
        self.label_4.setText(_translate("MainWindow", "Atributo 2"))
        self.lineEdit.setText(_translate("MainWindow", "valor 2"))
        self.label_5.setText(_translate("MainWindow", "Atributo 3"))
        self.label_6.setText(_translate("MainWindow", "Atributo 5"))
        self.label_7.setText(_translate("MainWindow", "Atributo 4"))
        self.lineEdit_3.setText(_translate("MainWindow", "valor 3"))
        self.lineEdit_4.setText(_translate("MainWindow", "valor 4"))
        self.lineEdit_5.setText(_translate("MainWindow", "valor 5"))
        self.label_8.setText(_translate("MainWindow", "Atributo 6"))
        self.lineEdit_6.setText(_translate("MainWindow", "valor 6"))
        self.pushButton.setText(_translate("MainWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
