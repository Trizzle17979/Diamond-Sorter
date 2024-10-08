# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessageItemWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MessageItemWidget(object):
    def setupUi(self, MessageItemWidget):
        MessageItemWidget.setObjectName("MessageItemWidget")
        MessageItemWidget.resize(290, 141)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MessageItemWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.avatar = ImageLabel(MessageItemWidget)
        self.avatar.setMinimumSize(QtCore.QSize(40, 40))
        self.avatar.setMaximumSize(QtCore.QSize(40, 40))
        self.avatar.setObjectName("avatar")
        self.verticalLayout_2.addWidget(self.avatar)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.iconIsSendSuccess = IconInfoBadge(MessageItemWidget)
        self.iconIsSendSuccess.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iconIsSendSuccess.setObjectName("iconIsSendSuccess")
        self.horizontalLayout.addWidget(self.iconIsSendSuccess)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_name = StrongBodyLabel(MessageItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_name.sizePolicy().hasHeightForWidth())
        self.lb_name.setSizePolicy(sizePolicy)
        self.lb_name.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lb_name.setObjectName("lb_name")
        self.verticalLayout.addWidget(self.lb_name)
        self.te_content = TextEdit(MessageItemWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_content.sizePolicy().hasHeightForWidth())
        self.te_content.setSizePolicy(sizePolicy)
        self.te_content.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.te_content.setReadOnly(True)
        self.te_content.setObjectName("te_content")
        self.verticalLayout.addWidget(self.te_content)
        spacerItem3 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.setStretch(1, 1)

        self.retranslateUi(MessageItemWidget)
        QtCore.QMetaObject.connectSlotsByName(MessageItemWidget)

    def retranslateUi(self, MessageItemWidget):
        _translate = QtCore.QCoreApplication.translate
        MessageItemWidget.setWindowTitle(_translate("MessageItemWidget", "💎 Chat Messenger"))
        self.lb_name.setText(_translate("MessageItemWidget", "Strong body label"))
from qfluentwidgets import IconInfoBadge, ImageLabel, StrongBodyLabel, TextEdit


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MessageItemWidget = QtWidgets.QWidget()
    ui = Ui_MessageItemWidget()
    ui.setupUi(MessageItemWidget)
    MessageItemWidget.show()
    sys.exit(app.exec_())
