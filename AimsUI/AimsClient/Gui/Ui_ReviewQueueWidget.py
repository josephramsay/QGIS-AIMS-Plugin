# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AimsUI/AimsClient/Gui/Ui_ReviewQueueWidget.ui'
#
# Created: Thu Feb 18 12:34:44 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ReviewQueueWidget(object):
    def setupUi(self, ReviewQueueWidget):
        ReviewQueueWidget.setObjectName(_fromUtf8("ReviewQueueWidget"))
        ReviewQueueWidget.resize(517, 858)
        self.verticalLayout_4 = QtGui.QVBoxLayout(ReviewQueueWidget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.splitter = QtGui.QSplitter(ReviewQueueWidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.uGroupTableView = QueueView(self.horizontalLayoutWidget)
        self.uGroupTableView.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.uGroupTableView.setObjectName(_fromUtf8("uGroupTableView"))
        self.verticalLayout_6.addWidget(self.uGroupTableView)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_6.addWidget(self.label_2)
        self.comboBoxUser = QtGui.QComboBox(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxUser.sizePolicy().hasHeightForWidth())
        self.comboBoxUser.setSizePolicy(sizePolicy)
        self.comboBoxUser.setObjectName(_fromUtf8("comboBoxUser"))
        self.horizontalLayout_6.addWidget(self.comboBoxUser)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout_6)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.verticalLayout.addWidget(self.pushButton_2)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.uFeaturesTableView = QueueView(self.horizontalLayoutWidget_2)
        self.uFeaturesTableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.uFeaturesTableView.setObjectName(_fromUtf8("uFeaturesTableView"))
        self.horizontalLayout_2.addWidget(self.uFeaturesTableView)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.buttonDisplay = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.buttonDisplay.setMaximumSize(QtCore.QSize(70, 16777215))
        self.buttonDisplay.setObjectName(_fromUtf8("buttonDisplay"))
        self.verticalLayout_2.addWidget(self.buttonDisplay)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.splitter)
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setMargin(0)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.uQueueEditor = QueueEditorWidget(self.horizontalLayoutWidget_3)
        self.uQueueEditor.setObjectName(_fromUtf8("uQueueEditor"))
        self.horizontalLayout_3.addWidget(self.uQueueEditor)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.uUpdateButton = QtGui.QPushButton(self.horizontalLayoutWidget_3)
        self.uUpdateButton.setMaximumSize(QtCore.QSize(70, 16777215))
        self.uUpdateButton.setObjectName(_fromUtf8("uUpdateButton"))
        self.verticalLayout_3.addWidget(self.uUpdateButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.splitter)

        self.retranslateUi(ReviewQueueWidget)
        QtCore.QMetaObject.connectSlotsByName(ReviewQueueWidget)

    def retranslateUi(self, ReviewQueueWidget):
        ReviewQueueWidget.setWindowTitle(_translate("ReviewQueueWidget", "Form", None))
        self.label_2.setText(_translate("ReviewQueueWidget", "Filter User:", None))
        self.pushButton.setText(_translate("ReviewQueueWidget", "Accept", None))
        self.pushButton_2.setText(_translate("ReviewQueueWidget", "Reject", None))
        self.buttonDisplay.setText(_translate("ReviewQueueWidget", "Display", None))
        self.uUpdateButton.setText(_translate("ReviewQueueWidget", "Update", None))

from QueueModelView import QueueView
from QueueEditorWidget import QueueEditorWidget
