# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from LineEdit import MyLineEdit


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(420, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.Clear = QtWidgets.QPushButton(self.centralwidget)
        self.Clear.setMinimumSize(QtCore.QSize(50, 0))
        self.Clear.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(9)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Clear")
        self.horizontalLayout_3.addWidget(self.Clear)
        self.verticalLayout_6.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.G55_Label = QtWidgets.QLabel(self.centralwidget)
        self.G55_Label.setMinimumSize(QtCore.QSize(35, 25))
        self.G55_Label.setMaximumSize(QtCore.QSize(35, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.G55_Label.setFont(font)
        self.G55_Label.setObjectName("G55_Label")
        self.verticalLayout.addWidget(self.G55_Label)
        self.G56_Label = QtWidgets.QLabel(self.centralwidget)
        self.G56_Label.setMinimumSize(QtCore.QSize(35, 25))
        self.G56_Label.setMaximumSize(QtCore.QSize(35, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.G56_Label.setFont(font)
        self.G56_Label.setObjectName("G56_Label")
        self.verticalLayout.addWidget(self.G56_Label)
        self.G57_Label = QtWidgets.QLabel(self.centralwidget)
        self.G57_Label.setMinimumSize(QtCore.QSize(35, 25))
        self.G57_Label.setMaximumSize(QtCore.QSize(35, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.G57_Label.setFont(font)
        self.G57_Label.setObjectName("G57_Label")
        self.verticalLayout.addWidget(self.G57_Label)
        self.G58_Label = QtWidgets.QLabel(self.centralwidget)
        self.G58_Label.setMinimumSize(QtCore.QSize(35, 25))
        self.G58_Label.setMaximumSize(QtCore.QSize(35, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.G58_Label.setFont(font)
        self.G58_Label.setObjectName("G58_Label")
        self.verticalLayout.addWidget(self.G58_Label)
        self.G59_Label = QtWidgets.QLabel(self.centralwidget)
        self.G59_Label.setMinimumSize(QtCore.QSize(35, 25))
        self.G59_Label.setMaximumSize(QtCore.QSize(35, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.G59_Label.setFont(font)
        self.G59_Label.setObjectName("G59_Label")
        self.verticalLayout.addWidget(self.G59_Label)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.G55_Path = MyLineEdit()
        # self.G55_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.G55_Path.setMinimumSize(QtCore.QSize(250, 25))
        self.G55_Path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.G55_Path.setFont(font)
        self.G55_Path.setObjectName("G55_Path")
        self.verticalLayout_2.addWidget(self.G55_Path)
        self.G56_Path = MyLineEdit()
        # self.G56_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.G56_Path.setMinimumSize(QtCore.QSize(250, 25))
        self.G56_Path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.G56_Path.setFont(font)
        self.G56_Path.setObjectName("G56_Path")
        self.verticalLayout_2.addWidget(self.G56_Path)
        self.G57_Path = MyLineEdit()
        # self.G57_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.G57_Path.setMinimumSize(QtCore.QSize(250, 25))
        self.G57_Path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.G57_Path.setFont(font)
        self.G57_Path.setObjectName("G57_Path")
        self.verticalLayout_2.addWidget(self.G57_Path)
        self.G58_Path = MyLineEdit()
        # self.G58_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.G58_Path.setMinimumSize(QtCore.QSize(250, 25))
        self.G58_Path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.G58_Path.setFont(font)
        self.G58_Path.setObjectName("G58_Path")
        self.verticalLayout_2.addWidget(self.G58_Path)
        self.G59_Path = MyLineEdit()
        # self.G59_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.G59_Path.setMinimumSize(QtCore.QSize(250, 25))
        self.G59_Path.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.G59_Path.setFont(font)
        self.G59_Path.setObjectName("G59_Path")
        self.verticalLayout_2.addWidget(self.G59_Path)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.G55_CBtn = QtWidgets.QPushButton(self.centralwidget)
        self.G55_CBtn.setMinimumSize(QtCore.QSize(50, 25))
        self.G55_CBtn.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.G55_CBtn.setFont(font)
        self.G55_CBtn.setObjectName("G55_CBtn")
        self.verticalLayout_3.addWidget(self.G55_CBtn)
        self.G56_CBtn = QtWidgets.QPushButton(self.centralwidget)
        self.G56_CBtn.setMinimumSize(QtCore.QSize(50, 25))
        self.G56_CBtn.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.G56_CBtn.setFont(font)
        self.G56_CBtn.setObjectName("G56_CBtn")
        self.verticalLayout_3.addWidget(self.G56_CBtn)
        self.G57_CBtn = QtWidgets.QPushButton(self.centralwidget)
        self.G57_CBtn.setMinimumSize(QtCore.QSize(50, 25))
        self.G57_CBtn.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.G57_CBtn.setFont(font)
        self.G57_CBtn.setObjectName("G57_CBtn")
        self.verticalLayout_3.addWidget(self.G57_CBtn)
        self.G58_CBtn = QtWidgets.QPushButton(self.centralwidget)
        self.G58_CBtn.setMinimumSize(QtCore.QSize(50, 25))
        self.G58_CBtn.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.G58_CBtn.setFont(font)
        self.G58_CBtn.setObjectName("G58_CBtn")
        self.verticalLayout_3.addWidget(self.G58_CBtn)
        self.G59_CBtn = QtWidgets.QPushButton(self.centralwidget)
        self.G59_CBtn.setMinimumSize(QtCore.QSize(50, 25))
        self.G59_CBtn.setMaximumSize(QtCore.QSize(50, 25))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.G59_CBtn.setFont(font)
        self.G59_CBtn.setObjectName("G59_CBtn")
        self.verticalLayout_3.addWidget(self.G59_CBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_6.addWidget(self.line)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ico = QtWidgets.QLabel(self.centralwidget)
        self.ico.setMinimumSize(QtCore.QSize(60, 60))
        self.ico.setMaximumSize(QtCore.QSize(60, 60))
        self.ico.setAlignment(QtCore.Qt.AlignCenter)
        self.ico.setObjectName("ico")
        self.horizontalLayout_2.addWidget(self.ico)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.output_1 = QtWidgets.QLabel(self.centralwidget)
        self.output_1.setObjectName("output_1")
        self.verticalLayout_4.addWidget(self.output_1)
        self.output_2 = QtWidgets.QLabel(self.centralwidget)
        self.output_2.setObjectName("output_2")
        self.verticalLayout_4.addWidget(self.output_2)
        self.output_3 = QtWidgets.QLabel(self.centralwidget)
        self.output_3.setObjectName("output_3")
        self.verticalLayout_4.addWidget(self.output_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.output_4 = QtWidgets.QLabel(self.centralwidget)
        self.output_4.setObjectName("output_4")
        self.verticalLayout_5.addWidget(self.output_4)
        self.output_5 = QtWidgets.QLabel(self.centralwidget)
        self.output_5.setObjectName("output_5")
        self.verticalLayout_5.addWidget(self.output_5)
        self.output_6 = QtWidgets.QLabel(self.centralwidget)
        self.output_6.setObjectName("output_6")
        self.verticalLayout_5.addWidget(self.output_6)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.Change_Btn = QtWidgets.QPushButton(self.centralwidget)
        self.Change_Btn.setMinimumSize(QtCore.QSize(100, 60))
        self.Change_Btn.setMaximumSize(QtCore.QSize(150, 60))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.Change_Btn.setFont(font)
        self.Change_Btn.setObjectName("Change_Btn")
        self.horizontalLayout_2.addWidget(self.Change_Btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "NC文件路径："))
        self.Clear.setText(_translate("MainWindow", "清空"))
        self.G55_Label.setText(_translate("MainWindow", "G55:"))
        self.G56_Label.setText(_translate("MainWindow", "G56:"))
        self.G57_Label.setText(_translate("MainWindow", "G57:"))
        self.G58_Label.setText(_translate("MainWindow", "G58:"))
        self.G59_Label.setText(_translate("MainWindow", "G59:"))
        self.G55_CBtn.setText(_translate("MainWindow", "选择"))
        self.G56_CBtn.setText(_translate("MainWindow", "选择"))
        self.G57_CBtn.setText(_translate("MainWindow", "选择"))
        self.G58_CBtn.setText(_translate("MainWindow", "选择"))
        self.G59_CBtn.setText(_translate("MainWindow", "选择"))
        self.ico.setText(_translate("MainWindow", "TextLabel"))
        self.output_3.setText(_translate("MainWindow", ""))
        self.output_1.setText(_translate("MainWindow", ""))
        self.output_2.setText(_translate("MainWindow", ""))
        self.output_5.setText(_translate("MainWindow", ""))
        self.output_4.setText(_translate("MainWindow", ""))
        self.output_6.setText(_translate("MainWindow", ""))
        self.Change_Btn.setText(_translate("MainWindow", "一键添加"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
