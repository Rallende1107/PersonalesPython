# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ListAnimes(object):
    def setupUi(self, ListAnimes):
        if not ListAnimes.objectName():
            ListAnimes.setObjectName(u"ListAnimes")
        ListAnimes.resize(961, 600)
        self.pushButton = QPushButton(ListAnimes)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 80, 121, 61))

        self.retranslateUi(ListAnimes)

        QMetaObject.connectSlotsByName(ListAnimes)
    # setupUi

    def retranslateUi(self, ListAnimes):
        ListAnimes.setWindowTitle(QCoreApplication.translate("ListAnimes", u"AnimeList", None))
        self.pushButton.setText(QCoreApplication.translate("ListAnimes", u"PushButton", None))
    # retranslateUi

