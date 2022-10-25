import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QImage


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 640
        self.height = 480
        # image
        self.image_width = 640
        self.image_height = 480
        self.setWindowTitle("Camera")
        self.setGeometry(0, 100, self.width, self.height)
        self.setFixedSize(self.width, self.height)
        self.ui()

    def ui(self):
        self.img_label = QLabel(self)
        self.img_label.setGeometry(0, 0, self.image_width, self.image_height)
        self.show()


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())
