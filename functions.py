# -*- coding: utf-8 -*-
import os
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from view import Ui_MainWindow


class Functions(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

    def SelectFile_G55(self):
        File = QFileDialog()
        FilePath, ok = File.getOpenFileName(self, '选择NC文件', 'D:/模型/')
        if ok:
            self.G55_Path.setText(FilePath)

    def SelectFile_G56(self):
        File = QFileDialog()
        FilePath, ok = File.getOpenFileName(self, '选择NC文件', 'D:/模型/')
        if ok:
            self.G56_Path.setText(FilePath)

    def SelectFile_G57(self):
        File = QFileDialog()
        FilePath, ok = File.getOpenFileName(self, '选择NC文件', 'D:/模型/')
        if ok:
            self.G57_Path.setText(FilePath)

    def SelectFile_G58(self):
        File = QFileDialog()
        FilePath, ok = File.getOpenFileName(self, '选择NC文件', 'D:/模型/')
        if ok:
            self.G58_Path.setText(FilePath)

    def SelectFile_G59(self):
        File = QFileDialog()
        FilePath, ok = File.getOpenFileName(self, '选择NC文件', 'D:/模型/')
        if ok:
            self.G59_Path.setText(FilePath)

    def msg_box(self):
        msg_box = QMessageBox()
        msg = '文件路径为空，请添加正确文件路径！！！'
        msg_box.question(self, '坐标G代码添加工具', msg, msg_box.ok)

    def GcodeChangeFunc(self, path, GCode):
        file_name = path
        f_new_name = "%s.new" % file_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(file_name, 'r', encoding='utf-8') as f_old:
            lines = f_old.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', GCode, 1)
                f_new.write(line)
            f_new.close()
            f_old.close()
            os.remove(file_name)
            os.rename(f_new_name, file_name)

    def path_list(self):
        G55_Path = self.G55_Path.text()
        G56_Path = self.G56_Path.text()
        G57_Path = self.G57_Path.text()
        G58_Path = self.G58_Path.text()
        G59_Path = self.G59_Path.text()
        pathList = [G55_Path, G56_Path, G57_Path, G58_Path, G59_Path]
        return pathList

    def btnChangeFunc(self):
        paths = self.path_list()
        for index, path in enumerate(paths):
            if index == 0:
                if path != '':
                    self.GcodeChangeFunc(path, GCode=' G55 ')
                    self.output_1.setText('G55添加成功')
                else:
                    print('G55 路径为空')
                    self.output_1.setText('G55路径为空')
            elif index == 1:
                if path != '':
                    self.GcodeChangeFunc(path, GCode=' G56 ')
                    self.output_2.setText('G56添加成功')
                else:
                    print('G56 路径为空')
                    self.output_2.setText('G56路径为空')
            elif index == 2:
                if path != '':
                    self.GcodeChangeFunc(path, GCode=' G57 ')
                    self.output_3.setText('G57添加成功')
                else:
                    print('G57 路径为空')
                    self.output_3.setText('G57路径为空')
            elif index == 3:
                if path != '':
                    self.GcodeChangeFunc(path, GCode=' G58 ')
                    self.output_4.setText('G58添加成功')
                else:
                    print('G58 路径为空')
                    self.output_4.setText('G58路径为空')
            elif index == 4:
                if path != '':
                    self.GcodeChangeFunc(path, GCode=' G59 ')
                    self.output_5.setText('G59添加成功')
                else:
                    print('G59 路径为空')
                    self.output_5.setText('G59路径为空')

    def Clear_Path(self):
        self.G55_Path.setText('')
        self.G56_Path.setText('')
        self.G57_Path.setText('')
        self.G58_Path.setText('')
        self.G59_Path.setText('')
