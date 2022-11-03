from random import randint
from functools import partial
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
# Global Var
X_SCORE = 0; O_SCORE = 0; DRAW = 0; WIN_SCORE = 5
class TicTacToa(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('ttt.ui', None)
        self.ui.show()
        self.game = [[None for i in range(3)] for j in range(3)]
        self.game[0][0] = self.ui.btn1; self.game[0][1] = self.ui.btn2; self.game[0][2] = self.ui.btn3
        self.game[1][0] = self.ui.btn4; self.game[1][1] = self.ui.btn5; self.game[1][2] = self.ui.btn6
        self.game[2][0] = self.ui.btn7; self.game[2][1] = self.ui.btn8; self.game[2][2] = self.ui.btn9
        self.player = 'X'
        self.AI = True
        self.game_start()
        self.ui.reset.clicked.connect(self.reset)
        self.ui.about.triggered.connect(self.about)
        self.ui.exit.triggered.connect(exit)
    def game_start(self):
        self.show_scoreBourad()
        self.cell_empty = 9
        for i in range(3):
            for j in range(3):
                self.game[i][j].setText('')
                self.game[i][j].setStyleSheet('color: black; background-color: skyblue; border-radius: 10px')
                self.game[i][j].clicked.connect(partial(self.play, i, j))
    def show_scoreBourad(self):
        self.ui.score.setText(str(X_SCORE) + ' - ' + str(O_SCORE))   
    def play(self, x, y):
        # if self.ui.ai.triggered.connect():
        #     self.AI = True
        # elif self.ui.players.triggered.connect():
        #     self.AI = False
        if self.game[x][y].text() == '':
            if self.player == 'X':
                self.game[x][y].setText('X')
                self.game[x][y].setStyleSheet('color: green; background-color: lightgreen; border-radius: 10px; font-size: 32px')
                self.cell_empty -=1
                self.player = 'O'
            else:
                self.game[x][y].setText('O')
                self.game[x][y].setStyleSheet('color: red; background-color: pink; border-radius: 10px; font-size: 32px')
                self.cell_empty -=1
                self.player = 'X'
        self.check()
        self.step_winner()
        # if self.AI == True:
        #     self.play(self.AI_round)
    
    def AI_round(self):
        while True:
            x = randint(0, 2); y = randint(0, 2)
            if self.game[x][y].text() == '':
                break
        return x, y        
    def check(self):
        self.diagonal_sort_x = 0; self.diagonal_sort_o = 0
        for i in range(3):
            self.row_sort_x = 0; self.col_sort_x = 0; self.row_sort_o = 0; self.col_sort_o = 0
            for j in range(3):
                if self.game[i][j].text() == 'X':
                    self.row_sort_x += 1
                if self.game[j][i].text() == 'X':
                    self.col_sort_x += 1
                if self.game[i][j].text() == 'O':
                    self.row_sort_o += 1
                if self.game[j][i].text() == 'O':
                    self.col_sort_o += 1
                if i == j:
                    if self.game[i][j].text() == 'O':
                        self.diagonal_sort_o += 1
                    if self.game[i][j].text() == 'X':
                        self.diagonal_sort_x += 1
                if self.row_sort_x == 3 or self.col_sort_x == 3 or self.diagonal_sort_x == 3 or (self.game[0][2].text() == 'X' and self.game[1][1].text() == 'X' and self.game[2][0].text() == 'X'):
                    return 'X'
                elif self.row_sort_o == 3 or self.col_sort_o == 3 or self.diagonal_sort_o == 3 or (self.game[0][2].text() == 'O' and self.game[1][1].text() == 'O' and self.game[2][0].text() == 'O'):
                    return 'O'
                elif self.cell_empty == 0:
                    return 'DRAW'            
    def step_winner(self):
        global X_SCORE, O_SCORE, DRAW
        winner = self.check()
        if winner == 'X':
            self.msg_box('X wins.')
            X_SCORE += 1
            self.final_winner('Congratulations, Player X wins✅ ', X_SCORE)
            self.game_start()
        elif winner == 'O':
            self.msg_box('O wins.')
            O_SCORE += 1
            self.final_winner('Congratulations, Player O wins✅ ', O_SCORE)
            self.game_start()
        elif winner == 'DRAW':
            self.msg_box('Draw!!')
            DRAW += 1
            self.final_winner('Sorry! 5 Draw happened!!', DRAW)
            self.game_start()
    def final_winner(self, msg, score):
        self.show_scoreBourad()
        if score == WIN_SCORE:
            self.msg_box(msg)
            self.reset()
    def msg_box(self, msg):
        msgbox = QMessageBox()
        msgbox.setText(msg)
        msgbox.exec()        
    def reset(self):
        global X_SCORE, O_SCORE, DRAW
        X_SCORE = 0; O_SCORE = 0; DRAW = 0
        self.game_start()
    def about(self):
        self.msg_box("TicTacToe:\nIt's a game for two players who take turns marking the spaces in a three-by-three grid with X or O.\nThe player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row is the winner.")
app = QApplication([])
window = TicTacToa()
app.exec()