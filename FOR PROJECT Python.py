# -*- coding: utf-8 -*-


from math import sqrt as sq
from PyQt5.QtGui import QPixmap
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Dialog1(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 322)
        Dialog.setStyleSheet("background-color: rgb(252, 228, 214);")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 100, 371, 101))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.textEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                                   "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><sty"
                                                   "le type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-"
                                                   "size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; marg"
                                                   "in-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:"
                                                   "0px;\">Данная программа направлена на создание файла, в который буд"
                                                   "ут записываться уравнения, для загрузки в систему Moodle. Пользоват"
                                                   "ель должен ввести коэффициенты уравнения общего вида, может задать "
                                                   "имя файла. Программа реагирует на действия пользователя, она может "
                                                   "выдавать предупреждение о неккоректно введеных данных. Картинка - и"
                                                   "ндикатор того, что уравнение добавлено в файл и базу данных.</p></b"
                                                   "ody></html>"))


class MyDialog1(QtWidgets.QDialog, Ui_Dialog1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class Ui_Dialog2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(502, 1072)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 501, 1061))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))


class MyDialog2(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self, file):
        super().__init__()
        self.setupUi(self)
        with open(file, 'rt') as f:
            read_data = f.read()
        self.textEdit.setHtml(_translate("Dialog", read_data))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(583, 556)
        MainWindow.setStyleSheet("background-color: rgb(252, 228, 214);\n"
"background-color: rgb(252, 240, 228);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.PB1 = QtWidgets.QPushButton(self.centralwidget)
        self.PB1.setGeometry(QtCore.QRect(260, 230, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PB1.setFont(font)
        self.PB1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.PB1.setStyleSheet("background-color: rgb(226, 228, 255);\n"
"color:rgb(0,0,0);")
        self.PB1.setObjectName("PB1")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 80, 131, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("border-bottom-color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 270, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 561, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(0, 112, 192);")
        self.label_3.setObjectName("label_3")
        self.PB2 = QtWidgets.QPushButton(self.centralwidget)
        self.PB2.setGeometry(QtCore.QRect(260, 410, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PB2.setFont(font)
        self.PB2.setStyleSheet("background-color: rgb(226, 228, 255);\n"
"color:rgb(0,0,0);")
        self.PB2.setObjectName("PB2")
        self.LE5 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE5.setGeometry(QtCore.QRect(110, 380, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LE5.setFont(font)
        self.LE5.setObjectName("LE5")
        self.LE4 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE4.setGeometry(QtCore.QRect(110, 310, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LE4.setFont(font)
        self.LE4.setObjectName("LE4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 350, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.PB3 = QtWidgets.QPushButton(self.centralwidget)
        self.PB3.setGeometry(QtCore.QRect(110, 460, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PB3.setFont(font)
        self.PB3.setStyleSheet("background-color: rgb(226, 228, 255);\n"
"color:rgb(0,0,0);")
        self.PB3.setObjectName("PB3")
        self.PB4 = QtWidgets.QPushButton(self.centralwidget)
        self.PB4.setGeometry(QtCore.QRect(320, 460, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PB4.setFont(font)
        self.PB4.setStyleSheet("background-color: rgb(226, 228, 255);\n"
"color:rgb(0,0,0);")
        self.PB4.setObjectName("PB4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 470, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.LE1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE1.setGeometry(QtCore.QRect(111, 117, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LE1.setFont(font)
        self.LE1.setStyleSheet("color:rgb(29, 46, 89);\n"
"background-color: rgb(193, 205, 234);")
        self.LE1.setObjectName("LE1")
        self.LE3 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE3.setGeometry(QtCore.QRect(111, 181, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LE3.setFont(font)
        self.LE3.setStyleSheet("color:rgb(29, 46, 89);\n"
"background-color: rgb(193, 205, 234);")
        self.LE3.setObjectName("LE3")
        self.LE2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE2.setGeometry(QtCore.QRect(111, 149, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.LE2.setFont(font)
        self.LE2.setStyleSheet("color:rgb(29, 46, 89);\n"
"background-color: rgb(193, 205, 234);")
        self.LE2.setObjectName("LE2")
        self.im = QtWidgets.QLabel(self.centralwidget)
        self.im.setGeometry(QtCore.QRect(400, 75, 47, 13))
        self.im.setObjectName("im")
        self.podick = QtWidgets.QLabel(self.centralwidget)
        self.podick.setGeometry(QtCore.QRect(373, 190, 133, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.podick.setFont(font)
        self.podick.setObjectName("podick")
        self.PB5 = QtWidgets.QPushButton(self.centralwidget)
        self.PB5.setGeometry(QtCore.QRect(20, 40, 151, 27))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PB5.setFont(font)
        self.PB5.setStyleSheet("background-color: rgb(226, 228, 255);")
        self.PB5.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 583, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PB1.setText(_translate("MainWindow", "Добавить в файл"))
        self.label.setText(_translate("MainWindow", "Задайте коэфициенты"))
        self.label_2.setText(_translate("MainWindow", "Вы добавили уравнение"))
        self.label_3.setText(_translate("MainWindow", "Составление квадратичного уравнения, нахождение его корней"))
        self.PB2.setText(_translate("MainWindow", "Задать имя файла"))
        self.LE5.setPlaceholderText(_translate("MainWindow", "project.txt"))
        self.LE4.setText(_translate("MainWindow", "Уравнение..."))
        self.label_4.setText(_translate("MainWindow", "Ввдети имя файла"))
        self.PB3.setText(_translate("MainWindow", "Просмотреть файл"))
        self.PB4.setText(_translate("MainWindow", "Просмотреть БД"))
        self.label_5.setText(_translate("MainWindow", "ИЛИ"))
        self.LE1.setPlaceholderText(_translate("MainWindow", "Коэффициент а"))
        self.LE3.setPlaceholderText(_translate("MainWindow", "Коэффициент c"))
        self.LE2.setPlaceholderText(_translate("MainWindow", "Коэффициент b"))
        self.podick.setText(_translate("MainWindow", "Уравнение добавлено"))
        self.PB5.setText(_translate("MainWindow", "О программе"))


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PB1.clicked.connect(self.makeyr)
        self.PB2.clicked.connect(self.prosm)
        self.PB3.clicked.connect(self.look)
        self.PB5.clicked.connect(self.proga)
        self.count = 0
        self.ques = ['Найдите произведение корней уравнения:',
                     'Найдите сумму корней уравнения:', 'Найдите максимальный корень уравнения:',
                     'Найдите минимальный корень уравнения:']
        self.yra = str()
        self.date = set()
        self.x1, self.x2 = float(), float()
        self.ak = str()
        self.bk = str()
        self.ck = str()
        self.nazv = str()
        self.dict = dict()
        self.flag = True
        self.pixmap = QPixmap('topchik1.jpg')
        self.im.resize(100, 100)
        self.im.setPixmap(self.pixmap)
        self.im.setVisible(False)
        self.podick.setVisible(False)

    def obr(self, x):
        if '.' in str(x):
            x = str(x).replace('.', ',')
            if x[x.index(',') + 1] == '0':
                x = x[:x.index(',')]
        return str(x)

    def proga(self):
        pass
        ex1 = MyDialog1()
        ex1.show()


    def korn(self):
        dis = float(self.bk) ** 2 - 4 * float(self.ak) * float(self.ck)
        if dis > 0:
            self.x1, self.x2 = (-float(self.bk) + sq(dis)) / (2 * float(self.ak)), (-float(self.bk) - sq(dis)) / (
                    2 * float(self.ak))
        elif dis == 0:
            self.x1, self.x2 = -float(self.bk) / (2 * float(self.ak)), -float(self.bk) / (2 * float(self.ak))
        else:
            error2 = QMessageBox()
            error2.setWindowTitle('Ошибка')
            error2.setText('Введены некорректные коэффициенты')
            error2.setIcon(QMessageBox.Warning)
            error2.setStandardButtons(QMessageBox.Ok)
            error2.setInformativeText('Введите коэффициенты, причем дискриминант должен быть положительным'
                                      ' или равен нулю.\nУравнение в файл не добавлено.')
            error2.exec_()
            self.LE1.setText("")
            self.LE2.setText("")
            self.LE3.setText("")
            self.LE4.setText("")

    def look(self):
        self.prosm()
        f = open(str(self.nazv), encoding="utf-8")
        look_ = QMessageBox()
        look_.setWindowTitle('Просмотр')
        look_.setText('Вы открыли файл ' + str(self.nazv))
        look_.setIcon(QMessageBox.Information)
        look_.setStandardButtons(QMessageBox.Ok)
        look_.setText(f.read())
        look_.exec_()
        f.close()

    def find_hcf(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def answ(self, a):
        if '.' in str(a):
            if len(a[a.index('.') + 1:]) > 2:
                return round(a, 2)
            elif len(a[a.index('.') + 1:]) == 1:
                return a
        return a


    def prosm(self):
        self.nazv = self.LE5.text()
        if self.nazv == '':
            self.nazv = "project.txt"

    def is_int(self, x):
        temp = str(x)
        i = 0
        while i < len(temp):
            if temp[i] == '.':
                while i + 1 < len(temp):
                    if temp[i + 1] != '0':
                        return False
                    i += 1
                else:
                    return True
            i += 1
        else:
            return True

    def makeyr(self):
        self.count += 1

        a = self.LE1.text()
        b = self.LE2.text()
        c = self.LE3.text()
        if a != '':
            self.im.setVisible(False)
            self.podick.setVisible(False)

        if a[0] == '-':
            aprov = a[1:]
        else:
            aprov = a[::]
        if b[0] == '-':
            bprov = b[1:]
        else:
            bprov = b[::]
        if c[0] == '-':
            cprov = c[1:]
        else:
            cprov = c[::]

        if not self.is_int(a) or a == '0' or not self.is_int(b) or b == '0' or not self.is_int(
                c) or c == '0' or not aprov.isdigit() or not bprov.isdigit() or not cprov.isdigit():
            error1 = QMessageBox()
            error1.setWindowTitle('Ошибка')
            error1.setText('Введены некорректные коэффициенты')
            error1.setIcon(QMessageBox.Warning)
            error1.setStandardButtons(QMessageBox.Ok)
            error1.setInformativeText('Необходимо ввести коэффициенты, причем они должны быть целыми и не рaвны нулю.\n'
                                      'Уравнение в файл не добавлено.')
            error1.exec_()
            self.LE1.setText("")
            self.LE2.setText("")
            self.LE3.setText("")
            self.LE4.setText("")



        else:
            self.ak = a
            self.bk = b
            self.ck = c

            if float(a) == 1:
                a = ''
            elif float(a) == -1:
                a = '-'
            if float(c) > 0:
                c = '+' + str(c)
            if float(b) != 0:
                if float(b) == 1:
                    b = ''
                elif float(b) == -1:
                    b = '-'
                self.yra = (self.obr(str(a)) + 'x' + '\u00B2' + '+' + self.obr(str(b)) + 'x' + self.obr(str(c)) + '=0').replace(
                    '+-', '-')

            self.LE4.setText(self.yra)
            self.LE1.setText("")
            self.LE2.setText("")
            self.LE3.setText("")

            if self.find_hcf(float(self.ak), float(self.bk)) == self.find_hcf(float(self.bk), float(self.ck)):
                akon = float(self.ak) // self.find_hcf(float(self.ak), float(self.bk))
                bkon = float(self.bk) // self.find_hcf(float(self.ak), float(self.bk))
                ckon = float(self.ck) // self.find_hcf(float(self.ak), float(self.bk))
            else:
                akon = float(self.ak)
                bkon = float(self.bk)
                ckon = float(self.ck)

            if float(akon) == 1:
                akon = ''
            elif float(akon) == -1:
                akon = '-'
            if float(ckon) > 0:
                ckon = '+' + str(ckon)
            if float(bkon) != 0:
                if float(bkon) == 1:
                    bkon = ''
                elif float(bkon) == -1:
                    bkon = '-'
                self.yra = (self.obr(str(akon)) + 'x' + '\u00B2' + '+' + self.obr(str(bkon)) + 'x' + self.obr(
                    str(ckon)) + '=0').replace('+-', '-').replace('++', '+')

            self.yra = (self.obr(str(akon)) + 'x' + '\u00B2' + '+' + self.obr(str(bkon)) + 'x' + self.obr(
                str(ckon)) + '=0').replace('+-', '-').replace('++', '+')

            if self.yra not in self.date:
                if self.flag:
                    pred = QMessageBox()
                    pred.setWindowTitle('Предупреждение')
                    pred.setText('Ответы представляют собой либо целое число, либо десятичную дробь.')
                    pred.setIcon(QMessageBox.Information)
                    pred.setStandardButtons(QMessageBox.Ok)
                    pred.exec_()
                    self.flag = False
                self.korn()
                self.prosm()
                self.date.add(self.yra)
                if self.nazv in self.dict.keys():
                    self.count = self.dict[self.nazv] + 1
                else:
                    self.dict[self.nazv] = 1
                    self.count = 1
                with open(str(self.nazv), 'a', encoding='utf-8') as f:
                    for i in range(4):
                        f.write(f'::{self.count}\n')
                        f.write('::При необходимости ответ округлите до сотых\n')
                        if i == 0:
                            otvet = self.obr(self.obr(str(self.x1 * self.x2)))
                            ot1 = otvet
                        elif i == 1:
                            otvet = self.obr(self.obr(str(self.x1 + self.x2)))
                            ot2 = otvet
                        elif i == 2:
                            otvet = self.obr(self.obr(str(max(self.x1, self.x2))))
                            ot3 = otvet
                        elif i == 3:
                            otvet = self.obr(self.obr(str(min(self.x1, self.x2))))
                            ot4 = otvet
                        f.write(f'::{self.ques[i]} {self.yra}\n')
                        f.write('{=' + f'{self.obr(str(otvet))}' + '}' + '\n')
                        f.write('\n')
                        self.count += 1
                    self.dict[self.nazv] = self.count - 1
                self.im.setVisible(True)
                self.podick.setVisible(True)

                # con = sqlite3.connect('DataBase.db')
                # cur = con.cursor()
                # cur.execute(f'INSERT INTO equation(id, yrav, summa, multiply, maxim, minim) VALUES({self.count}, {self.yra}, {ot1}, {ot2}, {ot3}, {ot4})')
                # con.commit()
                # con.close()

            else:
                pred1 = QMessageBox()
                pred1.setWindowTitle('Предупреждение')
                pred1.setText('Уравнение с подобными коэффициентами уже записано в файл и БД.')
                pred1.setIcon(QMessageBox.Information)
                pred1.setStandardButtons(QMessageBox.Ok)
                pred1.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())









































































