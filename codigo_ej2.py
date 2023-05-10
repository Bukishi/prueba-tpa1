import sys
from PyQt6 import QtWidgets, uic

from VentanaPrincipal import Ui_VentanaPrincipal
from ventanasecundaria import Ui_VentanaSecundaria

class Mascota:
    def __init__(self, nombre: str, especie: str, edad: int, peso:float):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def __str__(self) -> str:
        return f"Mascota {self.nombre} de {self.edad} anios de la especie {self.especie} con {self.peso} Kg."

class VentanaSecundaria(QtWidgets.QWidget,Ui_VentanaSecundaria):
    def __init__(self,*args,obj=None,**kwargs):
        super(VentanaSecundaria, self).__init__(*args,**kwargs)
        self.setupUi(self)
    def cambioinfo(self,x):
        if self.x!=None:
            self.label_2.setText(_translate("VentanaSecundaria", self.x.__str__))



class Ventana(QtWidgets.QMainWindow, Ui_VentanaPrincipal):
    def __init__(self, *args, obj=None, **kwargs):
        super(Ventana, self).__init__(*args, **kwargs)
        #Implementación de Ui_VentanaPrincipal
        self.setupUi(self)
        m=guardar_mascota(self.entrada_nombre,self.entrada_peso,self.entrada_edad,self.entrada_especie)
        self.ventana_secundaria=VentanaSecundaria()
        self.pushButton.clicked.connect(self.react())
        ventana_secundaria.cambioinfo(m)
    def guardar_mascota(self,nombre,peso,edad,especie):  
        return Mascota(nombre, especie, edad, peso)
    def react(self):
        if self.ventana_secundaria.isVisible():
            self.ventana_secundaria.hide()
        else:
            self.ventana_secundaria.show()
    m=guardar_mascota()
    self.ventana_secundaria=VentanaSecundaria()
    self.pushButton.clicked.connect(self.react())
    ventana_secundaria.cambioinfo(m)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    vista = Ventana()
    vista.show()
    app.exec()