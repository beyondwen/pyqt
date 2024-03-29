from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys


class SignalSlot(QWidget):
    def __int__(self):
        super(SignalSlot, self).__init__()
        self.initUI()

    def initUI(self):
        self.controlsGroup = QGroupBox('信号和槽')
        self.lcdNumber = QLCDNumber(self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.pBar = QProgressBar(self)
        vBox = QVBoxLayout()
        vBox.addWidget(self.pBar)
        vBox.addWidget(self.lcdNumber)
        vBox.addWidget(self.slider)
        self.controlsGroup.setLayout(vBox)
        controlsLayout = QGridLayout()
        self.label1 = QLabel('保存状态：')
        self.saveLabel = QLabel()
        self.label2 = QLabel('运行状态')
        self.runLabel = QLabel()
        self.buttonSave = QPushButton('保存')  # 添加按钮
        self.buttonRun = QPushButton('运行')
        self.buttonStop = QPushButton('停止')
        self.buttonDisconnected = QPushButton('停止绑定')
        self.buttonconnected = QPushButton('开始绑定')
        controlsLayout.addWidget(self.label1, 0, 0)
        controlsLayout.addWidget(self.saveLabel, 0, 1)
        controlsLayout.addWidget(self.label2, 1, 0)
        controlsLayout.addWidget(self.runLabel, 1, 1)
        controlsLayout.addWidget(self.buttonSave, 2, 0)
        controlsLayout.addWidget(self.buttonRun, 2, 1)
        controlsLayout.addWidget(self.buttonRun, 2, 2)
        controlsLayout.addWidget(self.buttonDisconnected, 3, 0)
        controlsLayout.addWidget(self.buttonDisconnected, 3, 1)
        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addLayout(controlsLayout)
        self.setLayout(layout)
        self.buttonRun.clicked.connect(self.buttonSave.clicked)
        self.slider.valueChanged.connect(self.pBar.setValue)
        self.slider.valueChanged.connect(self.lcdNumber.display)
        self.buttonSave.clicked.connect(self.showMessage)
        self.buttonRun.clicked.connect(self.showMessage)
        self.buttonDisconnect.clicked.connect(self.unbindConnection)
        self.buttonConnect.clicked.connect(self.bindConnection)
        self.buttonStop.clicked.connect(self.stop)
        self.setGeometry(300, 500, 500, 180)
        self.setWindowTitle('信号和槽')

    def showMessage(self):
        if self.sender().text() == "保存":
            self.saveLabel.setText("Saved")
        elif self.sender().text() == "运行":
            self.saveLabel.setText("Saved")
            self.runLabel.setText("Running")

    def unbindConnection(self):
        self.slider.valueChanged.disconnect()

    def bindConnection(self):
        self.slider.valueChanged.connect(self.pBar.setValue)
        self.slider.valueChanged.connect(self.lcdNumber.display)

    def stop(self):
        self.saveLabel.setText('')
        self.runLabel.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SignalSlot()
    ex.show()
    sys.exit(app.exec_())
