import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout, QLabel, QLineEdit, QPushButton
import mysql.connector as mycon

cx = mycon.connect(
    host="127.0.0.1",
    port="6556",
    user="root",
    password="senac@123",
    database="cursos"
)
cursor = cx.cursor()

class atualizarCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle("Cursos cadastrados")

        labelId = QLabel("Id do curso")
        self.editId = QLineEdit()

        labelCurso = QLabel("Nome do Curso")
        self.editCurso = QLineEdit()

        labelCh = QLabel("Carga Horária")
        self.editCh = QLineEdit()

        conCad = QPushButton("Concluir Cadastro")

        layout = QVBoxLayout()
        layout.addWidget(labelId)
        layout.addWidget(self.editId)

        layout.addWidget(labelCurso)
        layout.addWidget(self.editCurso)

        layout.addWidget(labelCh)
        layout.addWidget(self.editCh)

        layout.addWidget(conCad)
        conCad.clicked.connect(self.upCurso)

        tbCursos = QTableWidget(self)
        tbCursos.setColumnCount(3)
        tbCursos.setRowCount(15)

        headerLine = ["Id", "Curso", "Duração"]

        tbCursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("Select * from tbcursos")
        lintb = 0
        for linha in cursor:
            tbCursos.setItem(lintb, 0, QTableWidgetItem(str(linha[0])))
            tbCursos.setItem(lintb, 1, QTableWidgetItem(linha[1]))
            tbCursos.setItem(lintb, 2, QTableWidgetItem(linha[2]))
            lintb+=1

        layout.addWidget(tbCursos)
        self.setLayout(layout)

    def upCurso(self):
        if(self.editId.text()==""):
            print("Não é possível atualizar sem o Id do curso")
        elif(self.editCurso.text()=="" and self.editCh.text()==""):
            print("Não é possível atualizar sem dados")
        elif(self.editCurso.text()!="" and self.editCh.text()==""):
            cursor.execute("update tbcursos set nome_curso=%s where id_curso=%s",
                           (self.editCurso.text(), self.editId.text()))
        elif(self.editCurso.text()=="" and self.editCh.text()!=""):
            cursor.execute("update tbcursos set carga_horaria=%s where id_curso=%s",
                           (self.editCh.text(), self.editId.text()))
        else:
            cursor.execute("update tbcursos set nome_curso=%s, carga_horaria=%s where id_curso=%s",
                           (self.editCurso.text(), self.editCh.text(), self.editId.text()))
            
        cx.commit()
        print("Os dados foram atualizados.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = atualizarCursos()
    tela.show()
    sys.exit(app.exec_())