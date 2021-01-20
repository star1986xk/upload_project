# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_keyword.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(195, 309)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
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
        Dialog.setWindowTitle(_translate("Dialog", "关键词库"))
        self.pushButton_save.setText(_translate("Dialog", "确定"))
        self.pushButton_cancel.setText(_translate("Dialog", "取消"))
