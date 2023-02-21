from PyQt5.QtWidgets import QMainWindow, QApplication
import sys

from loginmapa_ui import *


class TeladeLogin(QMainWindow, Ui_mwlogin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mwlogin()
        self.ui.setupUi(self)
        self.ui.btnentrar.clicked.connect(self.entrar_pagina_inicial)
        
    def entrar_pagina_inicial(self):
        usuario= self.ui.edtusuario.text()
        if not usuario:
            self.ui.edtusuario.setStyleSheet("background-color: #F25757;"\
                                                                "font: 16pt \"MS Shell Dlg 2\";"\
                                                                "border-top-left-radius: 7px;"\
                                                                "border-top-right-radius: 7px;"\
                                                                "border-bottom-right-radius: 7px;"\
                                                                "border-bottom-left-radius: 7px;")
        if  usuario:
            self.ui.edtusuario.setStyleSheet("background-color: #f2f2f2;"\
                                                                "font: 16pt \"MS Shell Dlg 2\";"\
                                                                "border-top-left-radius: 7px;"\
                                                                "border-top-right-radius: 7px;"\
                                                                "border-bottom-right-radius: 7px;"\
                                                                "border-bottom-left-radius: 7px;")
            
        senha = self.ui.edtsenha.text()
        if not senha:
            self.ui.edtsenha.setStyleSheet("background-color: #F25757;"\
                                                                "font: 16pt \"MS Shell Dlg 2\";"\
                                                                "border-top-left-radius: 7px;"\
                                                                "border-top-right-radius: 7px;"\
                                                                "border-bottom-right-radius: 7px;"\
                                                                "border-bottom-left-radius: 7px;")
        if  senha:
            self.ui.edtsenha.setStyleSheet("background-color: #f2f2f2;"\
                                                                "font: 16pt \"MS Shell Dlg 2\";"\
                                                                "border-top-left-radius: 7px;"\
                                                                "border-top-right-radius: 7px;"\
                                                                "border-bottom-right-radius: 7px;"\
                                                                "border-bottom-left-radius: 7px;")
            
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    Teladelog = TeladeLogin()
    Teladelog.show()
    qt.exec_()
