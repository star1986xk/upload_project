# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_settings.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(824, 452)
        Dialog.setStyleSheet("QDialog{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolBox::tab{background-color: rgb(90, 200, 255);color:white;border-radius:5px}\n"
"QToolBox QWidget{background-color: rgb(255, 255, 255);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(Dialog)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 789, 330))
        self.page.setObjectName("page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.page)
        self.widget.setMinimumSize(QtCore.QSize(0, 50))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_title = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout.addWidget(self.lineEdit_title)
        self.verticalLayout_2.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.page)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignTop)
        self.textEdit_describe1 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_describe1.setObjectName("textEdit_describe1")
        self.horizontalLayout_2.addWidget(self.textEdit_describe1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_11 = QtWidgets.QWidget(self.page)
        self.widget_11.setMinimumSize(QtCore.QSize(0, 100))
        self.widget_11.setObjectName("widget_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_11)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_9 = QtWidgets.QWidget(self.widget_11)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.widget_9)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.textEdit_tips1 = QtWidgets.QTextEdit(self.widget_9)
        self.textEdit_tips1.setObjectName("textEdit_tips1")
        self.horizontalLayout_9.addWidget(self.textEdit_tips1)
        self.horizontalLayout_12.addWidget(self.widget_9)
        self.widget_10 = QtWidgets.QWidget(self.widget_11)
        self.widget_10.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_6 = QtWidgets.QLabel(self.widget_10)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6, 0, QtCore.Qt.AlignTop)
        self.textEdit_tips2 = QtWidgets.QTextEdit(self.widget_10)
        self.textEdit_tips2.setObjectName("textEdit_tips2")
        self.horizontalLayout_10.addWidget(self.textEdit_tips2)
        self.horizontalLayout_12.addWidget(self.widget_10)
        self.verticalLayout_2.addWidget(self.widget_11)
        self.widget_3 = QtWidgets.QWidget(self.page)
        self.widget_3.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_info = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_info.setMinimumSize(QtCore.QSize(70, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/保存.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_info.setIcon(icon)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_3.addWidget(self.pushButton_info)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 806, 278))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_4 = QtWidgets.QWidget(self.page_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton_ftp_add = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_ftp_add.setMinimumSize(QtCore.QSize(70, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ftp_add.setIcon(icon1)
        self.pushButton_ftp_add.setObjectName("pushButton_ftp_add")
        self.horizontalLayout_4.addWidget(self.pushButton_ftp_add)
        self.pushButton_ftp_update = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_ftp_update.setMinimumSize(QtCore.QSize(70, 0))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/修改.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ftp_update.setIcon(icon2)
        self.pushButton_ftp_update.setObjectName("pushButton_ftp_update")
        self.horizontalLayout_4.addWidget(self.pushButton_ftp_update)
        self.pushButton_ftp_detele = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_ftp_detele.setMinimumSize(QtCore.QSize(70, 0))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/删 除 .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_ftp_detele.setIcon(icon3)
        self.pushButton_ftp_detele.setObjectName("pushButton_ftp_detele")
        self.horizontalLayout_4.addWidget(self.pushButton_ftp_detele)
        self.verticalLayout_3.addWidget(self.widget_4)
        self.tableWidget_ftp = QtWidgets.QTableWidget(self.page_2)
        self.tableWidget_ftp.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_ftp.setObjectName("tableWidget_ftp")
        self.tableWidget_ftp.setColumnCount(8)
        self.tableWidget_ftp.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_ftp.setHorizontalHeaderItem(7, item)
        self.tableWidget_ftp.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget_ftp)
        self.toolBox.addItem(self.page_2, "")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 806, 278))
        self.page_3.setObjectName("page_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_5 = QtWidgets.QWidget(self.page_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.pushButton_role_add = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_role_add.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_role_add.setIcon(icon1)
        self.pushButton_role_add.setObjectName("pushButton_role_add")
        self.horizontalLayout_5.addWidget(self.pushButton_role_add)
        self.pushButton_role_update = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_role_update.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_role_update.setIcon(icon2)
        self.pushButton_role_update.setObjectName("pushButton_role_update")
        self.horizontalLayout_5.addWidget(self.pushButton_role_update)
        self.pushButton_role_delete = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_role_delete.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_role_delete.setIcon(icon3)
        self.pushButton_role_delete.setObjectName("pushButton_role_delete")
        self.horizontalLayout_5.addWidget(self.pushButton_role_delete)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.tableWidget_role = QtWidgets.QTableWidget(self.page_3)
        self.tableWidget_role.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_role.setObjectName("tableWidget_role")
        self.tableWidget_role.setColumnCount(4)
        self.tableWidget_role.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_role.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_role.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_role.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_role.setHorizontalHeaderItem(3, item)
        self.tableWidget_role.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_4.addWidget(self.tableWidget_role)
        self.toolBox.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 806, 278))
        self.page_4.setObjectName("page_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_6 = QtWidgets.QWidget(self.page_4)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem3)
        self.pushButton_user_add = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_user_add.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_user_add.setIcon(icon1)
        self.pushButton_user_add.setObjectName("pushButton_user_add")
        self.horizontalLayout_6.addWidget(self.pushButton_user_add)
        self.pushButton_user_update = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_user_update.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_user_update.setIcon(icon2)
        self.pushButton_user_update.setObjectName("pushButton_user_update")
        self.horizontalLayout_6.addWidget(self.pushButton_user_update)
        self.pushButton_user_delete = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_user_delete.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_user_delete.setIcon(icon3)
        self.pushButton_user_delete.setObjectName("pushButton_user_delete")
        self.horizontalLayout_6.addWidget(self.pushButton_user_delete)
        self.verticalLayout_5.addWidget(self.widget_6)
        self.tableWidget_user = QtWidgets.QTableWidget(self.page_4)
        self.tableWidget_user.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_user.setObjectName("tableWidget_user")
        self.tableWidget_user.setColumnCount(6)
        self.tableWidget_user.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_user.setHorizontalHeaderItem(5, item)
        self.tableWidget_user.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_5.addWidget(self.tableWidget_user)
        self.toolBox.addItem(self.page_4, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 806, 278))
        self.page_5.setObjectName("page_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.widget_7 = QtWidgets.QWidget(self.page_5)
        self.widget_7.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_7.setMaximumSize(QtCore.QSize(150, 16777215))
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineEdit_word_search = QtWidgets.QLineEdit(self.widget_7)
        self.lineEdit_word_search.setObjectName("lineEdit_word_search")
        self.verticalLayout_6.addWidget(self.lineEdit_word_search)
        self.pushButton_word_search = QtWidgets.QPushButton(self.widget_7)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/查询.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_word_search.setIcon(icon4)
        self.pushButton_word_search.setObjectName("pushButton_word_search")
        self.verticalLayout_6.addWidget(self.pushButton_word_search)
        self.pushButton_word_add = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_word_add.setIcon(icon1)
        self.pushButton_word_add.setObjectName("pushButton_word_add")
        self.verticalLayout_6.addWidget(self.pushButton_word_add)
        self.pushButton_word_del = QtWidgets.QPushButton(self.widget_7)
        self.pushButton_word_del.setIcon(icon3)
        self.pushButton_word_del.setObjectName("pushButton_word_del")
        self.verticalLayout_6.addWidget(self.pushButton_word_del)
        self.horizontalLayout_7.addWidget(self.widget_7)
        self.tableWidget_word = QtWidgets.QTableWidget(self.page_5)
        self.tableWidget_word.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget_word.setObjectName("tableWidget_word")
        self.tableWidget_word.setColumnCount(4)
        self.tableWidget_word.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_word.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_word.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_word.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_word.setHorizontalHeaderItem(3, item)
        self.tableWidget_word.horizontalHeader().setStretchLastSection(True)
        self.horizontalLayout_7.addWidget(self.tableWidget_word)
        self.toolBox.addItem(self.page_5, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 806, 278))
        self.page_6.setObjectName("page_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page_6)
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_3 = QtWidgets.QLabel(self.page_6)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.lineEdit_API_Key = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_API_Key.setObjectName("lineEdit_API_Key")
        self.verticalLayout_7.addWidget(self.lineEdit_API_Key)
        self.label_4 = QtWidgets.QLabel(self.page_6)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.lineEdit_Secret_Key = QtWidgets.QLineEdit(self.page_6)
        self.lineEdit_Secret_Key.setObjectName("lineEdit_Secret_Key")
        self.verticalLayout_7.addWidget(self.lineEdit_Secret_Key)
        self.widget_8 = QtWidgets.QWidget(self.page_6)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 50))
        self.widget_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem4)
        self.pushButton_key = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_key.setMinimumSize(QtCore.QSize(70, 0))
        self.pushButton_key.setIcon(icon)
        self.pushButton_key.setObjectName("pushButton_key")
        self.horizontalLayout_8.addWidget(self.pushButton_key)
        self.verticalLayout_7.addWidget(self.widget_8)
        self.toolBox.addItem(self.page_6, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(Dialog)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "设置"))
        self.label.setText(_translate("Dialog", "标题："))
        self.label_2.setText(_translate("Dialog", "备注："))
        self.label_5.setText(_translate("Dialog", "提示1："))
        self.label_6.setText(_translate("Dialog", "提示2："))
        self.pushButton_info.setText(_translate("Dialog", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "设置软件信息"))
        self.pushButton_ftp_add.setText(_translate("Dialog", "添加"))
        self.pushButton_ftp_update.setText(_translate("Dialog", "修改"))
        self.pushButton_ftp_detele.setText(_translate("Dialog", "删除"))
        item = self.tableWidget_ftp.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择"))
        item = self.tableWidget_ftp.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "编号"))
        item = self.tableWidget_ftp.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "服务器名"))
        item = self.tableWidget_ftp.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "地址"))
        item = self.tableWidget_ftp.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "端口"))
        item = self.tableWidget_ftp.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget_ftp.horizontalHeaderItem(6)
        item.setText(_translate("Dialog", "密码"))
        item = self.tableWidget_ftp.horizontalHeaderItem(7)
        item.setText(_translate("Dialog", "目录"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "设置FTP服务器"))
        self.pushButton_role_add.setText(_translate("Dialog", "添加"))
        self.pushButton_role_update.setText(_translate("Dialog", "修改"))
        self.pushButton_role_delete.setText(_translate("Dialog", "删除"))
        item = self.tableWidget_role.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择"))
        item = self.tableWidget_role.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "编号"))
        item = self.tableWidget_role.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "角色"))
        item = self.tableWidget_role.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "FTP服务器"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), _translate("Dialog", "设置角色"))
        self.pushButton_user_add.setText(_translate("Dialog", "添加"))
        self.pushButton_user_update.setText(_translate("Dialog", "修改"))
        self.pushButton_user_delete.setText(_translate("Dialog", "删除"))
        item = self.tableWidget_user.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择"))
        item = self.tableWidget_user.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "编号"))
        item = self.tableWidget_user.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "姓名"))
        item = self.tableWidget_user.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "用户名"))
        item = self.tableWidget_user.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "密码"))
        item = self.tableWidget_user.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "角色"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), _translate("Dialog", "设置用户"))
        self.pushButton_word_search.setText(_translate("Dialog", "查  询"))
        self.pushButton_word_add.setText(_translate("Dialog", "添  加"))
        self.pushButton_word_del.setText(_translate("Dialog", "删  除"))
        item = self.tableWidget_word.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "选择"))
        item = self.tableWidget_word.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "编号"))
        item = self.tableWidget_word.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "关键词"))
        item = self.tableWidget_word.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "用户"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), _translate("Dialog", "设置关键词库"))
        self.label_3.setText(_translate("Dialog", "API_Key"))
        self.label_4.setText(_translate("Dialog", "Secret_Key"))
        self.pushButton_key.setText(_translate("Dialog", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), _translate("Dialog", "设置百度识别key"))
import image_rc