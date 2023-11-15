import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5 import QtCore, QtWidgets
import random
from PyQt5 import uic

class Example(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.initUI()

    def initUI(self):
        self.btn = self.pushButton
        self.do_paint = False
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circ(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circ(self, qp):
        a = random.randint(30, 900)
        b = random.randint(30, 900)
        c = random.randint(30, 900)
        d = random.randint(30, 900)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(500, 30, a, a)
        qp.drawEllipse(30, 500, b, b)
        qp.drawEllipse(500, 500, c, c)
        qp.drawEllipse(30, 30, d, d)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())