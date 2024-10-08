# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QAxContainer
import requests
import subprocess

import binascii  # hex encoding
import hashlib
import json as jsond  # json
import os
import platform  # check platform
import subprocess  # needed for mac device
import sys
import time  # sleep before exit
from datetime import datetime
from time import sleep
from uuid import uuid4  # gen random guid
import keyauth
from keyauth import *
import hashlib
from hashlib import *
from PyQt5 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets
from keyauth import keyauth



getchecksum = lambda: hashlib.sha256(open(sys.argv[0], 'rb').read()).hexdigest()

name = "DiamondSorter"
ownerid = "VwOq0EhmEw"
secret = "795e63c4dd27cbb04b9af01befb8eae95625e51115356cbbd767196900409066"
version = "1.9"
hash_to_check = getchecksum()
keyauthapp = keyauth.api(name =name,
                        ownerid =ownerid,
                        secret =secret,
                        version =version,
                        hash_to_check=hash_to_check)
print(keyauthapp)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1027, 610)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-60, -80, 991, 681))
        self.widget.setStyleSheet("QPushButton#pushButton{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.backdrop_holder_label = QtWidgets.QLabel(self.widget)
        self.backdrop_holder_label.setGeometry(QtCore.QRect(100, 210, 531, 481))
        self.backdrop_holder_label.setStyleSheet("border-image: url(:/images/background.gif);\n"
"border-top-left-radius: 50px;")
        self.backdrop_holder_label.setText("")
        self.backdrop_holder_label.setObjectName("backdrop_holder_label")
        self.backdrop_holder = QtWidgets.QLabel(self.widget)
        self.backdrop_holder.setGeometry(QtCore.QRect(100, 70, 531, 611))
        self.backdrop_holder.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px;")
        self.backdrop_holder.setText("")
        self.backdrop_holder.setObjectName("backdrop_holder")
        self.program_backdrop = QtWidgets.QLabel(self.widget)
        self.program_backdrop.setGeometry(QtCore.QRect(110, 80, 521, 130))
        self.program_backdrop.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.program_backdrop.setText("")
        self.program_backdrop.setObjectName("program_backdrop")
        self.program_title = QtWidgets.QLabel(self.widget)
        self.program_title.setGeometry(QtCore.QRect(380, 90, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.program_title.setFont(font)
        self.program_title.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.program_title.setObjectName("program_title")
        self.program_description = QtWidgets.QLabel(self.widget)
        self.program_description.setGeometry(QtCore.QRect(119, 140, 241, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.program_description.setFont(font)
        self.program_description.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.program_description.setObjectName("program_description")
        self.system_updates = QtWidgets.QFrame(self.widget)
        self.system_updates.setGeometry(QtCore.QRect(110, 220, 511, 381))
        self.system_updates.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.system_updates.setFrameShadow(QtWidgets.QFrame.Raised)
        self.system_updates.setObjectName("system_updates")
        self.updates_label = QtWidgets.QLabel(self.system_updates)
        self.updates_label.setGeometry(QtCore.QRect(200, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("HACKED")
        font.setPointSize(22)
        self.updates_label.setFont(font)
        self.updates_label.setObjectName("updates_label")
        self.update_1_label = QtWidgets.QLabel(self.system_updates)
        self.update_1_label.setGeometry(QtCore.QRect(10, 60, 241, 91))
        self.update_1_label.setObjectName("update_1_label")
        self.update_2_label = QtWidgets.QLabel(self.system_updates)
        self.update_2_label.setGeometry(QtCore.QRect(10, 140, 241, 91))
        self.update_2_label.setObjectName("update_2_label")
        self.update_3_label = QtWidgets.QLabel(self.system_updates)
        self.update_3_label.setGeometry(QtCore.QRect(10, 230, 241, 91))
        self.update_3_label.setObjectName("update_3_label")
        self.update_1_label_2 = QtWidgets.QLabel(self.system_updates)
        self.update_1_label_2.setGeometry(QtCore.QRect(270, 60, 241, 91))
        self.update_1_label_2.setObjectName("update_1_label_2")
        self.update_1_label_3 = QtWidgets.QLabel(self.system_updates)
        self.update_1_label_3.setGeometry(QtCore.QRect(260, 150, 241, 91))
        self.update_1_label_3.setObjectName("update_1_label_3")
        self.update_1_label_4 = QtWidgets.QLabel(self.system_updates)
        self.update_1_label_4.setGeometry(QtCore.QRect(270, 250, 241, 91))
        self.update_1_label_4.setObjectName("update_1_label_4")
        self.program_stats_frame = QtWidgets.QFrame(self.widget)
        self.program_stats_frame.setGeometry(QtCore.QRect(110, 620, 511, 51))
        self.program_stats_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.program_stats_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.program_stats_frame.setObjectName("program_stats_frame")
        self.login_tab_widget = QtWidgets.QTabWidget(Form)
        self.login_tab_widget.setGeometry(QtCore.QRect(570, 0, 451, 611))
        self.login_tab_widget.setTabPosition(QtWidgets.QTabWidget.East)
        self.login_tab_widget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.login_tab_widget.setTabsClosable(True)
        self.login_tab_widget.setTabBarAutoHide(True)
        self.login_tab_widget.setObjectName("login_tab_widget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.login_backdrop = QtWidgets.QLabel(self.tab)
        self.login_backdrop.setGeometry(QtCore.QRect(-30, 0, 441, 591))
        self.login_backdrop.setStyleSheet("QWidget {\n"
"  background-color: #232629;\n"
"  color: #ffffff;\n"
"}\n"
"\n"
"QGroupBox,\n"
"QFrame {\n"
"  background-color: #232629;\n"
"  border: 2px solid #4f5b62;\n"
"  border-radius: 4px;\n"
"}\n"
"\n"
"QDateTimeEdit,\n"
"QSpinBox,\n"
"QDoubleSpinBox,\n"
"QTreeView,\n"
"QListView,\n"
"QLineEdit,\n"
"QComboBox {\n"
"  color: #1de9b6;\n"
"  background-color: #31363b;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 4px;\n"
"  height: 32px;\n"
"}\n"
"\n"
"QRadioButton::indicator,\n"
"QCheckBox::indicator {\n"
"  width: 16px;\n"
"  height: 16px;\n"
"  border: 2px solid #1de9b6;\n"
"  border-radius: 0;\n"
"  transform: rotate(45deg);\n"
"  transform-origin: center;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"  background-color: #1de9b6;\n"
"  border-color: #1de9b6;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover,\n"
"QCheckBox::indicator:hover {\n"
"  border-color: rgba(29, 233, 182, 0.8);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QCheckBox::indicator:checked:hover {\n"
"  border-color: #1de9b6;\n"
"}")
        self.login_backdrop.setText("")
        self.login_backdrop.setObjectName("login_backdrop")
        self.username_lineedit = QtWidgets.QLineEdit(self.tab)
        self.username_lineedit.setGeometry(QtCore.QRect(95, 180, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.username_lineedit.setFont(font)
        self.username_lineedit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.username_lineedit.setObjectName("username_lineedit")
        self.password_lineedit = QtWidgets.QLineEdit(self.tab)
        self.password_lineedit.setGeometry(QtCore.QRect(95, 245, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.password_lineedit.setFont(font)
        self.password_lineedit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.password_lineedit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_lineedit.setObjectName("password_lineedit")
        self.c_label_button = QtWidgets.QPushButton(self.tab)
        self.c_label_button.setGeometry(QtCore.QRect(230, 500, 30, 30))
        self.c_label_button.setMaximumSize(QtCore.QSize(30, 30))
        palette = QtGui.QPalette()
        self.c_label_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.c_label_button.setFont(font)
        self.c_label_button.setMouseTracking(True)
        self.c_label_button.setCheckable(False)
        self.c_label_button.setObjectName("c_label_button")
        self.u_label_button = QtWidgets.QPushButton(self.tab)
        self.u_label_button.setGeometry(QtCore.QRect(130, 500, 30, 30))
        self.u_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.u_label_button.setFont(font)
        self.u_label_button.setCheckable(False)
        self.u_label_button.setChecked(False)
        self.u_label_button.setObjectName("u_label_button")
        self.o_label_button = QtWidgets.QPushButton(self.tab)
        self.o_label_button.setGeometry(QtCore.QRect(80, 500, 30, 30))
        self.o_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.o_label_button.setFont(font)
        self.o_label_button.setObjectName("o_label_button")
        self.login_button = QtWidgets.QPushButton(self.tab)
        self.login_button.setGeometry(QtCore.QRect(95, 325, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.login_button.setFont(font)
        self.login_button.setObjectName("login_button")
        self.login_label = QtWidgets.QLabel(self.tab)
        self.login_label.setGeometry(QtCore.QRect(140, 110, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.login_label.setFont(font)
        self.login_label.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.login_label.setObjectName("login_label")
        self.S_label_button = QtWidgets.QPushButton(self.tab)
        self.S_label_button.setGeometry(QtCore.QRect(30, 500, 30, 30))
        self.S_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.S_label_button.setFont(font)
        self.S_label_button.setObjectName("S_label_button")
        self.r_label_button = QtWidgets.QPushButton(self.tab)
        self.r_label_button.setGeometry(QtCore.QRect(180, 500, 30, 30))
        self.r_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.r_label_button.setFont(font)
        self.r_label_button.setObjectName("r_label_button")
        self.Forgot_username_label = QtWidgets.QLabel(self.tab)
        self.Forgot_username_label.setGeometry(QtCore.QRect(101, 375, 201, 16))
        self.Forgot_username_label.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.Forgot_username_label.setObjectName("Forgot_username_label")
        self.e_label_button = QtWidgets.QPushButton(self.tab)
        self.e_label_button.setGeometry(QtCore.QRect(280, 500, 30, 30))
        self.e_label_button.setMaximumSize(QtCore.QSize(30, 30))
        palette = QtGui.QPalette()
        self.e_label_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.e_label_button.setFont(font)
        self.e_label_button.setMouseTracking(True)
        self.e_label_button.setCheckable(False)
        self.e_label_button.setObjectName("e_label_button")
        self.want_to_register_button = QtWidgets.QLabel(self.tab)
        self.want_to_register_button.setGeometry(QtCore.QRect(140, 400, 101, 16))
        self.want_to_register_button.setStyleSheet("color:rgba(0, 0, 0, 210);")
        self.want_to_register_button.setObjectName("want_to_register_button")
        self.d_label_button = QtWidgets.QPushButton(self.tab)
        self.d_label_button.setGeometry(QtCore.QRect(330, 500, 30, 30))
        self.d_label_button.setMaximumSize(QtCore.QSize(30, 30))
        palette = QtGui.QPalette()
        self.d_label_button.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.d_label_button.setFont(font)
        self.d_label_button.setMouseTracking(True)
        self.d_label_button.setCheckable(False)
        self.d_label_button.setObjectName("d_label_button")
        self.o_label_button_2 = QtWidgets.QPushButton(self.tab)
        self.o_label_button_2.setGeometry(QtCore.QRect(100, 440, 30, 30))
        self.o_label_button_2.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.o_label_button_2.setFont(font)
        self.o_label_button_2.setObjectName("o_label_button_2")
        self.P_label_button = QtWidgets.QPushButton(self.tab)
        self.P_label_button.setGeometry(QtCore.QRect(150, 440, 30, 30))
        self.P_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.P_label_button.setFont(font)
        self.P_label_button.setObjectName("P_label_button")
        self.E_label_button = QtWidgets.QPushButton(self.tab)
        self.E_label_button.setGeometry(QtCore.QRect(200, 440, 30, 30))
        self.E_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.E_label_button.setFont(font)
        self.E_label_button.setObjectName("E_label_button")
        self.N_label_button = QtWidgets.QPushButton(self.tab)
        self.N_label_button.setGeometry(QtCore.QRect(250, 440, 30, 30))
        self.N_label_button.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.N_label_button.setFont(font)
        self.N_label_button.setObjectName("N_label_button")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../OneDrive/Documents/New Structure/icons/exit-to-app.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_tab_widget.addTab(self.tab, icon, "")
        self.information_tab2 = QtWidgets.QWidget()
        self.information_tab2.setObjectName("information_tab2")
        self.tab_2_widget_holder = QAxContainer.QAxWidget(self.information_tab2)
        self.tab_2_widget_holder.setProperty("geometry", QtCore.QRect(10, 170, 391, 391))
        self.tab_2_widget_holder.setObjectName("tab_2_widget_holder")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../../../OneDrive/Documents/New Structure/icons/go-back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.login_tab_widget.addTab(self.information_tab2, icon1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.login_tab_widget.addTab(self.tab_2, "")

        self.retranslateUi(Form)
        self.login_tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.program_title.setText(_translate("Form", "Diamond💎\n"
"               Sorter"))
        self.program_description.setText(_translate("Form", "Hi,\n"
"Welcome to Diamond Sorter channel.\n"
"Don\'t forget to subscribe."))
        self.updates_label.setText(_translate("Form", "Updates"))
        self.update_1_label.setText(_translate("Form", "1/12/24\n"
"-Launched to Pre-Release of DIamond Sorter\n"
"-Configured Licensing System\n"
"-Developed Login GUI"))
        self.update_2_label.setText(_translate("Form", "1/14/24\n"
"- Developed Telegram Licensing Bot\n"
"- Added the 5 Feature Extensions\n"
"- Updated Anti Detect Browser\n"
"- Added Telegram Bot Forwarding Snatcher"))
        self.update_3_label.setText(_translate("Form", "T.B.A"))
        self.update_1_label_2.setText(_translate("Form", "1/12/24\n"
"-Launched to Pre-Release of DIamond Sorter\n"
"-Configured Licensing System\n"
"-Developed Login GUI"))
        self.update_1_label_3.setText(_translate("Form", "1/12/24\n"
"-Launched to Pre-Release of DIamond Sorter\n"
"-Configured Licensing System\n"
"-Developed Login GUI"))
        self.update_1_label_4.setText(_translate("Form", "1/12/24\n"
"-Launched to Pre-Release of DIamond Sorter\n"
"-Configured Licensing System\n"
"-Developed Login GUI"))
        self.username_lineedit.setPlaceholderText(_translate("Form", "  User Name"))
        self.password_lineedit.setPlaceholderText(_translate("Form", "  Password"))
        self.c_label_button.setText(_translate("Form", "C"))
        self.u_label_button.setText(_translate("Form", "U"))
        self.o_label_button.setText(_translate("Form", "O"))
        self.login_button.setText(_translate("Form", "L o g  I n"))
        self.login_label.setText(_translate("Form", "Log In"))
        self.S_label_button.setText(_translate("Form", "S"))
        self.r_label_button.setText(_translate("Form", "R"))
        self.Forgot_username_label.setText(_translate("Form", "<a href=https://t.me/OpenSourcedPros>Forgot your User Name or password?</a>"))
        self.e_label_button.setText(_translate("Form", "E"))
        self.want_to_register_button.setText(_translate("Form", "<a href=\"#\">Want to Register?</a>"))
        self.d_label_button.setText(_translate("Form", "D"))
        self.o_label_button_2.setText(_translate("Form", "O"))
        self.P_label_button.setText(_translate("Form", "P"))
        self.E_label_button.setText(_translate("Form", "E"))
        self.N_label_button.setText(_translate("Form", "N"))
        self.login_tab_widget.setTabText(self.login_tab_widget.indexOf(self.tab), _translate("Form", "Login"))
        self.login_tab_widget.setTabText(self.login_tab_widget.indexOf(self.information_tab2), _translate("Form", "Information"))
        self.login_tab_widget.setTabText(self.login_tab_widget.indexOf(self.tab_2), _translate("Form", "Project Information + Updates"))
        self.login_button.clicked.connect(self.handle_login)  # Connect the login_button clicked signal to handle_login slot



    def getchecksum():
        path = os.path.basename(__file__)
        if not os.path.exists(path):
            path = path[:-2] + "exe"
        md5_hash = hashlib.md5()
        a_file = open(path, "rb")
        content = a_file.read()
        md5_hash.update(content)
        digest = md5_hash.hexdigest()
        return digest
        
    def handle_login(self):
        username = self.login_tab_widget.findChild(QtWidgets.QLineEdit, "username_lineedit").text()
        password = self.password_lineedit.text()
        
        # Check if username or password is empty
        if not username or not password:
            error_message = "Please enter both a username and password."
            QtWidgets.QMessageBox.warning(self.login_tab, "Login Error", error_message, QtWidgets.QMessageBox.Ok)
            return
    
        hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        
        login = keyauthapp.login(username, password, hwid)

    def open_forgot_password_link(self, link):
        webbrowser.open(link)  # Open the provided link in a web browser

    def register_activation_key():
        # Display three choices for registering an activation key
        reply = QtWidgets.QMessageBox.question(self.login_tab, "Register Activation Key", "Choose an option to register an activation key:",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            # Buy from Store
            buy_from_store()
        elif reply == QtWidgets.QMessageBox.No:
            # Buy from Developer
            buy_from_developer()
        elif reply == QtWidgets.QMessageBox.Cancel:
            # Buy from KeyAuth
            buy_from_keyauth()
                    
                
    def open_register_dialog(self):
        license_key, ok = QtWidgets.QInputDialog.getText(Form, "Register", "Enter License Key:")
        if ok:
            response = self.verify_license_key(license_key)
            if response["status"] == "success":
                username, ok1 = QtWidgets.QInputDialog.getText(Form, "Register", "Enter Username:")
                password, ok2 = QtWidgets.QInputDialog.getText(Form, "Register", "Enter Password:", QtWidgets.QLineEdit.Password)
                if ok1 and ok2:
                    print("License Key:", license_key)
                    print("Username:", username)
                    print("Password:", password)
            else:
                QtWidgets.QMessageBox.warning(Form, "Invalid License", "The license key is not valid. Please try again.", QtWidgets.QMessageBox.Ok)
    
    def verify_license_key(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()
    
        response = self.api.verify_license(key, hwid)
        return response      
                
    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            time.sleep(3)
            os._exit(1)

    def buy_from_store():
        # Implement the logic to buy an activation key from the store
        pass
    
    def buy_from_developer():
        # Implement the logic to buy an activation key from the developer
        pass
    
    def buy_from_keyauth():
        # Implement the logic to buy an activation key from KeyAuth
        pass


    def open_signup_screen(self):
        # Open the signup screen with license key activation
        signup_screen = SignupScreen()
        signup_screen.exec_()


    sessionid = enckey = ""
    initialized = True

    def init(self):
        if self.sessionid != "":
            print("You've already initialized!")
            time.sleep(3)
            os._exit(1)

        sent_key = str(uuid4())[:16]
        
        self.enckey = sent_key + "-" + self.secret
        
        post_data = {
            "type": "init",
            "ver": self.version,
            "hash": self.hash_to_check,
            "enckey": sent_key,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        if response == "KeyAuth_Invalid":
            print("The application doesn't exist")
            time.sleep(3)
            os._exit(1)

        json = jsond.loads(response)

        if json["message"] == "invalidver":
            if json["download"] != "":
                print("New Version Available")
                download_link = json["download"]
                os.system(f"start {download_link}")
                time.sleep(3)
                os._exit(1)
            else:
                print("Invalid Version, Contact owner to add download link to latest app version")
                time.sleep(3)
                os._exit(1)

        if not json["success"]:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

        self.sessionid = json["sessionid"]
        self.initialized = True
        
        if json["newSession"]:
            time.sleep(0.1)


    def register(self, user, password, license, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "register",
            "username": user,
            "pass": password,
            "key": license,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print(json["message"])
            self.__load_user_data(json["info"])
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def upgrade(self, user, license):
        self.checkinit()

        post_data = {
            "type": "upgrade",
            "username": user,
            "key": license,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print(json["message"])
            print("Please restart program and login")
            time.sleep(3)
            os._exit(1)
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def login(self, user, password, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "login",
            "username": user,
            "pass": password,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
            print(json["message"])
            subprocess.run(["python", "diamondsorter.py"])  # Launch diamondsorter.py
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)
    def handle_login_button_press(self):
        # Code for handling login button press and obtaining the response
        response = self.login(user, password, hwid)
        
        if response == "Logged in!":
            subprocess.run(["python", "DiamondSorter.py"])  # Launch DiamondSorter.py
        else:
            # Handle login failure
            pass
    def license(self, key, hwid=None):
        self.checkinit()
        if hwid is None:
            hwid = others.get_hwid()

        post_data = {
            "type": "license",
            "key": key,
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_user_data(json["info"])
            print(json["message"])
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def var(self, name):
        self.checkinit()

        post_data = {
            "type": "var",
            "varid": name,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def getvar(self, var_name):
        self.checkinit()

        post_data = {
            "type": "getvar",
            "var": var_name,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["response"]
        else:
            print(f"NOTE: This is commonly misunderstood. This is for user variables, not the normal variables.\nUse keyauthapp.var(\"{var_name}\") for normal variables");
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def setvar(self, var_name, var_data):
        self.checkinit()

        post_data = {
            "type": "setvar",
            "var": var_name,
            "data": var_data,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def ban(self):
        self.checkinit()

        post_data = {
            "type": "ban",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def file(self, fileid):
        self.checkinit()

        post_data = {
            "type": "file",
            "fileid": fileid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if not json["success"]:
            print(json["message"])
            time.sleep(3)
            os._exit(1)
        return binascii.unhexlify(json["contents"])

    def webhook(self, webid, param, body = "", conttype = ""):
        self.checkinit()

        post_data = {
            "type": "webhook",
            "webid": webid,
            "params": param,
            "body": body,
            "conttype": conttype,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["message"]
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)

    def check(self):
        self.checkinit()

        post_data = {
            "type": "check",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)
        if json["success"]:
            return True
        else:
            return False

    def checkblacklist(self):
        self.checkinit()
        hwid = others.get_hwid()

        post_data = {
            "type": "checkblacklist",
            "hwid": hwid,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }
        response = self.__do_request(post_data)

        json = jsond.loads(response)
        if json["success"]:
            return True
        else:
            return False

    def log(self, message):
        self.checkinit()

        post_data = {
            "type": "log",
            "pcuser": os.getenv('username'),
            "message": message,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        self.__do_request(post_data)

    def fetchOnline(self):
        self.checkinit()

        post_data = {
            "type": "fetchOnline",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            if len(json["users"]) == 0:
                return None
            else:
                return json["users"]
        else:
            return None
            
    def fetchStats(self):
        self.checkinit()

        post_data = {
            "type": "fetchStats",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            self.__load_app_data(json["appinfo"])
            
    def chatGet(self, channel):
        self.checkinit()

        post_data = {
            "type": "chatget",
            "channel": channel,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return json["messages"]
        else:
            return None

    def chatSend(self, message, channel):
        self.checkinit()

        post_data = {
            "type": "chatsend",
            "message": message,
            "channel": channel,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            return True
        else:
            return False

    def checkinit(self):
        if not self.initialized:
            print("Initialize first, in order to use the functions")
            time.sleep(3)
            os._exit(1)

    def changeUsername(self, username):
        self.checkinit()

        post_data = {
            "type": "changeUsername",
            "newUsername": username,
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print("Successfully changed username")
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)  

    def logout(self):
        self.checkinit()

        post_data = {
            "type": "logout",
            "sessionid": self.sessionid,
            "name": self.name,
            "ownerid": self.ownerid
        }

        response = self.__do_request(post_data)

        json = jsond.loads(response)

        if json["success"]:
            print("Successfully logged out")
            time.sleep(3)
            os._exit(1)
        else:
            print(json["message"])
            time.sleep(3)
            os._exit(1)         
            
    def __do_request(self, post_data):
        try:
            response = requests.post(
                "https://keyauth.win/api/1.2/", data=post_data, timeout=10
            )
            
            key = self.secret if post_data["type"] == "init" else self.enckey
            if post_data["type"] == "log": return response.text
                        
            client_computed = hmac.new(key.encode('utf-8'), response.text.encode('utf-8'), hashlib.sha256).hexdigest()
            
            signature = response.headers["signature"]
            
            if not hmac.compare_digest(client_computed, signature):
                print("Signature checksum failed. Request was tampered with or session ended most likely.")
                print("Response: " + response.text)
                time.sleep(3)
                os._exit(1) 
            
            return response.text
        except requests.exceptions.Timeout:
            print("Request timed out. Server is probably down/slow at the moment")

    class application_data_class:
        numUsers = numKeys = app_ver = customer_panel = onlineUsers = ""

    class user_data_class:
        username = ip = hwid = expires = createdate = lastlogin = subscription = subscriptions = ""

    user_data = user_data_class()
    app_data = application_data_class()

    def __load_app_data(self, data):
        self.app_data.numUsers = data["numUsers"]
        self.app_data.numKeys = data["numKeys"]
        self.app_data.app_ver = data["version"]
        self.app_data.customer_panel = data["customerPanelLink"]
        self.app_data.onlineUsers = data["numOnlineUsers"]

    def __load_user_data(self, data):
        self.user_data.username = data["username"]
        self.user_data.ip = data["ip"]
        self.user_data.hwid = data["hwid"] or "N/A"
        self.user_data.expires = data["subscriptions"][0]["expiry"]
        self.user_data.createdate = data["createdate"]
        self.user_data.lastlogin = data["lastlogin"]
        self.user_data.subscription = data["subscriptions"][0]["subscription"]
        self.user_data.subscriptions = data["subscriptions"]


class others:
    @staticmethod
    def get_hwid():
        if platform.system() == "Linux":
            with open("/etc/machine-id") as f:
                hwid = f.read()
                return hwid
        elif platform.system() == 'Windows':
            winuser = os.getlogin()
            sid = win32security.LookupAccountName(None, winuser)[0]  # You can also use WMIC (better than SID, some users had problems with WMIC)
            hwid = win32security.ConvertSidToStringSid(sid)
            return hwid
            '''
            cmd = subprocess.Popen(
                "wmic useraccount where name='%username%' get sid",
                stdout=subprocess.PIPE,
                shell=True,
            )

            (suppost_sid, error) = cmd.communicate()

            suppost_sid = suppost_sid.split(b"\n")[1].strip()

            return suppost_sid.decode()

            ^^ HOW TO DO IT USING WMIC
            '''
        elif platform.system() == 'Darwin':
            output = subprocess.Popen("ioreg -l | grep IOPlatformSerialNumber", stdout=subprocess.PIPE, shell=True).communicate()[0]
            serial = output.decode().split('=', 1)[1].replace(' ', '')
            hwid = serial[1:-2]
            return hwid


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())