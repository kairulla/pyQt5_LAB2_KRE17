#!/usr/bin/env python3
# coding=utf-8

import sys

from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import math


# Основной класс программы
class Launcher(QDialog):
    def __init__(self):
        super(Launcher, self).__init__()
        loadUi('GUI.ui', self)  # Загрузка формы из файла

        # Задание заголовка окна
        self.setWindowTitle('Лабораторная 2 _ Python3 + PyQt5')
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)

        # Задание иконки окна
        self.setWindowIcon(QtGui.QIcon('res\\logo.png'))

        # Задание картинки с заданием с масштабированием в компоненте
        self.qLabelPicture.setPixmap(QPixmap('res\\primer17.png'))
        self.qLabelPicture.setScaledContents(True)

        # Привязываем к кнопкам наши процедуры-обработчики
        self.qPushButtonSolver.clicked.connect(self.solve)
        self.qPushButtonClear.clicked.connect(self.clear)
        self.qPushButtonExit.clicked.connect(self.close)

    # Процедура решения примера

    def solve(self):
        try:
            a = float(self.qLineEditA.text())
            b = float(self.qLineEditB.text())
            x = float(self.qLineEditX.text())
            if x > 6:
                y = (6 * x * x - a * b) / (2 * x * x)
            else:
                y = 4 * (x + a * a + b * b)

            if math.isnan(y):
                self.qLabelOtvet.setText("Нет решения")
            elif math.isinf(y):
                self.qLabelOtvet.setText("Бесконечность")
            else:
                self.qLabelOtvet.setText('Ответ: ' + str(format(y, '.2f')))
        except:
            self.qLabelOtvet.setText('Ошибка!')

    # Процедура очистки данных

    def clear(self):
        self.qLineEditA.setText('')
        self.qLineEditB.setText('')
        self.qLineEditX.setText('')
        self.qLabelOtvet.setText('Ответ: ')


if __name__ == '__main__':
    # Основная часть программы
    app = QApplication(sys.argv)
    window = Launcher()  # базовый класс окна
    window.show()  # отобразить окно на экране
    sys.exit(app.exec_())  # запуск основного цикла приложения
