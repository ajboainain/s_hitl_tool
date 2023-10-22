# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\hitl.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import threading
import serial.tools.list_ports
from pymavlink import mavutil

channels = [
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
]


class Server(QtCore.QObject):

    def __init__(self, PORT=9078):
        self.fc_connection = None
        self.HOST = '127.0.0.1'
        self.PORT = PORT
        self.mav = mavutil.mavlink_connection('udp:localhost:' + str(self.PORT))
        
        self.recievingData = False
        self.recievedData = None


        self.receive_data_thread = threading.Thread(target=self.recieve_data)

        # self.s.setblocking(0)
        # print("Starting a server")
        # print("IP: " + str(self.HOST))
        # print("Port: " + str(self.PORT))

    def start_recieving(self):
        self.recievingData = True
        self.recievedData = None
        self.receive_data_thread.start()

    def stop_recieving(self):
        self.recievingData = False
        self.mav.close()

    def recieve_data(self):
        self.recievingData = True
        
        while self.recievingData:
            msg = self.mav.recv_match(type="SERVO_OUTPUT_RAW", blocking=True)
            channels_in = []
            if  msg:
                for i in range(12):
                    channels_in.append(msg.to_dict()['servo'+str(i+1)+'_raw'])
                # print(channels_in)
            try:
                global channels
                channels = channels_in
                self.receivedData = channels_in
            except:
                self.recievedData = None
        

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setWindowFlags(
            QtCore.Qt.Window |
            QtCore.Qt.CustomizeWindowHint |
            QtCore.Qt.WindowTitleHint |
            QtCore.Qt.WindowMinimizeButtonHint
        )
        self.fc_connection = None
        self.pwm_bars = []
        self.server = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(540, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(540, 450))
        MainWindow.setMaximumSize(QtCore.QSize(540, 450))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/sahab.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_menus = QtWidgets.QFrame(self.centralwidget)
        self.frame_menus.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_menus.setObjectName("frame_menus")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_menus)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_server_menu = QtWidgets.QFrame(self.frame_menus)
        self.frame_server_menu.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_server_menu.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_server_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_server_menu.setObjectName("frame_server_menu")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_server_menu)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_server = QtWidgets.QLabel(self.frame_server_menu)
        self.label_server.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_server.setAlignment(QtCore.Qt.AlignCenter)
        self.label_server.setObjectName("label_server")
        self.verticalLayout_4.addWidget(self.label_server)
        self.frame_8 = QtWidgets.QFrame(self.frame_server_menu)
        self.frame_8.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_port = QtWidgets.QLabel(self.frame_8)
        self.label_port.setObjectName("label_port")
        self.horizontalLayout_4.addWidget(self.label_port)
        self.lineEdit_port = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_port.setMaximumSize(QtCore.QSize(60, 16777215))
        self.lineEdit_port.setMaxLength(8)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_4.addWidget(self.lineEdit_port)
        self.pushButton_start_server = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_start_server.setObjectName("pushButton_start_server")
        self.horizontalLayout_4.addWidget(self.pushButton_start_server)
        self.verticalLayout_4.addWidget(self.frame_8)
        self.frame_3 = QtWidgets.QFrame(self.frame_server_menu)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_server_status = QtWidgets.QLabel(self.frame_3)
        self.label_server_status.setObjectName("label_server_status")
        self.horizontalLayout_5.addWidget(self.label_server_status)
        self.label_current_server_status = QtWidgets.QLabel(self.frame_3)
        self.label_current_server_status.setFrameShape(QtWidgets.QFrame.Box)
        self.label_current_server_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_server_status.setObjectName("label_current_server_status")
        self.horizontalLayout_5.addWidget(self.label_current_server_status)
        self.verticalLayout_4.addWidget(self.frame_3)
        self.horizontalLayout_3.addWidget(self.frame_server_menu)
        self.frame_fc_menu = QtWidgets.QFrame(self.frame_menus)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_fc_menu.sizePolicy().hasHeightForWidth())
        self.frame_fc_menu.setSizePolicy(sizePolicy)
        self.frame_fc_menu.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_fc_menu.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_fc_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_fc_menu.setObjectName("frame_fc_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_fc_menu)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_fc = QtWidgets.QLabel(self.frame_fc_menu)
        self.label_fc.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_fc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fc.setObjectName("label_fc")
        self.verticalLayout_3.addWidget(self.label_fc)
        self.frame_6 = QtWidgets.QFrame(self.frame_fc_menu)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_com = QtWidgets.QLabel(self.frame_6)
        self.label_com.setMaximumSize(QtCore.QSize(25, 16777215))
        self.label_com.setObjectName("label_com")
        self.horizontalLayout.addWidget(self.label_com)
        self.comboBox_com = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_com.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox_com.setObjectName("comboBox_com")
        self.comboBox_com.addItem("")
        self.comboBox_com.addItem("")
        self.comboBox_com.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_com)
        self.pushButton_com_refresh = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_com_refresh.setMaximumSize(QtCore.QSize(24, 24))
        self.pushButton_com_refresh.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/reload2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_com_refresh.setIcon(icon1)
        self.pushButton_com_refresh.setObjectName("pushButton_com_refresh")
        self.horizontalLayout.addWidget(self.pushButton_com_refresh)
        self.pushButton_com_connect = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_com_connect.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_com_connect.setObjectName("pushButton_com_connect")
        self.horizontalLayout.addWidget(self.pushButton_com_connect)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.frame_fc_menu)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_fc_status = QtWidgets.QLabel(self.frame_4)
        self.label_fc_status.setObjectName("label_fc_status")
        self.horizontalLayout_6.addWidget(self.label_fc_status)
        self.label_current_fc_status = QtWidgets.QLabel(self.frame_4)
        self.label_current_fc_status.setFrameShape(QtWidgets.QFrame.Box)
        self.label_current_fc_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_fc_status.setObjectName("label_current_fc_status")
        self.horizontalLayout_6.addWidget(self.label_current_fc_status)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout_3.addWidget(self.frame_fc_menu)
        self.verticalLayout.addWidget(self.frame_menus)
        self.frame_channels = QtWidgets.QFrame(self.centralwidget)
        self.frame_channels.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_channels.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_channels.setObjectName("frame_channels")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_channels)
        self.gridLayout.setObjectName("gridLayout")
        self.bar_ch2 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch2.setProperty("value", 0)
        self.bar_ch2.setFormat("%v")
        self.bar_ch2.setObjectName("bar_ch2")
        self.gridLayout.addWidget(self.bar_ch2, 1, 1, 1, 1)
        self.label_ch2 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch2.setObjectName("label_ch2")
        self.gridLayout.addWidget(self.label_ch2, 1, 0, 1, 1)
        self.label_ch4 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch4.setObjectName("label_ch4")
        self.gridLayout.addWidget(self.label_ch4, 3, 0, 1, 1)
        self.label_ch6 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch6.setObjectName("label_ch6")
        self.gridLayout.addWidget(self.label_ch6, 5, 0, 1, 1)
        self.bar_ch10 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch10.setProperty("value", 0)
        self.bar_ch10.setFormat("%v")
        self.bar_ch10.setObjectName("bar_ch10")
        self.gridLayout.addWidget(self.bar_ch10, 3, 3, 1, 1)
        self.bar_ch3 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch3.setProperty("value", 0)
        self.bar_ch3.setFormat("%v")
        self.bar_ch3.setObjectName("bar_ch3")
        self.gridLayout.addWidget(self.bar_ch3, 2, 1, 1, 1)
        self.bar_ch11 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch11.setProperty("value", 0)
        self.bar_ch11.setFormat("%v")
        self.bar_ch11.setObjectName("bar_ch11")
        self.gridLayout.addWidget(self.bar_ch11, 4, 3, 1, 1)
        self.label_ch9 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch9.setObjectName("label_ch9")
        self.gridLayout.addWidget(self.label_ch9, 2, 2, 1, 1)
        self.label_ch12 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch12.setObjectName("label_ch12")
        self.gridLayout.addWidget(self.label_ch12, 5, 2, 1, 1)
        self.bar_ch4 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch4.setProperty("value", 0)
        self.bar_ch4.setFormat("%v")
        self.bar_ch4.setObjectName("bar_ch4")
        self.gridLayout.addWidget(self.bar_ch4, 3, 1, 1, 1)
        self.bar_ch9 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch9.setProperty("value", 0)
        self.bar_ch9.setFormat("%v")
        self.bar_ch9.setObjectName("bar_ch9")
        self.gridLayout.addWidget(self.bar_ch9, 2, 3, 1, 1)
        self.label_ch8 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch8.setObjectName("label_ch8")
        self.gridLayout.addWidget(self.label_ch8, 1, 2, 1, 1)
        self.label_ch10 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch10.setObjectName("label_ch10")
        self.gridLayout.addWidget(self.label_ch10, 3, 2, 1, 1)
        self.label_ch1 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch1.setObjectName("label_ch1")
        self.gridLayout.addWidget(self.label_ch1, 0, 0, 1, 1)
        self.bar_ch7 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch7.setProperty("value", 0)
        self.bar_ch7.setFormat("%v")
        self.bar_ch7.setObjectName("bar_ch7")
        self.gridLayout.addWidget(self.bar_ch7, 0, 3, 1, 1)
        self.label_ch5 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch5.setObjectName("label_ch5")
        self.gridLayout.addWidget(self.label_ch5, 4, 0, 1, 1)
        self.bar_ch8 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch8.setProperty("value", 0)
        self.bar_ch8.setFormat("%v")
        self.bar_ch8.setObjectName("bar_ch8")
        self.gridLayout.addWidget(self.bar_ch8, 1, 3, 1, 1)
        self.label_ch11 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch11.setObjectName("label_ch11")
        self.gridLayout.addWidget(self.label_ch11, 4, 2, 1, 1)
        self.bar_ch1 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch1.setProperty("value", 0)
        self.bar_ch1.setFormat("%v")
        self.bar_ch1.setObjectName("bar_ch1")
        self.gridLayout.addWidget(self.bar_ch1, 0, 1, 1, 1)
        self.bar_ch5 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch5.setProperty("value", 0)
        self.bar_ch5.setFormat("%v")
        self.bar_ch5.setObjectName("bar_ch5")
        self.gridLayout.addWidget(self.bar_ch5, 4, 1, 1, 1)
        self.bar_ch6 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch6.setProperty("value", 0)
        self.bar_ch6.setFormat("%v")
        self.bar_ch6.setObjectName("bar_ch6")
        self.gridLayout.addWidget(self.bar_ch6, 5, 1, 1, 1)
        self.label_ch3 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch3.setObjectName("label_ch3")
        self.gridLayout.addWidget(self.label_ch3, 2, 0, 1, 1)
        self.label_ch7 = QtWidgets.QLabel(self.frame_channels)
        self.label_ch7.setObjectName("label_ch7")
        self.gridLayout.addWidget(self.label_ch7, 0, 2, 1, 1)
        self.bar_ch12 = QtWidgets.QProgressBar(self.frame_channels)
        self.bar_ch12.setProperty("value", 0)
        self.bar_ch12.setFormat("%v")
        self.bar_ch12.setObjectName("bar_ch12")
        self.gridLayout.addWidget(self.bar_ch12, 5, 3, 1, 1)
        self.verticalLayout.addWidget(self.frame_channels)
        self.frame_quit = QtWidgets.QFrame(self.centralwidget)
        self.frame_quit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_quit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_quit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_quit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_quit.setObjectName("frame_quit")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_quit)
        self.horizontalLayout_2.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_quit = QtWidgets.QPushButton(self.frame_quit)
        self.pushButton_quit.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButton_quit.setObjectName("pushButton_quit")
        self.horizontalLayout_2.addWidget(self.pushButton_quit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_quit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.running = True

        self.pwm_bars.append(self.bar_ch1)
        self.pwm_bars.append(self.bar_ch2)
        self.pwm_bars.append(self.bar_ch3)
        self.pwm_bars.append(self.bar_ch4)
        self.pwm_bars.append(self.bar_ch5)
        self.pwm_bars.append(self.bar_ch6)
        self.pwm_bars.append(self.bar_ch7)
        self.pwm_bars.append(self.bar_ch8)
        self.pwm_bars.append(self.bar_ch9)
        self.pwm_bars.append(self.bar_ch10)
        self.pwm_bars.append(self.bar_ch11)
        self.pwm_bars.append(self.bar_ch12)
        for pwm_bar in self.pwm_bars:
            pwm_bar.setMinimum(1100)
            pwm_bar.setMaximum(1900)
            pwm_bar.setValue(1100)

        self.update_com_ports_combobox()
        self.retranslateUi(MainWindow)
        self.pushButton_com_refresh.clicked.connect(self.update_com_ports_combobox) # type: ignore
        self.pushButton_start_server.clicked.connect(self.handle_stop_start_server) # type: ignore
        self.pushButton_com_connect.clicked.connect(self.handle_fc_connection) # type: ignore
        self.pushButton_quit.clicked.connect(self.close_application) # type: ignore

        # self.timer = QtCore.QTimer()
        # self.timer.setInterval(30)
        # self.timer.timeout.connect(self.update_channels)
        # self.timer.start()

        self.update_channels_thread = threading.Thread(target=self.update_channels)
        self.update_channels_thread.start()

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def update_channels(self):
        global channels
        while self.running:
            for i, bar in enumerate(self.pwm_bars):
                pwm = int(channels[i])
                if pwm == 0:
                    pwm = 1100
                    channels[i] = 1100
                    # if self.fc_connection is not None:
                    #     self.fc_connection.set_servo(i+1, pwm)
                bar.setValue(pwm)
                # print("set bar ", i, "to", pwm)
            if self.fc_connection is not None:
                # channels2 = [int(x) for x in channels]
                self.fc_connection.mav.rc_channels_override_send(
                    self.fc_connection.target_system,
                    self.fc_connection.target_component,
                    *channels
                )
            
    def handle_stop_start_server(self):
        if self.lineEdit_port.text() == "":
            return

        if self.pushButton_start_server.text() == "Start":
            try:
                self.server = Server(int(self.lineEdit_port.text()))
                self.server.start_recieving()
                self.label_current_server_status.setText("Operational")
                self.label_current_server_status.setStyleSheet("background-color: green")
                self.pushButton_start_server.setText("Stop")
            except Exception as error:
                self.label_current_fc_status.setStyleSheet("background-color: red")
                self.label_current_fc_status.setText("Failed")
                dlg = QtWidgets.QMessageBox()
                dlg.setIcon(QtWidgets.QMessageBox.Critical)
                dlg.setWindowTitle("Error")
                dlg.setText("Unable to connect to start server. Please try again.")
                dlg.setDetailedText(str(error))
                dlg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                dlg.exec_()

        else:
            try:
                self.server.stop_recieving()
                self.server = None
                self.label_current_server_status.setText("Not Started")
                self.label_current_server_status.setStyleSheet("")
                self.pushButton_start_server.setText("Start")
                print("Stopped server")
            except:
                pass

    def handle_fc_connection(self):

        if self.comboBox_com.count() == 0:
            return
        if self.pushButton_com_connect.text() == "Disconnect":
            self.fc_connection.close()
            self.fc_connection = None
            self.pushButton_com_connect.setText("Connect")
            self.label_current_fc_status.setStyleSheet("")
            self.label_current_fc_status.setText("Not Connected")
            return
        try:
            self.fc_connection = mavutil.mavlink_connection(
                self.comboBox_com.currentText())

            # TODO Make this application more robust by achieving the following:
            # 1) If not armed, arm the plane.
            # 2) If not on MANUAL mode, switch to MANUAL mode
            # 3) If RC channels 1-12 are not RC-PASSTHROUGH, make them RC-PASSTHROUGH
            # 4) Nice to have: Reset back to original settings before closing
            # Will need a better understanding of this mavutil library


            connected = self.fc_connection.wait_heartbeat(timeout=5)
            if connected is None:
                raise Exception("Could not connect on this COM port.")

            # arm the plane
            # self.fc_connection.mav.command_long_send(
            #     self.fc_connection.target_system,
            #     self.fc_connection.target_component,
            #     mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
            #     0,
            #     1, 0, 0, 0, 0, 0, 0
            # )

            # if self.fc_connection.recv_match(timeout=5000) is None:
            #     raise Exception("Could not arm the flight controller.")

            # self.fc_connection.motors_armed_wait()

            # Get mode ID
            # mode_id = self.fc_connection.mode_mapping()["MANUAL"]
            # # Set mode to manual
            # self.fc_connection.mav.set_mode_send(
            #     self.fc_connection.target_system,
            #     mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED,
            #     mode_id
            # )
            # Find a better non-blocking way to do this. Separate thread?
            # while True:
            #     # Wait for ACK command
            #     # Would be good to add mechanism to avoid endlessly blocking
            #     # if the autopilot sends a NACK or never receives the message
            #     ack_msg = self.fc_connection.recv_match(type='COMMAND_ACK', blocking=True)
            #     ack_msg = ack_msg.to_dict()

            #     # Continue waiting if the acknowledged command is not `set_mode`
            #     if ack_msg['command'] != mavutil.mavlink.MAV_CMD_DO_SET_MODE:
            #         continue

            #     # Print the ACK result !
            #     print(mavutil.mavlink.enums['MAV_RESULT'][ack_msg['result']].description)
            #     print("Set to manual mode")
            #     break
            self.label_current_fc_status.setStyleSheet("background-color: green")
            self.label_current_fc_status.setText("Connected")
            self.pushButton_com_connect.setText("Disconnect")

        except Exception as error:
            self.label_current_fc_status.setStyleSheet("background-color: red")
            self.label_current_fc_status.setText("Failed")
            self.fc_connection = None
            dlg = QtWidgets.QMessageBox()
            dlg.setIcon(QtWidgets.QMessageBox.Critical)
            dlg.setWindowTitle("Error")
            dlg.setText("Unable to connect to flight controller. Please try again.")
            dlg.setDetailedText(str(error))
            dlg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            dlg.exec_()


    def close_application(self):
        self.running = False
        if (self.server is not None):
            self.server.stop_recieving()
            self.server.kill_server()
            self.server = None
        if self.fc_connection is not None:
            self.fc_connection.close()
            self.fc_connection = None
        self.update_channels_thread.join()

        QtCore.QCoreApplication.quit()

    def update_com_ports_combobox(self):
        ports = serial.tools.list_ports.comports()
        self.comboBox_com.clear()
        cube_index = None
        for index, port in enumerate(ports):
            self.comboBox_com.addItem(port.name)
            if ("cube" in port.description.lower()):
                cube_index = index
        if cube_index is not None:
            self.comboBox_com.setCurrentIndex(cube_index)
        return

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Al-Suhaab HITL Tool"))
        self.label_server.setText(_translate("MainWindow", "Server"))
        self.label_port.setText(_translate("MainWindow", "PORT"))
        self.lineEdit_port.setText(_translate("MainWindow", "5052"))
        self.lineEdit_port.setPlaceholderText(_translate("MainWindow", ""))
        self.pushButton_start_server.setText(_translate("MainWindow", "Start"))
        self.label_server_status.setText(_translate("MainWindow", "Server Status:"))
        self.label_current_server_status.setText(_translate("MainWindow", "Not Started"))
        self.label_fc.setText(_translate("MainWindow", "Flight Controller"))
        self.label_com.setText(_translate("MainWindow", "FC"))
        self.pushButton_com_connect.setText(_translate("MainWindow", "Connect"))
        self.label_fc_status.setText(_translate("MainWindow", "FC Status:"))
        self.label_current_fc_status.setText(_translate("MainWindow", "Not Connected"))
        self.label_ch2.setText(_translate("MainWindow", "Channel 2"))
        self.label_ch4.setText(_translate("MainWindow", "Channel 4"))
        self.label_ch6.setText(_translate("MainWindow", "Channel 6"))
        self.label_ch9.setText(_translate("MainWindow", "Channel 9"))
        self.label_ch12.setText(_translate("MainWindow", "Channel 12"))
        self.label_ch8.setText(_translate("MainWindow", "Channel 8"))
        self.label_ch10.setText(_translate("MainWindow", "Channel 10"))
        self.label_ch1.setText(_translate("MainWindow", "Channel 1"))
        self.label_ch5.setText(_translate("MainWindow", "Channel 5"))
        self.label_ch11.setText(_translate("MainWindow", "Channel 11"))
        self.label_ch3.setText(_translate("MainWindow", "Channel 3"))
        self.label_ch7.setText(_translate("MainWindow", "Channel 7"))
        self.pushButton_quit.setText(_translate("MainWindow", "Quit"))



import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
