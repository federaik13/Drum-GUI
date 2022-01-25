# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Batacompleta.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sounddevice as sd
import soundfile as sf

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(614, 487)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Drums.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label") #Defino los nombres de los botones
        redo = self.pushButton = QtWidgets.QPushButton(Dialog)
        redo.clicked.connect(self.Play_redo)  #Asigno conexion con audio
        self.pushButton.setGeometry(QtCore.QRect(50, 310, 151, 131))
        self.pushButton.setObjectName("pushButton")
        bombo = self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        bombo.clicked.connect(self.Play_bombo)
        self.pushButton_2.setGeometry(QtCore.QRect(244, 330, 141, 131))
        self.pushButton_2.setObjectName("pushButton_2")
        chancha = self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        chancha.clicked.connect(self.Play_chancha)
        self.pushButton_3.setGeometry(QtCore.QRect(424, 300, 181, 111))
        self.pushButton_3.setObjectName("pushButton_3")
        tom_1 = self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        tom_1.clicked.connect(self.Play_tom_1)
        self.pushButton_4.setGeometry(QtCore.QRect(184, 110, 101, 101))
        self.pushButton_4.setObjectName("pushButton_4")
        tom_2 = self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        tom_2.clicked.connect(self.Play_tom_2)
        self.pushButton_5.setGeometry(QtCore.QRect(334, 100, 111, 111))
        self.pushButton_5.setObjectName("pushButton_5")
        ride = self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        ride.clicked.connect(self.Play_ride)
        self.pushButton_6.setGeometry(QtCore.QRect(484, 20, 121, 171))
        self.pushButton_6.setObjectName("pushButton_6")
        crash = self.pushButton_7 = QtWidgets.QPushButton(Dialog)
        crash.clicked.connect(self.Play_crash)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 30, 141, 121))
        self.pushButton_7.setObjectName("pushButton_7")
        hihat = self.pushButton_8 = QtWidgets.QPushButton(Dialog)
        hihat.clicked.connect(self.Play_hihat)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 180, 141, 101))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_4.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_6.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_7.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.pushButton_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bata"))
        self.pushButton.setText(_translate("Dialog", ""))
        self.pushButton_2.setText(_translate("Dialog", ""))
        self.pushButton_3.setText(_translate("Dialog", ""))
        self.pushButton_4.setText(_translate("Dialog", ""))
        self.pushButton_5.setText(_translate("Dialog", ""))
        self.pushButton_6.setText(_translate("Dialog", ""))
        self.pushButton_7.setText(_translate("Dialog", ""))
        self.pushButton_8.setText(_translate("Dialog", ""))
        
    def Play_redo(self): #Función que lanza el audio de cada objeto
        redoblante, fs = sf.read('Redoblante.wav')
        sd.play(redoblante)
        
        
    def Play_bombo(self):
        bombo, fs = sf.read('bombo.wav')
        sd.play(bombo)
        
    def Play_chancha(self):
        chancha, fs = sf.read('chancha.wav')
        sd.play(chancha)
        
    def Play_tom_1(self):
        tom_1, fs = sf.read('tom_1.wav')
        sd.play(tom_1)
    
    
    def Play_tom_2(self):
        tom_2, fs = sf.read('tom2.wav')
        sd.play(tom_2)
        
    
    def Play_hihat(self):
        hihat, fs = sf.read('hihat.wav')
        sd.play(hihat)
    
    
    def Play_crash(self):
        crash, fs = sf.read('crash.wav')
        sd.play(crash)
    
    
    def Play_ride(self):
        ride, fs = sf.read('ride.wav')
        sd.play(ride)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

