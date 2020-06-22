# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QMainWindow, QFileDialog
from view import Ui_MainWindow
from LineEdit import LineEditDrop
import os


class Functions(QMainWindow, Ui_MainWindow, LineEditDrop):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        LineEditDrop.__init__(self)

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

    def ChangeFunc(self):
        G55 = self.G55_Path.text()
        G56 = self.G56_Path.text()
        G57 = self.G57_Path.text()
        G58 = self.G58_Path.text()
        G59 = self.G59_Path.text()
        Files = [G55, G56, G57, G58, G59]
        G_Code = [' G55 ', ' G56 ', ' G57 ', ' G58 ', ' G59 ']
        for file in Files:
            f_name = file
            f_new_name = '%s.new' % f_name
            old_str = 'N0010 G40 G17 G90 G71'
            f_new = open(f_new_name, mode='w', encoding='utf-8')
            f_old = open(f_name, mode='r', encoding='utf-8')
            lines = f_old.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', '', 1)
                f_new.write(line)
            f_new.close()
            f_old.close()

    def G55_Change(self):
        f_name = self.G55_Path.text()
        f_new_name = '%s.new' % f_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', ' G55 ', 1)
                f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)

    def G56_Change(self):
        f_name = self.G56_Path.text()
        f_new_name = '%s.new' % f_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', ' G56 ', 1)
                f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)

    def G57_Change(self):
        f_name = self.G57_Path.text()
        f_new_name = '%s.new' % f_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', ' G57 ', 1)
                f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)

    def G58_Change(self):
        f_name = self.G58_Path.text()
        f_new_name = '%s.new' % f_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', ' G58 ', 1)
                f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)

    def G59_Change(self):
        f_name = self.G59_Path.text()
        f_new_name = '%s.new' % f_name
        old_str = 'N0010 G40 G17 G90 G71'
        f_new = open(f_new_name, 'w', encoding='utf-8')
        with open(f_name, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                if old_str in line:
                    line = line.replace(' ', ' G59 ', 1)
                f_new.write(line)
        f_new.close()
        f.close()
        os.remove(f_name)
        os.rename(f_new_name, f_name)

    def dragEnterEvent(self, event):
        FilePath = (event.mimeData().urls())[0].toLocalFile()
        self.G55_Path.setText(FilePath)


