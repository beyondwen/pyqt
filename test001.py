# -*- coding: utf-8 -*-
"""第一个程序"""

import sys

from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
first_window = QtWidgets.QWidget()
first_window.resize(400, 300)
first_window.setWindowTitle("我的都一个pyqt5程序")
first_window.show()
sys.exit(app.exec_())
