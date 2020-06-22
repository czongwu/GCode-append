# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QLineEdit


class MyLineEdit(QLineEdit):
    def __init__(self, *args, **kwargs):
        super(MyLineEdit, self).__init__(*args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().text().endswith('.NC'):
            event.accept()
        # if event.mimeData().hasUrls():
        #     event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        path = event.mimeData().text().replace('file:///', '')
        self.setText(path)
        # files = ''
        # urls = [u for u in event.mimeData().urls()]
        # for url in urls:
        #     files.replace(files, url.toLocalFile())
        #     self.setText(files)
