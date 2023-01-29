from random import randint
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('guessNumber.ui', None)
        self.ui.show()

        self.randomNumber = randint(1, 100)
        
        self.ui.check_btn.clicked.connect(self.check)
        self.ui.newgame_btn.clicked.connect(self.newGame)
    
    def check(self):
        userGuess = self.ui.lineEdit.text()
        if userGuess!='':
            try:
                if int(userGuess)==self.randomNumber:
                    self.ui.guide_label.setText('You Won!👏')
                elif int(userGuess)>self.randomNumber:
                    self.ui.guide_label.setText('Go Down👇')
                elif int(userGuess)<self.randomNumber:
                    self.ui.guide_label.setText('Go UP👆')
            except:
                self.ui.guide_label.setText('Give me a number!')
        else:
            self.ui.guide_label.setText('')

    def newGame(self):
        self.randomNumber = randint(1, 100)
        self.ui.guide_label.setText('')
        self.ui.lineEdit.setText('')


app = QApplication([])
window = MainWindow()
app.exec()