import math
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtUiTools import QUiLoader

class cal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.divNum1 = 0
        self.sumNum1 = 0
        self.subNum1 = 0
        self.mulNum1 = 0
        self.perNum1 = 0
        self.decimal_count = 0
        loader = QUiLoader()
        self.ui = loader.load('form.ui', None)
        self.ui.show()
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.seven)
        self.ui.eight.clicked.connect(self.eight)
        self.ui.nine.clicked.connect(self.nine)
        self.ui.zero.clicked.connect(self.zero)
        self.ui.decimal.clicked.connect(self.decimal)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.sum.clicked.connect(self.sum)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.cot.clicked.connect(self.cot)
        self.ui.log.clicked.connect(self.log)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.sign.clicked.connect(self.sign)
        self.ui.percent.clicked.connect(self.percent)
        self.ui.equal.clicked.connect(self.equal)
    # Functions of numbers
    def one(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '1')
    def two(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '2')
    def three(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '3')
    def four(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '4')
    def five(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '5')
    def six(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '6')
    def seven(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '7')
    def eight(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '8')
    def nine(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '9')
    def zero(self):
        if self.ui.label.text() == '0': self.ui.label.setText('')
        self.ui.label.setText(self.ui.label.text() + '0')
    def decimal(self):
        if self.decimal_count == 0:
            self.ui.label.setText(self.ui.label.text() + '.')
            self.decimal_count += 1

    # Functions of operators
    def sum(self):
        self.sumNum1 = float(self.ui.label.text())
        self.ui.label.setText('')
        self.decimal_count = 0
    def sub(self):
        self.subNum1 = float(self.ui.label.text())
        self.ui.label.setText('')
        self.decimal_count = 0
    def mul(self):
        self.mulNum1 = float(self.ui.label.text())
        self.ui.label.setText('')
        self.decimal_count = 0
    def div(self):
        self.divNum1 = float(self.ui.label.text())
        self.ui.label.setText('')
        self.decimal_count = 0
    def sin(self):
        self.ui.label.setText(str(round(math.sin(math.radians(float(self.ui.label.text()))), 2)))
        self.decimal_count = 0
    def cos(self):
        self.ui.label.setText(str(round(math.cos(math.radians(float(self.ui.label.text()))), 2)))
        self.decimal_count = 0
    def tan(self):
        self.ui.label.setText(str(round(math.tan(math.radians(float(self.ui.label.text()))), 2)))
        self.decimal_count = 0
    def cot(self):
        self.ui.label.setText(str(round(1 / math.tan(math.radians(float(self.ui.label.text()))), 2)))
        self.decimal_count = 0
    def log(self):
        self.ui.label.setText(str(round(math.log10(float(self.ui.label.text())), 2)))
        self.decimal_count = 0
    def sqrt(self):
        self.ui.label.setText(str(round(math.sqrt(float(self.ui.label.text())), 2)))
        self.decimal_count = 0
    def percent(self):
        self.perNum1 = float(self.ui.label.text()) / 100
        self.ui.label.setText('')
        self.decimal_count = 0
    def sign(self):
        self.ui.label.setText(str(float(self.ui.label.text()) * -1))
        self.decimal_count = 0
    def clear(self):
        self.ui.label.setText('0')
    def equal(self):
        self.decimal_count = 0
        if self.sumNum1 != 0:
            self.ui.label.setText(str(self.sumNum1 + float(self.ui.label.text())))
            self.sumNum1 = 0
        elif self.subNum1 != 0:
            self.ui.label.setText(str(self.subNum1 - float(self.ui.label.text())))
            self.subNum1 = 0
        elif self.mulNum1 != 0:
            if self.perNum1 != 0:
                self.ui.label.setText(str(round(self.perNum1 * self.mulNum1, 2)))
                self.perNum1 = 0
            self.ui.label.setText(str(self.mulNum1 * float(self.ui.label.text())))
            self.mulNum1 = 0
        elif self.divNum1 != 0:
            self.ui.label.setText(str(round(self.divNum1 / float(self.ui.label.text()), 2)))
            self.divNum1 = 0
        

app = QApplication([])
window = cal()

app.exec()


