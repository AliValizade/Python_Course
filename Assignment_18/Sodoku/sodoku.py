from random import randint
from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import *

class sodoku(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('sodoku.ui')
        self.game = [[None for i in range(9)] for j in range(9)]
        self.user_cells = []
        # --------------------------------------- Creat empty sodoku 9*9 -----------------------------
        for i in range(9):
            for j in range(9):
                cell = QLineEdit()
                cell.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
                cell.setStyleSheet('font-size: 18px; color: blue; padding: 0px')
                cell.setAlignment(Qt.AlignCenter)
                self.ui.myGrid.addWidget(cell, i, j)
                self.game[i][j] = cell
        
        self.ui.show()
        self.style_sheet()
        self.ui.btn_newGame.clicked.connect(self.newGame)
        self.ui.btn_checkGame.clicked.connect(self.check)
        self.ui.btn_reset.clicked.connect(self.clear)
        self.ui.mode.triggered.connect(self.mode)
        self.ui.about.triggered.connect(self.about)
        self.ui.exit.triggered.connect(exit)

    def newGame(self): 
        self.style_sheet()
        self.user_cells.clear()
        try:
            myFile = open(f"data/s{randint(1, 7)}.txt", 'r')
            big_str = myFile.read()
            rows = big_str.split('\n')
            for i in range(9):
                numbers = rows[i].split(' ')
                for j in range(9):
                    self.game[i][j].setText('')
                    self.game[i][j].setReadOnly(False)
                    if numbers[j] != '0':
                        self.game[i][j].setText(numbers[j])
                        self.game[i][j].setReadOnly(True)
                    else:
                        self.user_cells.append(self.game[i][j])
        except: 
            self.msg_Box('Error! Cannot open file.')
    def style_sheet(self):
        for i in range(9):
            for j in range(9):
                self.game[i][j].setMaxLength(1)
                if i == 2 or i == 5:
                    self.game[i][j].setStyleSheet('font-size: 18px; padding: 0px; margin-bottom: 3px')
                elif j == 2 or j == 5:
                    self.game[i][j].setStyleSheet('font-size: 18px; padding: 0px; margin-right: 3px')
                else :
                    self.game[i][j].setStyleSheet('font-size: 18px; padding: 0px; margin: 0px')
                if (i == 2 and j == 2) or (i == 2 and j == 5) or (i == 5 and j == 2) or (i == 5 and j == 5):
                    self.game[i][j].setStyleSheet('font-size: 18px; padding: 0px; margin-right: 3px; margin-bottom: 3px')    
                

    def check(self):
        flag = True
        empty_cell = 0
        self.style_sheet()
        # --------------------------------------- check rows ------------------------------------------
        for row in range(9):    
            for i in range(9):
                for j in range(9):
                    if self.game[row][i].text() == self.game[row][j].text() and i!=j and self.game[row][i].text() != '':
                        self.game[row][j].setStyleSheet('font-size: 18px; color: green; background-color: pink; padding: 0px')
                        flag = False
        # --------------------------------------- check columns ---------------------------------------
        for col in range(9):    
            for i in range(9):
                for j in range(9):
                    if self.game[i][col].text() == self.game[j][col].text() and i!=j and self.game[i][col].text() != '':
                        self.game[j][col].setStyleSheet('font-size: 18px; color: green; background-color: pink; padding: 0px')
                        flag = False
        # --------------------------------------- check squars(3*3) -----------------------------------
        for row in range(0, 9, 3):    
            for col in range(0, 9, 3):
                for r_square in range(row, row + 3):
                     for c_square in range(col, col + 3):
                        for i in range(row, row + 3):
                            for j in range(col, col + 3):
                                if self.game[r_square][c_square].text() == self.game[i][j].text() and (i!=r_square or j!=c_square) and self.game[r_square][c_square].text() != '':
                                    self.game[r_square][c_square].setStyleSheet('font-size: 18px; color: black; background-color: pink; padding: 0px')
                                    self.game[i][j].setStyleSheet('font-size: 18px; color: black; background-color: pink; padding: 0px')
                                    flag = False
        # --------------------------------------- if solved, show msg ---------------------------------                            
        for i in range(9):
            for j in range(9):
                if self.game[i][j].text() == '':
                    empty_cell += 1
                    # self.style_sheet()
        if empty_cell == 0 and flag:
            self.msg_Box('Congratulations, it solved✅')

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.style_sheet()
                if self.game[i][j] in self.user_cells:
                    self.game[i][j].setText('')
    
    def mode(self):
        if self.ui.mode.text() == 'Dark Mode':
            self.ui.mode.setText('Light Mode')
            self.ui.setStyleSheet('background-color: gray')
        else:
            self.ui.mode.setText('Dark Mode')
            self.ui.setStyleSheet('')
    def about(self):
        self.msg_Box('Sudoku is a logic-based, combinatorial number-placement puzzle.\n In classic Sudoku, the objective is to fill a 9 × 9 grid with digits so that each column, each row, and each of the nine 3 × 3 subgrids that compose the grid contain all of the digits from 1 to 9.')
    def msg_Box(self, msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.exec()

app = QApplication([])
window = sodoku()
app.exec()

