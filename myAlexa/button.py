from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import main


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()

    def button_clicked(self):
        main.run_alexa()
        # self.update()

    def initUI(self):
        self.setGeometry(1600, 900, 300, 100)
        self.setWindowTitle("My Alexa")

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Ask me!")
        self.b1.move(100, 30)
        self.b1.clicked.connect(self.button_clicked)


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


while True:
    window()