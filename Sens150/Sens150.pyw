# -*- coding: utf-8 -*-
import sys, time, socket

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

TCP_IP = "192.168.0.134"
TCP_PORT = 5000
BUFFER_SIZE = 256

class TCP_stream(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            send_dt = "dt\r\n"
            s.send(send_dt.encode())
            recv_dt = s.recv(BUFFER_SIZE).decode('cp1251')
            s.close()
            dead_time = int(recv_dt.split()[0])

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TCP_IP, TCP_PORT))
            send_data = "allsensors\r\n"
            s.send(send_data.encode())
            recv_data = s.recv(BUFFER_SIZE).decode()
            s.close()
            sens_lst = recv_data.split() 
            self.mainwindow.label_letters.setText(f'{sens_lst[0]}\t{sens_lst[1]}\t{sens_lst[2]}')
            self.mainwindow.label_dig_1.setText(f'{sens_lst[4]}  \N{DEGREE SIGN}C')
            self.mainwindow.label_dig_2.setText(f'{sens_lst[6]}  \N{DEGREE SIGN}C')
            self.mainwindow.label_dig_3.setText(f'{sens_lst[8]}  \N{DEGREE SIGN}C')
            self.mainwindow.label_dig_4.setText(f'{sens_lst[10]}  \N{DEGREE SIGN}C')
            time.sleep(dead_time)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Picture = QtWidgets.QGraphicsView(self.centralwidget)
        self.Picture.setGeometry(QtCore.QRect(80, 100, 431, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Picture.setFont(font)
        self.Picture.setStyleSheet("border-image: url(sens150bg.bin);")
        self.Picture.setObjectName("Picture")
        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(250, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_letters = QtWidgets.QLabel(self.centralwidget)
        self.label_letters.setGeometry(QtCore.QRect(3, 0, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_letters.setFont(font)
        self.label_letters.setObjectName("label_letters")
        self.label_read = QtWidgets.QLabel(self.centralwidget)
        self.label_read.setGeometry(QtCore.QRect(3, 20, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_read.setFont(font)
        self.label_read.setObjectName("label_read")
        self.label_stop = QtWidgets.QLabel(self.centralwidget)
        self.label_stop.setGeometry(QtCore.QRect(3, 20, 300, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_stop.setFont(font)
        self.label_stop.setObjectName("label_stop")
        self.label_sensor_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor_1.setGeometry(QtCore.QRect(190, 130, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sensor_1.setFont(font)
        self.label_sensor_1.setObjectName("label_sensor_1")
        self.label_sensor_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor_2.setGeometry(QtCore.QRect(190, 230, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sensor_2.setFont(font)
        self.label_sensor_2.setObjectName("label_sensor_2")
        self.label_sensor_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor_3.setGeometry(QtCore.QRect(380, 130, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sensor_3.setFont(font)
        self.label_sensor_3.setObjectName("label_sensor_3")
        self.label_sensor_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_sensor_4.setGeometry(QtCore.QRect(380, 230, 80, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_sensor_4.setFont(font)
        self.label_sensor_4.setObjectName("label_sensor_4")
        self.label_dig_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_dig_3.setGeometry(QtCore.QRect(335, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dig_3.setFont(font)
        self.label_dig_3.setObjectName("label_dig_3")
        self.label_dig_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_dig_1.setGeometry(QtCore.QRect(145, 110, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dig_1.setFont(font)
        self.label_dig_1.setObjectName("label_dig_1")
        self.label_dig_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_dig_4.setGeometry(QtCore.QRect(335, 210, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dig_4.setFont(font)
        self.label_dig_4.setObjectName("label_dig_4")
        self.label_dig_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_dig_2.setGeometry(QtCore.QRect(145, 210, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_dig_2.setFont(font)
        self.label_dig_2.setObjectName("label_dig_2")
        self.label_temp_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_2.setGeometry(QtCore.QRect(110, 260, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_temp_2.setFont(font)
        self.label_temp_2.setObjectName("label_temp_2")
        self.label_temp_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_1.setGeometry(QtCore.QRect(110, 160, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_temp_1.setFont(font)
        self.label_temp_1.setObjectName("label_temp_1")
        self.label_temp_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_4.setGeometry(QtCore.QRect(300, 260, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_temp_4.setFont(font)
        self.label_temp_4.setObjectName("label_temp_4")
        self.label_temp_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_temp_3.setGeometry(QtCore.QRect(300, 160, 110, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_temp_3.setFont(font)
        self.label_temp_3.setObjectName("label_temp_3")
        self.button_launch = QtWidgets.QPushButton(self.centralwidget)
        self.button_launch.setGeometry(QtCore.QRect(200, 320, 93, 28))
        self.button_launch.setObjectName("button_launch")
        self.button_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_stop.setGeometry(QtCore.QRect(310, 320, 93, 28))
        self.button_stop.setObjectName("button_stop")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button_launch.clicked.connect(self.launch_tcp_stream)
        self.button_stop.clicked.connect(self.stop_tcp_stream)
        self.TCPstream_Thread_instance = TCP_stream(mainwindow=self)

    def launch_tcp_stream(self):
        self.TCPstream_Thread_instance.start()
        self.label_stop.setText(f'')
        self.label_read.setText(f'Идет чтение...')

    def stop_tcp_stream(self):
        self.TCPstream_Thread_instance.terminate()
        self.label_letters.setText(f'Нет связи')
        self.label_read.setText(f'')
        self.label_stop.setText(f'Чтение остановлено')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ВК-150"))
        self.label_name.setText(_translate("MainWindow", "Камера"))
        self.label_letters.setText(_translate("MainWindow", "Нет связи"))
        self.label_sensor_1.setText(_translate("MainWindow", "Датчик 1"))
        self.label_sensor_2.setText(_translate("MainWindow", "Датчик 2"))
        self.label_sensor_3.setText(_translate("MainWindow", "Датчик 3"))
        self.label_sensor_4.setText(_translate("MainWindow", "Датчик 4"))
        self.label_dig_3.setText(_translate("MainWindow", "0"))
        self.label_dig_1.setText(_translate("MainWindow", "0"))
        self.label_dig_4.setText(_translate("MainWindow", "0"))
        self.label_dig_2.setText(_translate("MainWindow", "0"))
        self.label_temp_2.setText(_translate("MainWindow", "Температура"))
        self.label_temp_1.setText(_translate("MainWindow", "Температура"))
        self.label_temp_4.setText(_translate("MainWindow", "Температура"))
        self.label_temp_3.setText(_translate("MainWindow", "Температура"))
        self.button_launch.setText(_translate("MainWindow", "Старт"))
        self.button_stop.setText(_translate("MainWindow", "Стоп"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
