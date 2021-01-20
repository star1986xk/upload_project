# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_role.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(194, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_name = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.horizontalLayout.addWidget(self.lineEdit_name)
        self.verticalLayout.addWidget(self.widget)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.widget_5 = QtWidgets.QWidget(Dialog)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_save = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_save.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_save.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_5.addWidget(self.pushButton_save)
        self.pushButton_cancel = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_cancel.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_cancel.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout_5.addWidget(self.pushButton_cancel)
        self.verticalLayout.addWidget(self.widget_5)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "角色"))
        self.label.setText(_translate("Dialog", "角色："))
        self.pushButton_save.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
