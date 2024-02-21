# Arquivos de cadastro, atualização e visualização de cursos

Foi criado três arquivos conectados remotamente a um banco de dados, para poder cadastrar novos cursos, listar os cursos para ter uma melhor visualização e um para atualizar os dados já cadastrados tudo em um ambiente gráfico. Aqui estão os códigos a seguir dos arquivos utilizados:

### Arquivo de cadastro

```python
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


```

### Arquivo de listagem

```python
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

class mostrarCursos(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(100,100,500,300)
        self.setWindowTitle("Cursos cadastrados")

        tablecursos = QTableWidget(self)
        tablecursos.setColumnCount(3)
        tablecursos.setRowCount(15)

        headerLine = ["Id","Curso","Duração"]

        tablecursos.setHorizontalHeaderLabels(headerLine)
        cursor.execute("select * from tbcursos")
        lintb = 0
        for linha in cursor:
            tablecursos.setItem(lintb, 0, QTableWidgetItem(str(linha[0])))
            tablecursos.setItem(lintb, 1, QTableWidgetItem(linha[1]))
            tablecursos.setItem(lintb, 2, QTableWidgetItem(linha[2]))
            lintb+=1
        
        layout = QVBoxLayout()
        layout.addWidget(tablecursos)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    tela = mostrarCursos()
    tela.show()
    sys.exit(app.exec_())


```

### Arquivo de atualização

```python
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


```