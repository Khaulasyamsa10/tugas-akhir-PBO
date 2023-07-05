from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from harrypotterfams import Ui_Form
class Login(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.show_message)
    def show_message(self):
        name = self.lineEdit.text()
        QMessageBox.information(self, "HARRY POTTER FAMS", f"Welcome to Harry Potter Fams, {name}!")

app = QApplication([])
form = Login()
form.show()
app.exec_()