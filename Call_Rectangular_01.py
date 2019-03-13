import sys
from PyQt5.QtWidgets import QDialog, QApplication
from Rectangular_01 import *

class MyForm(QDialog): #creates a new MyForm class that inherits from the base class, QDialog.
    def __init__(self): #the default constructor for QDialog.
        super().__init__() #
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calcQ)
        self.show()

    def calcQ(self):
        # Collect the input values
        n = float(self.ui.lEdt_n.text())
        S = float(self.ui.lEdt_S.text())
        y = float(self.ui.lEdt_y.text())
        W = float(self.ui.lEdt_B.text())

        # make necessary backround calculations
        A = y * W
        P = W + 2 * y
        R = A / P

        Q = 1/n * A * R**0.667 * S**0.5

        self.ui.label_6.setText(str('%.2f' %Q))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ww = MyForm()  # MyForm is a general class, now w is a specific object/instance of MyForm
    ww.show()
    sys.exit(app.exec_())



