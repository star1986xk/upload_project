# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(790, 504)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/upload.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#Form{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QDialog{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#textEdit_describe,#textEdit_tips{\n"
"    border-style:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#lineEdit_uid{\n"
"    border-style:none;\n"
"}\n"
"QLineEdit{\n"
"    border: 1px solid #55aaff;\n"
"    border-radius:5px;\n"
"}\n"
"QLineEdit:focus{border: 1px solid #78ffeb;}\n"
"\n"
"QTextEdit{\n"
"    border: 1px solid #55aaff;\n"
"    border-radius:5px;\n"
"    padding:1px 1px;\n"
"}\n"
"QTextEdit:focus{border: 1px solid #78ffeb;}\n"
"\n"
"QPushButton{\n"
"border-style:none;\n"
"background-color:white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:hover{color:lightskyblue}\n"
"QPushButton:pressed {\n"
"    /* 改变背景色 */\n"
"    /* background-color:rgb(180, 180, 180,120); */\n"
"    /* 改变边框风格 */\n"
"    /* border-style:inset; */\n"
"    /* 使文字有一点移动 */\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"}\n"
"\n"
"QCheckBox::indicator{width: 30px;height: 30px;}\n"
"QCheckBox::indicator:unchecked{image: url(:/newPrefix/多选.png);}\n"
"QCheckBox::indicator:checked{image: url(:/newPrefix/多选1.png);}\n"
"QCheckBox:hover{color:lightskyblue}\n"
"QCheckBox:pressed{\n"
"    padding-left:2px;\n"
"    padding-top:2px;\n"
"}")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_file = QtWidgets.QPushButton(self.widget_5)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/打开文件.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_file.setIcon(icon1)
        self.pushButton_file.setObjectName("pushButton_file")
        self.horizontalLayout_10.addWidget(self.pushButton_file)
        self.lineEdit_filename = QtWidgets.QLineEdit(self.widget_5)
        self.lineEdit_filename.setReadOnly(True)
        self.lineEdit_filename.setObjectName("lineEdit_filename")
        self.horizontalLayout_10.addWidget(self.lineEdit_filename)
        self.verticalLayout.addWidget(self.widget_5)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_7 = QtWidgets.QLabel(self.widget_6)
        self.label_7.setMinimumSize(QtCore.QSize(70, 0))
        self.label_7.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_11.addWidget(self.label_7)
        self.comboBox_project = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_project.setObjectName("comboBox_project")
        self.horizontalLayout_11.addWidget(self.comboBox_project)
        self.verticalLayout.addWidget(self.widget_6)
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_6 = QtWidgets.QLabel(self.widget_4)
        self.label_6.setMinimumSize(QtCore.QSize(70, 0))
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.comboBox_ftp = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_ftp.setObjectName("comboBox_ftp")
        self.horizontalLayout_9.addWidget(self.comboBox_ftp)
        self.verticalLayout.addWidget(self.widget_4)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.progressBar = QtWidgets.QProgressBar(self.widget_8)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_12.addWidget(self.progressBar)
        self.verticalLayout.addWidget(self.widget_8)
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_up = QtWidgets.QLabel(self.widget_9)
        self.label_up.setObjectName("label_up")
        self.horizontalLayout_13.addWidget(self.label_up)
        self.lineEdit_uid = QtWidgets.QLineEdit(self.widget_9)
        self.lineEdit_uid.setText("")
        self.lineEdit_uid.setReadOnly(True)
        self.lineEdit_uid.setObjectName("lineEdit_uid")
        self.horizontalLayout_13.addWidget(self.lineEdit_uid)
        self.verticalLayout.addWidget(self.widget_9)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.pushButton_upload = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(60, 0))
        self.pushButton_upload.setIcon(icon)
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout_8.addWidget(self.pushButton_upload)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.pushButton_settings = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_settings.setMinimumSize(QtCore.QSize(60, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_settings.setIcon(icon2)
        self.pushButton_settings.setObjectName("pushButton_settings")
        self.horizontalLayout_8.addWidget(self.pushButton_settings)
        self.pushButton_logout = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_logout.setMinimumSize(QtCore.QSize(60, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/登出.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_logout.setIcon(icon3)
        self.pushButton_logout.setObjectName("pushButton_logout")
        self.horizontalLayout_8.addWidget(self.pushButton_logout)
        self.verticalLayout.addWidget(self.widget_7)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.textEdit_describe = QtWidgets.QTextEdit(self.widget_3)
        self.textEdit_describe.setTabChangesFocus(False)
        self.textEdit_describe.setReadOnly(True)
        self.textEdit_describe.setObjectName("textEdit_describe")
        self.verticalLayout_3.addWidget(self.textEdit_describe)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_10 = QtWidgets.QWidget(self.widget_2)
        self.widget_10.setObjectName("widget_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_10)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.widget_10)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.textEdit_tips = QtWidgets.QTextEdit(self.widget_10)
        self.textEdit_tips.setTabChangesFocus(False)
        self.textEdit_tips.setReadOnly(True)
        self.textEdit_tips.setObjectName("textEdit_tips")
        self.verticalLayout_4.addWidget(self.textEdit_tips)
        self.verticalLayout_5.addWidget(self.widget_10)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_file.setText(_translate("Form", "选择文件"))
        self.label_7.setText(_translate("Form", "选择项目"))
        self.label_6.setText(_translate("Form", "选择位置"))
        self.label_up.setText(_translate("Form", "上传成功："))
        self.pushButton_upload.setText(_translate("Form", "上传"))
        self.pushButton_settings.setText(_translate("Form", "设置"))
        self.pushButton_logout.setText(_translate("Form", "登出"))
        self.label_5.setText(_translate("Form", "说明："))
        self.label_9.setText(_translate("Form", "提示："))
import image_rc
