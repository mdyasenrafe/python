import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPainter, QImage
from PyQt5.QtCore import QTimer


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

        # setuup timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update)
        self.ui()

    def ui(self):
        self.img_label = QLabel(self)
        self.img_label.setGeometry(0, 0, self.image_width, self.image_height)
        if not self.timer.isActive():
            self.cap = cv2.VideoCapture(0)
            self.timer.start(20)

        self.show()

    def update(self):
        pass


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())
