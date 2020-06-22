# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTranslator, QTimer
from functions import Functions


class showFunc(Functions):
    def __init__(self):
        Functions.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('坐标G代码添加工具')
        self.setWindowIcon(QIcon('./res/img/zuobiao96px.png'))
        self.pix = QPixmap('./res/img/zuobiaoxi.png')
        self.ico.setPixmap(self.pix)
        self.setFixedSize(self.width(), self.height())
        self.G55_CBtn.clicked.connect(self.SelectFile_G55)
        self.G56_CBtn.clicked.connect(self.SelectFile_G56)
        self.G57_CBtn.clicked.connect(self.SelectFile_G57)
        self.G58_CBtn.clicked.connect(self.SelectFile_G58)
        self.G59_CBtn.clicked.connect(self.SelectFile_G59)
        self.Clear.clicked.connect(self.Clear_Path)
        self.time = QTimer(self)
        self.time.setInterval(9000)
        self.Change_Btn.clicked.connect(self.btn_Func)
        self.time.timeout.connect(self.refresh)

    def btn_Func(self):
        self.btnChangeFunc()
        self.time.start()

    def refresh(self):
        self.time.stop()
        self.output_1.setText('')
        self.output_2.setText('')
        self.output_3.setText('')
        self.output_4.setText('')
        self.output_5.setText('')


def translate():
    translateLoad = QTranslator()
    translateLoad.load('./res/qt_zh_CN.qm')
    return translateLoad


if __name__ == '__main__':
    app = QApplication([])
    translateInstall = translate()
    app.installTranslator(translateInstall)
    win = showFunc()
    win.show()
    sys.exit(app.exec_())
