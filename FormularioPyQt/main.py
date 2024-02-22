from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QHBoxLayout, QSpinBox, QVBoxLayout, QComboBox, QFormLayout, QTextEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import sys

class Formulario(QWidget):

    def __init__(self):
        super(Formulario,self).__init__()
        self.resize(300,400)
        self.setWindowTitle("Hospital B")
        self.display_widgets()

    def display_widgets(self):
        lbl_titulo = QLabel("Turno Médico", self)
        lbl_titulo.setAlignment(Qt.AlignCenter)
        lbl_titulo.setFont(QFont("Arial", 18))

        # 3 line edit
        lned_nombre = QLineEdit(self)
        lned_direccion = QLineEdit(self)
        lned_telefono = QLineEdit(self)
        lned_telefono.setInputMask("+54-000-0000000")

        hlyt_edades = QHBoxLayout()

        lbl_edad = QLabel("Edad")
        spbox_edad = QSpinBox(self)
        spbox_edad.setRange(1, 110)
        lbl_altura = QLabel("Altura", self)
        lned_altura = QLineEdit(self)
        lned_altura.setPlaceholderText("cm")
        lbl_peso = QLabel("Peso", self)
        lned_peso = QLineEdit(self)
        lned_peso.setPlaceholderText("kg")

        hlyt_edades.addWidget(lbl_edad)
        hlyt_edades.addWidget(spbox_edad)
        hlyt_edades.addWidget(lbl_altura)
        hlyt_edades.addWidget(lned_altura)
        hlyt_edades.addWidget(lbl_peso)
        hlyt_edades.addWidget(lned_peso)

        #ComboBox
        cbox_genero = QComboBox(self)
        cbox_genero.addItems(["Femenino", "Masculino", "No especificado"])

        #TextEdit
        txted_turno = QTextEdit(self)
        txted_turno.setPlaceholderText("Especifique su turno médico")

        # ComboBox
        cbox_sangre = QComboBox(self)
        cbox_sangre.addItems(["A", "B", "AB", "0"])

        #Horario
        hlyt_horario = QHBoxLayout()
        spbox_hora = QSpinBox(self)
        spbox_hora.setRange(1,12)
        cbox_minutos = QComboBox(self)
        cbox_minutos.addItems([":00", ":15", ":30", ":45"])
        cbox_ampm = QComboBox(self)
        cbox_ampm.addItems(["Am", "Pm"])
        hlyt_horario.addWidget(spbox_hora)
        hlyt_horario.addWidget(cbox_minutos)
        hlyt_horario.addWidget(cbox_ampm)

        btn_enviar = QPushButton("Enviar")
        btn_enviar.clicked.connect(self.close)

        flyt_principal = QFormLayout(self)
        flyt_principal.addRow(lbl_titulo)
        flyt_principal.addRow("Nombre", lned_nombre)
        flyt_principal.addRow("Dirección", lned_direccion)
        flyt_principal.addRow("Teléfono", lned_telefono)
        flyt_principal.addRow(hlyt_edades)
        flyt_principal.addRow("Género", cbox_genero)
        flyt_principal.addRow("Turno", txted_turno)
        flyt_principal.addRow("Tipo de sangre", cbox_sangre)
        flyt_principal.addRow("Hora", hlyt_horario)
        flyt_principal.addRow(btn_enviar)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Formulario()
    window.show()
    sys.exit(app.exec_())