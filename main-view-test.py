# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTranslator
from functions_1 import Functions


class showFunc(Functions):
    def __init__(self):
        Functions.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('坐标G代码添加工具')
        self.setWindowIcon(QIcon('./res/img/zuobiao96px.png'))
        self.setFixedSize(self.width(), self.height())
        self.setAcceptDrops(True)
        self.G55_CBtn.clicked.connect(self.SelectFile_G55)
        self.G56_CBtn.clicked.connect(self.SelectFile_G56)
        self.G57_CBtn.clicked.connect(self.SelectFile_G57)
        self.G58_CBtn.clicked.connect(self.SelectFile_G58)
        self.G59_CBtn.clicked.connect(self.SelectFile_G59)
        self.G55_Btn.clicked.connect(self.ChangeFunc)


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
