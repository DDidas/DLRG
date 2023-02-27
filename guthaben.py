import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QDesktopWidget
from py import *


class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setFixedSize(300, 200)
        self.initUI()
    def initUI(self):
        self.lbl_username = QLabel(self)
        self.lbl_username.setText("Benutzername:")
        self.lbl_username.move(50, 50)
        self.txt_username = QLineEdit(self)
        self.txt_username.move(150, 50)
        self.txt_username.resize(100, 25)
        self.btn_login = QPushButton("Login", self)
        self.btn_login.move(100, 100)
        self.btn_login.clicked.connect(self.check_user)
        # Set relative sizes for the widgets
        self.lbl_username.setMinimumSize(100, 25)
        self.txt_username.setMinimumSize(150, 25)
        self.btn_login.setMinimumSize(100, 30)
        # Set font size relative to the widget size
        font = self.font()
        font.setPointSize(12)
        self.setFont(font)
        self.lbl_username.setFont(font)
        self.txt_username.setFont(font)
        self.btn_login.setFont(font)
        self.show()
    def check_user(self):
        if check_if_user_exists(self.txt_username.text()):
            self.new_window()
        else:
            QMessageBox.warning(self, "Fehler", "Benutzer nicht gefunden.")
    def new_window(self):
        self.close()
        self.window = QWidget()
        self.window.setWindowTitle("Erfolgreicher Login")
        self.window.setGeometry(400, 200, 300, 200)
        # Benutzername und Guthaben hinzufügen
        self.lbl_welcome = QLabel("Willkommen, " + self.txt_username.text(), self.window)
        self.lbl_welcome.move(50, 50)
        self.lbl_guthaben = QLabel("Guthaben: " + str(get_guthaben_by_id(self.txt_username.text())), self.window)
        self.lbl_guthaben.move(50, 70)
        # Knopf für Flaschenberechnung hinzufügen
        self.btn_calc = QPushButton("Flaschenberechnung", self.window)
        self.btn_calc.move(50, 100)
        self.btn_calc.clicked.connect(self.open_calc_page)
        # Knopf für Benutzerregistrierung hinzufügen
        self.btn_register = QPushButton("Benutzer registrieren", self.window)
        self.btn_register.move(150, 100)
        self.btn_register.clicked.connect(self.open_register_page)
        # Knopf für Guthabenaufladung hinzufügen
        self.btn_add_guthaben = QPushButton("Guthaben aufladen", self.window)
        self.btn_add_guthaben.move(50, 130)
        self.btn_add_guthaben.clicked.connect(self.open_add_guthaben_page)
        # Logout-Knopf hinzufügen
        self.btn_logout = QPushButton("Logout", self.window)
        self.btn_logout.move(150, 130)
        self.btn_logout.clicked.connect(self.logout)
        self.window.show()
    def open_calc_page(self):
        self.close()
        self.window_calc = QWidget()
        self.window_calc.setWindowTitle("Flaschenberechnung")
        self.window_calc.setGeometry(400, 200, 300, 200)
        self.lbl_restdruck = QLabel("Restdruck:", self.window_calc)
        self.lbl_restdruck.move(50, 50)
        self.txt_restdruck = QLineEdit(self.window_calc)
        self.txt_restdruck.move(150, 50)
        self.lbl_flaschengroesse = QLabel("Flaschengröße:", self.window_calc)
        self.lbl_flaschengroesse.move(50, 80)
        self.txt_flaschengroesse = QLineEdit(self.window_calc)
        self.txt_flaschengroesse.move(150, 80)
        self.btn_calc = QPushButton("Berechnen", self.window_calc)
        self.btn_calc.move(100, 120)
        self.btn_calc.clicked.connect(self.calculate_bottles)
        self.window_calc.show()
    def calculate_bottles(self):
        restdruck = float(self.txt_restdruck.text())
        flaschengroesse = float(self.txt_flaschengroesse.text())
        bottles = 1
        QMessageBox.information(self.window_calc, "Ergebnis", f"Es können {bottles} Flaschen abgefüllt werden.")
    def open_register_page(self):
        self.close()
        self.window_register = QWidget()
        self.window_register.setWindowTitle("Benutzerregistrierung")
        self.window_register.setGeometry(400, 200, 300, 200)
        self.lbl_new_username = QLabel("Benutzername:", self.window_register)
        self.lbl_new_username.move(50, 50)
        self.txt_new_username = QLineEdit(self.window_register)
        self.txt_new_username.move(150, 50)
        self.lbl_new_password = QLabel("Passwort:", self.window_register)
        self.lbl_new_password.move(50, 80)
        self.txt_new_password = QLineEdit(self.window_register)
        self.txt_new_password.move(150, 80)
        self.txt_new_password.setEchoMode(QLineEdit.Password)
        self.btn_register = QPushButton("Registrieren", self.window_register)
        self.btn_register.move(100, 120)
        self.btn_register.clicked.connect(self.register_user)
        self.window_register.show()
    def register_user(self):
        username = self.txt_new_username.text()
        guthaben = float(self.txt_new_password.text())
        if create_user(username, "name", guthaben):
            QMessageBox.information(self.window_register, "Erfolg", "Benutzer wurde erfolgreich registriert.")
    def open_add_guthaben_page(self):
        self.close()
        self.window_add_guthaben = QWidget()
        self.window_add_guthaben.setWindowTitle("Guthaben aufladen")
        self.window_add_guthaben.setGeometry(400, 200, 300, 200)
        self.lbl_add_guthaben = QLabel("Guthaben aufladen:", self.window_add_guthaben)
        self.lbl_add_guthaben.move(50, 50)
        self.txt_add_guthaben = QLineEdit(self.window_add_guthaben)
        self.txt_add_guthaben.move(150, 50)
        self.btn_add_guthaben = QPushButton("Aufladen", self.window_add_guthaben)
        self.btn_add_guthaben.move(100, 100)
        self.btn_add_guthaben.clicked.connect(self.add_guthaben)
        self.window_add_guthaben.show()
    def add_guthaben(self):
        username = self.txt_username.text()
        amount = float(self.txt_add_guthaben.text())
        amount = get_guthaben_by_id(username) + amount
        update_guthaben(username, amount)
        self.lbl_guthaben.setText("Guthaben: " + str(get_guthaben_by_id(self.txt_username.text())))
        self.window_add_guthaben.close()  # schließen des Fensters
    def logout(self):
        self.txt_username.setText("")
        self.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    sys.exit(app.exec_())
