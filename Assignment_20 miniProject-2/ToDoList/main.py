from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from functools import partial
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui", None)
        self.ui.show()
        self.readFromDatabase()
        self.ui.btn_add.clicked.connect(self.addNewTaskToDatabase)
        

    def addNewTaskToDatabase(self):
        title = self.ui.tb_title.text()
        description = self.ui.tb_description.text()
        time = self.ui.tb_time.text()
        result = database.getAll()
        new_id = 1
        for i in range(len(result)):
            new_id = result[i][0] + 1
        database.addTask(new_id, title, description, time)
        self.readFromDatabase()
        self.ui.tb_title.setText('')
        self.ui.tb_description.setText('')
        self.ui.tb_time.setText('')
        
    def updateTask(self):
        pass

    def clearUI_tasks(self):
        for i in reversed(range(self.ui.gridLayout.count())): 
            self.ui.gridLayout.itemAt(i).widget().deleteLater()

    def readFromDatabase(self):
        results = database.getAll()
        self.lastID = 0
        for i in range(len(results)):
            new_id = QLabel()
            new_id.setText(str(results[i][0]))
            new_title = QLabel()
            new_title.setText(results[i][1])
            new_checkbox = QCheckBox()
            new_checkbox.setObjectName(f'chkBx_{results[i][0]}')
            new_checkbox.stateChanged.connect(self.doneTask)
            if results[i][3] == 1:
                new_checkbox.setChecked(True)
            new_details_btn = QPushButton()
            new_details_btn.setText('ℹ')
            new_details_btn.setObjectName(f'detail_btn_{results[i][0]}')
            new_delete_btn = QPushButton()
            new_delete_btn.setText('❌')
            new_delete_btn.setObjectName(f'delete_btn_{results[i][0]}')
            self.lastID += 1
            
            self.ui.gridLayout.addWidget(new_id, i, 0)
            self.ui.gridLayout.addWidget(new_title, i, 1)
            self.ui.gridLayout.addWidget(new_checkbox, i, 2)
            self.ui.gridLayout.addWidget(new_details_btn, i, 3)
            self.ui.gridLayout.addWidget(new_delete_btn, i, 4)
            
            new_details_btn.clicked.connect(self.taskDetails)
            new_delete_btn.clicked.connect(self.deleteTaskFromDatabase)            

    def doneTask(self):
        id = self.sender().objectName().split('_')[-1]
        if self.sender().isChecked():
            database.update_done(id, 1)
        else:
            database.update_done(id, 0)

    def deleteTaskFromDatabase(self):
        del_id = self.sender().objectName().split('_')[-1]
        database.deleteTask(del_id)
        self.clearUI_tasks()
        self.readFromDatabase()

    def taskDetails(self):
        id = self.sender().objectName().split('_')[-1]
        self.ui = taskDetailsWindow(id)

class taskDetailsWindow(QWindow):
    def __init__(self, id):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('details.ui', None)
        self.ui.show()

        details = database.getDetails(id)
        self.ui.id_label.setText(f'{details[0][0]}')
        self.ui.title_label.setText(f'{details[0][1]}')
        self.ui.description_label.setText(f'{details[0][2]}')
        self.ui.time_label.setText(f'{details[0][4]}')
        if details[0][3]==1:
            self.ui.done_label.setText('YES')
        else:
            self.ui.done_label.setText('NO')

        self.ui.back_btn.clicked.connect(self.backToMainWindow)
    
    def backToMainWindow(self):
        self.ui = MainWindow()


app = QApplication([])
window = MainWindow()
app.exec_()