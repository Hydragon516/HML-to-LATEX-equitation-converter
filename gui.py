from PyQt5.QtCore import pyqtSignal, pyqtSlot, QThread
from PyQt5.QtWidgets import QDialog, QLineEdit, QTextBrowser, QVBoxLayout, QApplication
import hml_equation_parser as hp

class MyMainGUI(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.hml_input = QLineEdit(self)
        self.latex_output = QTextBrowser()

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.hml_input)
        vbox.addStretch(1)
        vbox.addWidget(self.latex_output)

        self.setLayout(vbox)

        self.setWindowTitle('HML to LATEX Equitation Converter')
        self.setGeometry(300, 300, 500, 200)


class MyMain(MyMainGUI):
    add_sec_signal = pyqtSignal()
    send_instance_singal = pyqtSignal("PyQt_PyObject")

    def __init__(self, parent=None):
        super().__init__(parent)

        self.hml_input.textChanged[str].connect(self.convert)

        self.th_convert = converter(parent=self)
        self.th_convert.updated_list.connect(self.list_update)
        self.show()

    def convert(self, hml):
        global input_hml
        input_hml = hml
        self.th_convert.start()

    @pyqtSlot(str)
    def list_update(self, msg):
        self.latex_output.setText(msg)


class converter(QThread):
    updated_list = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__()
        self.main = parent

    def __del__(self):
        self.wait()

    def run(self):
        global input_hml

        result = hp.eq2latex(input_hml)
        self.updated_list.emit(result)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MyMain()
    app.exec_()