# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginpanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoginPanel(object):
    def setupUi(self, LoginPanel):
        LoginPanel.setObjectName("LoginPanel")
        LoginPanel.resize(559, 511)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginPanel.sizePolicy().hasHeightForWidth())
        LoginPanel.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoginPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LoginWidget = QtWidgets.QWidget(LoginPanel)
        self.LoginWidget.setObjectName("LoginWidget")
        self.imgLB_logo = ImageLabel(self.LoginWidget)
        self.imgLB_logo.setGeometry(QtCore.QRect(160, 90, 247, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imgLB_logo.sizePolicy().hasHeightForWidth())
        self.imgLB_logo.setSizePolicy(sizePolicy)
        self.imgLB_logo.setMaximumSize(QtCore.QSize(247, 161))
        self.imgLB_logo.setObjectName("imgLB_logo")
        self.lb_register = HyperlinkLabel(self.LoginWidget)
        self.lb_register.setGeometry(QtCore.QRect(9, 459, 181, 24))
        self.lb_register.setObjectName("lb_register")
        self.stackedWidget_login = QtWidgets.QStackedWidget(self.LoginWidget)
        self.stackedWidget_login.setGeometry(QtCore.QRect(145, 232, 291, 211))
        self.stackedWidget_login.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget_login.setLineWidth(20)
        self.stackedWidget_login.setMidLineWidth(23)
        self.stackedWidget_login.setObjectName("stackedWidget_login")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.bt_login = PushButton(self.page)
        self.bt_login.setGeometry(QtCore.QRect(10, 160, 128, 32))
        self.bt_login.setMinimumSize(QtCore.QSize(128, 0))
        self.bt_login.setObjectName("bt_login")
        self.comb_username = EditableComboBox(self.page)
        self.comb_username.setGeometry(QtCore.QRect(50, 20, 151, 24))
        self.comb_username.setObjectName("comb_username")
        self.PasswordLineEdit = PasswordLineEdit(self.page)
        self.PasswordLineEdit.setGeometry(QtCore.QRect(50, 70, 151, 24))
        self.PasswordLineEdit.setObjectName("PasswordLineEdit")
        self.cb_autoLogin = CheckBox(self.page)
        self.cb_autoLogin.setGeometry(QtCore.QRect(0, 120, 131, 22))
        self.cb_autoLogin.setMinimumSize(QtCore.QSize(90, 22))
        self.cb_autoLogin.setObjectName("cb_autoLogin")
        self.cb_rememberPassword = CheckBox(self.page)
        self.cb_rememberPassword.setGeometry(QtCore.QRect(150, 120, 141, 22))
        self.cb_rememberPassword.setMinimumSize(QtCore.QSize(90, 22))
        self.cb_rememberPassword.setObjectName("cb_rememberPassword")
        self.quick_signin_button = PushButton(self.page)
        self.quick_signin_button.setGeometry(QtCore.QRect(150, 160, 128, 32))
        self.quick_signin_button.setMinimumSize(QtCore.QSize(128, 0))
        self.quick_signin_button.setObjectName("quick_signin_button")
        self.stackedWidget_login.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lb_loading = IndeterminateProgressRing(self.page_2)
        self.lb_loading.setGeometry(QtCore.QRect(100, 10, 30, 30))
        self.lb_loading.setMinimumSize(QtCore.QSize(30, 30))
        self.lb_loading.setMaximumSize(QtCore.QSize(30, 30))
        self.lb_loading.setObjectName("lb_loading")
        self.stackedWidget_login.addWidget(self.page_2)
        self.lb_findPassword = CaptionLabel(self.LoginWidget)
        self.lb_findPassword.setGeometry(QtCore.QRect(241, 459, 88, 16))
        self.lb_findPassword.setMinimumSize(QtCore.QSize(48, 0))
        self.lb_findPassword.setObjectName("lb_findPassword")
        self.layoutWidget = QtWidgets.QWidget(self.LoginWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(490, 460, 41, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.layout_QRcode = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.layout_QRcode.setContentsMargins(0, 0, 0, 0)
        self.layout_QRcode.setObjectName("layout_QRcode")
        self.bt_QRcode = ToolButton(self.layoutWidget)
        self.bt_QRcode.setObjectName("bt_QRcode")
        self.layout_QRcode.addWidget(self.bt_QRcode)
        self.verticalLayout.addWidget(self.LoginWidget)

        self.retranslateUi(LoginPanel)
        self.stackedWidget_login.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(LoginPanel)

    def retranslateUi(self, LoginPanel):
        _translate = QtCore.QCoreApplication.translate
        LoginPanel.setWindowTitle(_translate("LoginPanel", "ChatQQ"))
        self.lb_register.setText(_translate("LoginPanel", "Register for an account"))
        self.bt_login.setText(_translate("LoginPanel", "Submit"))
        self.comb_username.setPlaceholderText(_translate("LoginPanel", "Username"))
        self.PasswordLineEdit.setPlaceholderText(_translate("LoginPanel", "Password"))
        self.cb_autoLogin.setText(_translate("LoginPanel", "Auto Login"))
        self.cb_rememberPassword.setText(_translate("LoginPanel", "Remember Pass"))
        self.quick_signin_button.setText(_translate("LoginPanel", "Qucik SIgn In"))
        self.lb_findPassword.setText(_translate("LoginPanel", "Forgot Password"))
from qfluentwidgets import CaptionLabel, CheckBox, EditableComboBox, HyperlinkLabel, ImageLabel, IndeterminateProgressRing, PasswordLineEdit, PushButton, ToolButton


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginPanel = QtWidgets.QWidget()
    ui = Ui_LoginPanel()
    ui.setupUi(LoginPanel)
    LoginPanel.show()
    sys.exit(app.exec_())
