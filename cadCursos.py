import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit, QPushButton
import mysql.connector

cx = mysql.connector.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="cursos"
)

cursor = cx.cursor()

class cadCursos(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(60,60,600,300)
        self.setWindowTitle("Cadastro de Cursos")

        labelCurso = QLabel("Nome do curso: ")
        self.editCurso = QLineEdit()

        labelCh = QLabel("Carga Horária: ")
        self.editCh = QLineEdit()

        conCad = QPushButton("Concluir Cadastro")
        self.labelMsg = QLabel("|")

        layout = QVBoxLayout()
        layout.addWidget(labelCurso)
        layout.addWidget(self.editCurso)

        layout.addWidget(labelCh)
        layout.addWidget(self.editCh)

        layout.addWidget(conCad)
        conCad.clicked.connect(self.conCadastro)

        layout.addWidget(self.labelMsg)

        self.setLayout(layout)

    def conCadastro(self):
        cursor.execute("insert into tbcursos(nome_curso, carga_horaria)values(%s,%s)",
                       (self.editCurso.text(), self.editCh.text()))
        cx.commit()
        self.labelMsg.setText("Curso Cadastrado")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = cadCursos()
    tela.show()
    sys.exit(app.exec_())

