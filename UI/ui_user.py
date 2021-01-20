# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_user.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(201, 235)
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
        self.widget_2 = QtWidgets.QWidget(Dialog)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_username = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_username.setObjectName("lineEdit_username")
        self.horizontalLayout_2.addWidget(self.lineEdit_username)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(Dialog)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_password = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.horizontalLayout_3.addWidget(self.lineEdit_password)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(Dialog)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setMinimumSize(QtCore.QSize(36, 0))
        self.label_4.setMaximumSize(QtCore.QSize(36, 16777215))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(self.widget_4)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addWidget(self.widget_4)
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
        Dialog.setWindowTitle(_translate("Dialog", "用户"))
        self.label.setText(_translate("Dialog", "名字："))
        self.label_2.setText(_translate("Dialog", "账号："))
        self.label_3.setText(_translate("Dialog", "密码："))
        self.label_4.setText(_translate("Dialog", "角色："))
        self.pushButton_save.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
