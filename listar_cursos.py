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