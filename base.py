from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import psycopg2
from tkinter import messagebox
from loginmapa_ui import *

conexao = psycopg2.connect( host="localhost",
                                                database="projectmapa",
                                                user='postgres',
                                                password='postgres')   

cursor=conexao.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios(\
                        idUsuario BIGSERIAL PRIMARY KEY ,\
                        usuario VARCHAR(20),\
                        nomeUsuario VARCHAR(20),\
                        sobrenomeUsuario VARCHAR(20),\
                        senhaUsuario VARCHAR(20),\
                        email VARCHAR(60),\
                        inativo boolean DEFAULT  FALSE,\
                        dataNascimento DATE NOT NULL,\
                        dataCadastro DATE NOT NULL DEFAULT CURRENT_DATE,\
                        usermaster boolean DEFAULT FALSE\
                        )")
conexao.commit()
cursor.close()

class TeladeLogin(QMainWindow, Ui_mwlogin):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mwlogin()
        self.ui.setupUi(self)
        self.ui.btnentrar.clicked.connect(self.entrar_pagina_inicial)
        
    def entrar_pagina_inicial(self):
        usuario= self.ui.edtusuario.text()
        usuario_replace=usuario.replace("'","''")
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
            if usuario and senha:
                cursor=conexao.cursor()

                cursor.execute(f"SELECT usuario, senhausuario FROM usuarios WHERE  usuario = '{usuario_replace}'")
                pesquisa_usuario=cursor.fetchall()
                if len(pesquisa_usuario) == 0:
                    messagebox.showinfo('info', 'Usuario não encontrado')
                    
                else:
                    for linha in pesquisa_usuario:
                        if linha[1] == senha:
                            print("entrou")
                            
                        else:
                            messagebox.showinfo('info', 'Senha invalida')
                
if __name__ == '__main__':
    qt = QApplication(sys.argv)
    Teladelog = TeladeLogin()
    Teladelog.show()
    qt.exec_()
