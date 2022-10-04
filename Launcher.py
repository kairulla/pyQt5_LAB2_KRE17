#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.uic import loadUi
import math


# Основной класс программы
class Launcher(QWidget):
    def __init__(self):
        super(Launcher, self).__init__()
        loadUi('GUI.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Лабораторная 2 _ Python3 + PyQt5')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('_MY_PICTURES//logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.qLabelPicture.setPixmap(QPixmap('_MY_PICTURES//primer17.png'))
        self.qLabelPicture.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.qPushButtonSolver.clicked.connect(self.qPushButtonSolverOnClick)
        self.qPushButtonClear.clicked.connect(self.qPushButtonClearOnClick)
        self.qPushButtonExit.clicked.connect(self.close)
        self.qLineEditA.textChanged.connect(lambda text, obj=self.qLineEditA: self.qLineEditA_textChangedEvent(text))
        self.qLineEditB.textChanged.connect(lambda text, obj=self.qLineEditB: self.qLineEditB_textChangedEvent(text))
        self.qLineEditX.textChanged.connect(lambda text, obj=self.qLineEditX: self.qLineEditX_textChangedEvent(text))

    # Процедура решения примера

    def qPushButtonSolverOnClick(self):
        self.qLabelOtvet.setStyleSheet("color: rgb(0, 0, 255)")
        try:
            a = float(self.qLineEditA.text())
            b = float(self.qLineEditB.text())
            x = float(self.qLineEditX.text())
            if x > 6:
                y = (6 * x * x - a * b) / (2 * x * x)
            else:
                y = 4 * (x + a * a + b * b)

            if math.isnan(y):
                self.qLabelOtvet.setStyleSheet("color: rgb(255, 0, 0)")
                self.qLabelOtvet.setText("Нет решения")
            elif math.isinf(y):
                self.qLabelOtvet.setStyleSheet("color: rgb(255, 0, 0)")
                self.qLabelOtvet.setText("Бесконечность")
            else:
                self.qLabelOtvet.setText('Ответ: ' + str(format(y, '.2f')))
        except:
            self.qLabelOtvet.setStyleSheet("color: rgb(255, 0, 0)")
            self.qLabelOtvet.setText('Ошибка!')



    # Процедура очистки данных

    def qPushButtonClearOnClick(self):
        self.qLineEditA.setText('')
        self.qLineEditA.setStyleSheet('border: 1px solid gray;'
                                      'border-radius: 5px;')
        self.qLineEditB.setText('')
        self.qLineEditB.setStyleSheet('border: 1px solid gray;'
                                      'border-radius: 5px;')
        self.qLineEditX.setText('')
        self.qLineEditX.setStyleSheet('border: 1px solid gray;'
                                      'border-radius: 5px;')
        self.qLabelOtvet.setText('Ответ = ')
        self.qLabelOtvet.setStyleSheet('')

    # Установка окраски рамки у компонента в зависимости от значения в нем
    def setBorderColor(self, objectName, currentValue):
        try:
            float(currentValue)
            objectName.setStyleSheet("border: 3px solid rgb(0, 255, 0);"
                                     "border-radius: 5px;")
        except:
            objectName.setStyleSheet("border: 3px solid rgb(255, 0, 0);"
                                     "border-radius: 5px;")

    def qLineEditA_textChangedEvent(self, text):
        self.setBorderColor(self.qLineEditA, text)


    def qLineEditB_textChangedEvent(self, text):
        self.setBorderColor(self.qLineEditB, text)


    def qLineEditX_textChangedEvent(self, text):
        self.setBorderColor(self.qLineEditX, text)





if __name__ == '__main__':
    # Основная часть программы
    app = QApplication(sys.argv)
    window = Launcher()  # базовый класс окна
    window.show()  # отобразить окно на экране
    sys.exit(app.exec_())  # запуск основного цикла приложения
