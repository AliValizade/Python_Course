from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from functools import partial
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui", None)
        self.ui.show()
        self.ui.btn_add.clicked.connect(self.addNewTaskToDatabase)
        self.readFromDatabase()

    def addNewTaskToDatabase(self):
        title = self.ui.tb_title.text()
        description = self.ui.tb_description.text()
        database.addTask(title, description)
        self.readFromDatabase()
        self.ui.tb_title.setText('')
        self.ui.tb_description.setText('')

    def readFromDatabase(self):
        results = database.getAll()
        for i in range(len(results)):
            new_checkbox = QCheckBox()
            if results[i][3] == 1:
                new_checkbox.setChecked(True)
            new_title = QLabel()
            new_title.setText(results[i][1])
            new_details_btn = QPushButton()
            new_details_btn.setText('ℹ')
            new_delete_btn = QPushButton()
            new_delete_btn.setText('❌')
            self.ui.gridLayout.addWidget(new_checkbox, i, 0)
            self.ui.gridLayout.addWidget(new_title, i, 1)
            self.ui.gridLayout.addWidget(new_details_btn, i, 2)
            self.ui.gridLayout.addWidget(new_delete_btn, i, 3)
            self.ui.new_delete_btn.clicked.connect(partial(self.deleteTaskFromDatabase))
            

    def deleteTaskFromDatabase(self):
        pass

app = QApplication([])
window = MainWindow()
app.exec_()