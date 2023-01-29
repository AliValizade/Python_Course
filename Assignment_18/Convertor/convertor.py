from unittest import result
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from PySide6.QtCore import *
from unit_converter.converter import converts

class Convertor(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load('convertor.ui', None)
        self.ui.show()

        self.ui.calculate.clicked.connect(self.calculate)
        self.ui.convert_cbox.currentTextChanged.connect(self.change_comboBox)
        self.ui.convert_cbox.addItems(['Mass','Length', 'DigitalVolume', 'Temperature'])

    def change_comboBox(self):
        self.ui.from_cbox.clear()
        self.ui.to_cbox.clear()
        if self.ui.convert_cbox.currentText() == 'Mass':
            self.ui.from_cbox.addItems(['g','kg','T','P'])
            self.ui.to_cbox.addItems(['kg','g','T','P'])
        elif self.ui.convert_cbox.currentText()=='Length':
            self.ui.from_cbox.addItems(['mm','cm','m','km','in'])
            self.ui.to_cbox.addItems(['cm','mm','m','km','in'])
        elif self.ui.convert_cbox.currentText()=='DigitalVolume':
            self.ui.from_cbox.addItems(['bit','byte','KByte','MByte','GByte','TByte'])
            self.ui.to_cbox.addItems(['byte','bit','KByte','MByte','GByte','TByte'])
        elif self.ui.convert_cbox.currentText()=='Temperature':
            self.ui.from_cbox.addItems(['°C','°F','°K'])
            self.ui.to_cbox.addItems(['°F','°C','°K'])
    def calculate(self):
        quantity = self.ui.input.text()
        current_unit = self.ui.from_cbox.currentText()
        converted_unit = self.ui.to_cbox.currentText()
        result = converts(quantity= quantity + current_unit, desired_unit= converted_unit)
        self.ui.output.setText(str(round(float(result), 2)))

app = QApplication([])
window = Convertor()
app.exec()