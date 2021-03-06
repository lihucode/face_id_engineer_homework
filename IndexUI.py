# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IndexUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(751, 441)
        TabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.clockIn_tab = QtWidgets.QWidget()
        self.clockIn_tab.setInputMethodHints(QtCore.Qt.ImhNone)
        self.clockIn_tab.setObjectName("clockIn_tab")
        self.faceIdentification_label = QtWidgets.QLabel(self.clockIn_tab)
        self.faceIdentification_label.setGeometry(QtCore.QRect(10, 20, 461, 371))
        self.faceIdentification_label.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.faceIdentification_label.setAlignment(QtCore.Qt.AlignCenter)
        self.faceIdentification_label.setObjectName("faceIdentification_label")
        self.chooseFace_btn = QtWidgets.QPushButton(self.clockIn_tab)
        self.chooseFace_btn.setGeometry(QtCore.QRect(510, 20, 221, 41))
        self.chooseFace_btn.setObjectName("chooseFace_btn")
        self.identifyClockIn_tab = QtWidgets.QPushButton(self.clockIn_tab)
        self.identifyClockIn_tab.setGeometry(QtCore.QRect(510, 110, 221, 41))
        self.identifyClockIn_tab.setObjectName("identifyClockIn_tab")
        self.clockInRecordsList = QtWidgets.QListWidget(self.clockIn_tab)
        self.clockInRecordsList.setGeometry(QtCore.QRect(510, 180, 221, 211))
        self.clockInRecordsList.setObjectName("clockInRecordsList")
        TabWidget.addTab(self.clockIn_tab, "")
        self.addMember_tab = QtWidgets.QWidget()
        self.addMember_tab.setObjectName("addMember_tab")
        self.faceAddition_label = QtWidgets.QLabel(self.addMember_tab)
        self.faceAddition_label.setGeometry(QtCore.QRect(10, 20, 461, 371))
        self.faceAddition_label.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.faceAddition_label.setAlignment(QtCore.Qt.AlignCenter)
        self.faceAddition_label.setObjectName("faceAddition_label")
        self.addFaceChoose_btn = QtWidgets.QPushButton(self.addMember_tab)
        self.addFaceChoose_btn.setGeometry(QtCore.QRect(510, 30, 221, 41))
        self.addFaceChoose_btn.setObjectName("addFaceChoose_btn")
        self.addFace_btn = QtWidgets.QPushButton(self.addMember_tab)
        self.addFace_btn.setGeometry(QtCore.QRect(510, 200, 221, 41))
        self.addFace_btn.setObjectName("addFace_btn")
        self.addFaceName_lineEdit = QtWidgets.QLineEdit(self.addMember_tab)
        self.addFaceName_lineEdit.setGeometry(QtCore.QRect(510, 110, 221, 31))
        self.addFaceName_lineEdit.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.addFaceName_lineEdit.setDragEnabled(False)
        self.addFaceName_lineEdit.setObjectName("addFaceName_lineEdit")
        self.blackboardAdd_textEidt = QtWidgets.QTextEdit(self.addMember_tab)
        self.blackboardAdd_textEidt.setGeometry(QtCore.QRect(510, 280, 221, 111))
        self.blackboardAdd_textEidt.setObjectName("blackboardAdd_textEidt")
        self.addFaceID_lineEdit = QtWidgets.QLineEdit(self.addMember_tab)
        self.addFaceID_lineEdit.setGeometry(QtCore.QRect(510, 160, 221, 31))
        self.addFaceID_lineEdit.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.addFaceID_lineEdit.setText("")
        self.addFaceID_lineEdit.setDragEnabled(False)
        self.addFaceID_lineEdit.setObjectName("addFaceID_lineEdit")
        TabWidget.addTab(self.addMember_tab, "")
        self.delMember_tab = QtWidgets.QWidget()
        self.delMember_tab.setObjectName("delMember_tab")
        self.faceDeletion_label = QtWidgets.QLabel(self.delMember_tab)
        self.faceDeletion_label.setGeometry(QtCore.QRect(10, 20, 461, 371))
        self.faceDeletion_label.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.faceDeletion_label.setAlignment(QtCore.Qt.AlignCenter)
        self.faceDeletion_label.setObjectName("faceDeletion_label")
        self.delFaceID_lineEdit = QtWidgets.QLineEdit(self.delMember_tab)
        self.delFaceID_lineEdit.setGeometry(QtCore.QRect(500, 20, 221, 31))
        self.delFaceID_lineEdit.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.delFaceID_lineEdit.setText("")
        self.delFaceID_lineEdit.setDragEnabled(False)
        self.delFaceID_lineEdit.setObjectName("delFaceID_lineEdit")
        self.delMemberQuery_btn = QtWidgets.QPushButton(self.delMember_tab)
        self.delMemberQuery_btn.setGeometry(QtCore.QRect(500, 80, 221, 41))
        self.delMemberQuery_btn.setObjectName("delMemberQuery_btn")
        self.delFace_btn = QtWidgets.QPushButton(self.delMember_tab)
        self.delFace_btn.setGeometry(QtCore.QRect(500, 150, 221, 41))
        self.delFace_btn.setObjectName("delFace_btn")
        self.blackboardDel_textEidt = QtWidgets.QTextEdit(self.delMember_tab)
        self.blackboardDel_textEidt.setGeometry(QtCore.QRect(500, 230, 221, 161))
        self.blackboardDel_textEidt.setObjectName("blackboardDel_textEidt")
        TabWidget.addTab(self.delMember_tab, "")
        self.checkMember_tab = QtWidgets.QWidget()
        self.checkMember_tab.setObjectName("checkMember_tab")
        self.membersQuery_listWidget = QtWidgets.QListWidget(self.checkMember_tab)
        self.membersQuery_listWidget.setGeometry(QtCore.QRect(20, 20, 461, 371))
        self.membersQuery_listWidget.setObjectName("membersQuery_listWidget")
        self.membersQuery_btn = QtWidgets.QPushButton(self.checkMember_tab)
        self.membersQuery_btn.setGeometry(QtCore.QRect(500, 20, 221, 41))
        self.membersQuery_btn.setObjectName("membersQuery_btn")
        TabWidget.addTab(self.checkMember_tab, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        self.identifyClockIn_tab.clicked.connect(TabWidget.iden)
        self.addFaceChoose_btn.clicked.connect(TabWidget.chooseFaceToAdd)
        self.addFace_btn.clicked.connect(TabWidget.signUpFace)
        self.chooseFace_btn.clicked.connect(TabWidget.videoCapture)
        self.addFaceName_lineEdit.editingFinished.connect(TabWidget.addFaceName_changed)
        self.addFaceID_lineEdit.editingFinished.connect(TabWidget.addFaceID_changed)
        self.delFaceID_lineEdit.editingFinished.connect(TabWidget.delFaceID_changed)
        self.delMemberQuery_btn.clicked.connect(TabWidget.delMemberQuery)
        self.delFace_btn.clicked.connect(TabWidget.delMember)
        self.membersQuery_btn.clicked.connect(TabWidget.queryMembers)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "人脸识别打卡"))
        self.faceIdentification_label.setText(_translate("TabWidget", "请选择要输入的脸"))
        self.chooseFace_btn.setText(_translate("TabWidget", "输入脸"))
        self.identifyClockIn_tab.setText(_translate("TabWidget", "识别打卡"))
        TabWidget.setTabText(TabWidget.indexOf(self.clockIn_tab), _translate("TabWidget", "打卡"))
        self.faceAddition_label.setText(_translate("TabWidget", "请选择要新增的脸"))
        self.addFaceChoose_btn.setText(_translate("TabWidget", "选择要新增的脸"))
        self.addFace_btn.setText(_translate("TabWidget", "注册新脸到库"))
        self.addFaceName_lineEdit.setPlaceholderText(_translate("TabWidget", "请输入新脸的名字"))
        self.addFaceID_lineEdit.setPlaceholderText(_translate("TabWidget", "请输入身份证号码"))
        TabWidget.setTabText(TabWidget.indexOf(self.addMember_tab), _translate("TabWidget", "增员"))
        self.faceDeletion_label.setText(_translate("TabWidget", "查询已存在的脸"))
        self.delFaceID_lineEdit.setPlaceholderText(_translate("TabWidget", "请输入身份证号"))
        self.delMemberQuery_btn.setText(_translate("TabWidget", "查询"))
        self.delFace_btn.setText(_translate("TabWidget", "删脸"))
        TabWidget.setTabText(TabWidget.indexOf(self.delMember_tab), _translate("TabWidget", "减员"))
        self.membersQuery_btn.setText(_translate("TabWidget", "查询成员"))
        TabWidget.setTabText(TabWidget.indexOf(self.checkMember_tab), _translate("TabWidget", "查看"))
