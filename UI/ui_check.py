# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_check.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 117)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/check.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(100, 0))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_2.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_3.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.pushButton_run = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_run.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_run.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_run.setObjectName("pushButton_run")
        self.horizontalLayout_2.addWidget(self.pushButton_run)
        self.pushButton_stop = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton_stop.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_2.addWidget(self.pushButton_stop)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "定时检测"))
        self.label.setText(_translate("Form", "定时检测"))
        self.label_2.setText(_translate("Form", "天"))
        self.label_3.setText(_translate("Form", "时"))
        self.label_4.setText(_translate("Form", "分"))
        self.label_5.setText(_translate("Form", "0"))
        self.pushButton_run.setText(_translate("Form", "检测"))
        self.pushButton_stop.setText(_translate("Form", "停止"))
import image_rc
