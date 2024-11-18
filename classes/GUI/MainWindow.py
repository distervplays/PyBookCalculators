from PyQt6 import QtCore, QtGui, QtWidgets
from classes.JobCalculatorStore import JobCalculatorStore


class Ui_MainWindow(object):
    def __init__(self):
        self.jcs = JobCalculatorStore()
    
    def on_resize(self, event):
        if self.mw.height() > 500:
            extra_height = self.mw.height()-500
            new_height = self.original_size.height() + extra_height
            self.widget_Bottem.setGeometry(QtCore.QRect(0, 340, 825, new_height))
            self.widget_PurpleSide.setGeometry(QtCore.QRect(0, 0, 50, 220 + extra_height))
            self.list_PageSizes.setGeometry(QtCore.QRect(0, 0, 825, 160 + extra_height))
        else:
            self.widget_Bottem.setGeometry(self.original_size)
            self.widget_PurpleSide.setGeometry(QtCore.QRect(0, 0, 50, 220))
            self.list_PageSizes.setGeometry(QtCore.QRect(0, 0, 825, 160))
        event.accept()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(825, 500)
        MainWindow.setMaximumSize(825, 1080)
        MainWindow.setMinimumSize(825, 500)
        self.mw = MainWindow
        
        # Set the application icon
        icon = QtGui.QIcon("/bin/icon.ico")
        MainWindow.setWindowIcon(icon) 
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.DefaultContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background: rgb(255, 255, 255);\n"
    "border-color: rgb(90,90,90);\n"
    "color: rgb(90,90,90);")
        
        self.widget_Bottem = QtWidgets.QWidget(parent=MainWindow)
        self.original_size = QtCore.QRect(0, 340, 825, 180)
        self.widget_Bottem.setGeometry(self.original_size)
        
        MainWindow.resizeEvent = self.on_resize


    
        self.widget_Bottem.setGeometry(QtCore.QRect(0, 340, 825, 200))
        self.widget_Bottem.setStyleSheet("border: None;\n"
"background: white;\n"
"")
        self.widget_Bottem.setObjectName("widget_Bottem")
        effect = QtWidgets.QGraphicsDropShadowEffect(
            offset=QtCore.QPointF(0, -5), blurRadius=25, color=QtGui.QColor("#c2c0c0")
        )
        self.widget_Bottem.setGraphicsEffect(effect)
        
        

        self.widget_PurpleSide = QtWidgets.QWidget(parent=self.widget_Bottem)
        self.widget_PurpleSide.setGeometry(QtCore.QRect(0, 0, 50, 220))
        self.widget_PurpleSide.setStyleSheet("background: rgb(67,48,168);")
        self.widget_PurpleSide.setObjectName("widget_PurpleSide")
        
        
        self.list_PageSizes = QtWidgets.QListWidget(parent=self.widget_Bottem)
        self.list_PageSizes.setGeometry(QtCore.QRect(50, 0, 775, 160))
        self.list_PageSizes.setStyleSheet("""
            border: None;
            background: transparent;
            """)
        
        self.list_PageSizes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.list_PageSizes.verticalScrollBar().setStyleSheet("""

            QScrollBar {
                border: None;
                background: transparent;
            }
            QScrollBar:vertical {
                border: none;
                border-left: 1.5px solid #c0c0c0;
                background: #f0f0f0;
                width: 12px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: #c0c0c0;
                min-height: 20px;
                border-radius: 5px;
            }
            QScrollBar::add-line:vertical {
                background: none;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                background: none;
                height: 0px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """)
        self.list_PageSizes.setObjectName("list_PageSizes")
        
        
        self.list_KaternSizes = QtWidgets.QListWidget(parent=MainWindow)
        self.list_KaternSizes.setGeometry(QtCore.QRect(10, 290, 751, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_KaternSizes.sizePolicy().hasHeightForWidth())
        self.list_KaternSizes.setSizePolicy(sizePolicy)
        self.list_KaternSizes.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.list_KaternSizes.setStyleSheet("border: None;\n"
                                            "background: transparent;")
        self.list_KaternSizes.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.list_KaternSizes.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.list_KaternSizes.setObjectName("list_KaternSizes")
        self.list_KaternSizes.setSpacing(5)
        
        self.widget_TabContainer = QtWidgets.QWidget(parent=MainWindow)
        self.widget_TabContainer.setGeometry(QtCore.QRect(80, 50, 671, 241))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_TabContainer)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.widget_TabContainer.setObjectName("widget_TabContainer")
        self.widget_SequenceSizes = QtWidgets.QWidget(parent=self.widget_TabContainer)
        self.widget_SequenceSizes.setGeometry(QtCore.QRect(0, 0, 221, 241))
        self.widget_SequenceSizes.setStyleSheet("border-right: 1px solid rgba(90, 90, 90, 0.6);")
        self.widget_SequenceSizes.setObjectName("widget_SequenceSizes")
        self.lbl_TitleSeqSizes = QtWidgets.QLabel(parent=self.widget_SequenceSizes)
        self.lbl_TitleSeqSizes.setGeometry(QtCore.QRect(0, 0, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_TitleSeqSizes.setFont(font)
        self.lbl_TitleSeqSizes.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_TitleSeqSizes.setObjectName("lbl_TitleSeqSizes")
        
        self.widget_SeqBtns = QtWidgets.QWidget(parent=self.widget_SequenceSizes)
        self.widget_SeqBtns.setGeometry(QtCore.QRect(30, 50, 160, 160))
        self.widget_SeqBtns.setStyleSheet("border: None;")
        self.widget_SeqBtns.setObjectName("widget_SeqBtns")
        self.grid_layout = QtWidgets.QGridLayout(self.widget_SeqBtns)
        self.grid_layout.setContentsMargins(0, 0, 0, 0)
        self.grid_layout.setSpacing(10)
        
        button_size = QtCore.QSize(45, 45)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        
        self.btn_Sequence4 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence4.setMinimumSize(button_size)
        self.btn_Sequence4.setMaximumSize(button_size)
        self.btn_Sequence4.setFont(font)
        self.btn_Sequence4.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence4.setObjectName("btn_Sequence4")
        self.grid_layout.addWidget(self.btn_Sequence4, 0, 0)
        self.btn_Sequence4.clicked.connect(lambda: self.add_section(4))
        
        self.btn_Sequence8 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence8.setMinimumSize(button_size)
        self.btn_Sequence8.setMaximumSize(button_size)
        self.btn_Sequence8.setFont(font)
        self.btn_Sequence8.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence8.setObjectName("btn_Sequence8")
        self.grid_layout.addWidget(self.btn_Sequence8, 0, 1)
        self.btn_Sequence8.clicked.connect(lambda: self.add_section(8))
        
        self.btn_Sequence12 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence12.setMinimumSize(button_size)
        self.btn_Sequence12.setMaximumSize(button_size)
        self.btn_Sequence12.setFont(font)
        self.btn_Sequence12.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence12.setObjectName("btn_Sequence12")
        self.grid_layout.addWidget(self.btn_Sequence12, 0, 2)
        self.btn_Sequence12.clicked.connect(lambda: self.add_section(12))
        
        self.btn_Sequence16 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence16.setMinimumSize(button_size)
        self.btn_Sequence16.setMaximumSize(button_size)
        self.btn_Sequence16.setFont(font)
        self.btn_Sequence16.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence16.setObjectName("btn_Sequence16")
        self.grid_layout.addWidget(self.btn_Sequence16, 1, 0)
        self.btn_Sequence16.clicked.connect(lambda: self.add_section(16))
        
        self.btn_Sequence20 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence20.setMinimumSize(button_size)
        self.btn_Sequence20.setMaximumSize(button_size)
        self.btn_Sequence20.setFont(font)
        self.btn_Sequence20.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence20.setObjectName("btn_Sequence20")
        self.grid_layout.addWidget(self.btn_Sequence20, 1, 1)
        self.btn_Sequence20.clicked.connect(lambda: self.add_section(20))
        
        self.btn_Sequence24 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence24.setMinimumSize(button_size)
        self.btn_Sequence24.setMaximumSize(button_size)
        self.btn_Sequence24.setFont(font)
        self.btn_Sequence24.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence24.setObjectName("btn_Sequence24")
        self.grid_layout.addWidget(self.btn_Sequence24, 1, 2)
        self.btn_Sequence24.clicked.connect(lambda: self.add_section(24))
        
        self.btn_Sequence28 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence28.setMinimumSize(button_size)
        self.btn_Sequence28.setMaximumSize(button_size)
        self.btn_Sequence28.setFont(font)
        self.btn_Sequence28.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence28.setObjectName("btn_Sequence28")
        self.grid_layout.addWidget(self.btn_Sequence28, 2, 0)
        self.btn_Sequence28.clicked.connect(lambda: self.add_section(28))
        
        self.btn_Sequence32 = QtWidgets.QPushButton(parent=self.widget_SeqBtns)
        self.btn_Sequence32.setMinimumSize(button_size)
        self.btn_Sequence32.setMaximumSize(button_size)
        self.btn_Sequence32.setFont(font)
        self.btn_Sequence32.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
    "border-radius: 10px;\n"
    "color: rgb(90, 90, 90);\n"
    "")
        self.btn_Sequence32.setObjectName("btn_Sequence32")
        self.grid_layout.addWidget(self.btn_Sequence32, 2, 1)
        self.btn_Sequence32.clicked.connect(lambda: self.add_section(32))
        
        self.widget_Settings = QtWidgets.QWidget(parent=self.widget_TabContainer)
        self.widget_Settings.setGeometry(QtCore.QRect(230, 0, 221, 241))
        self.widget_Settings.setStyleSheet("")
        self.widget_Settings.setObjectName("widget_Settings")
        self.lbl_TitleSettings = QtWidgets.QLabel(parent=self.widget_Settings)
        self.lbl_TitleSettings.setGeometry(QtCore.QRect(0, 0, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_TitleSettings.setFont(font)
        self.lbl_TitleSettings.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_TitleSettings.setObjectName("lbl_TitleSettings")
        self.cb_AutoFormat = QtWidgets.QCheckBox(parent=self.widget_Settings)
        self.cb_AutoFormat.setGeometry(QtCore.QRect(50, 80, 141, 20))
        self.cb_AutoFormat.stateChanged.connect(lambda: self.autoFormatChanged())
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        self.cb_AutoFormat.setFont(font)
        self.cb_AutoFormat.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.cb_AutoFormat.setStyleSheet("QCheckBox::indicator {\n"
"    border: 1.5px solid rgba(140, 140, 140, 1);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    border: 1.5px solid lime;\n"
"    border-radius: 5px;\n"
"    background: lime;\n"
"}")
        self.cb_AutoFormat.setChecked(False)
        self.cb_AutoFormat.setObjectName("cb_AutoFormat")
        self.inp_JobId = QtWidgets.QLineEdit(parent=self.widget_Settings)
        self.inp_JobId.setGeometry(QtCore.QRect(40, 150, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        self.inp_JobId.setFont(font)
        self.inp_JobId.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.inp_JobId.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
                                        "border-radius: 10px;\n"
                                        "padding-left: 5px;\n")
        self.inp_JobId.setObjectName("inp_JobId")
        self.inp_JobId.setAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
        
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        
        self.btn_IdSubmit = QtWidgets.QPushButton(parent=self.widget_Settings)
        self.btn_IdSubmit.setGeometry(QtCore.QRect(30, 190, 91, 25))
        self.btn_IdSubmit.setFont(font)
        self.btn_IdSubmit.setStyleSheet("border: None;\n"
"background: rgb(235,99,0);\n"
"border-radius: 8px;\n"
"color: white;")
        self.btn_IdSubmit.setObjectName("btn_IdSubmit")
        self.btn_IdSubmit.clicked.connect(lambda: self.submitJobId())
        
        self.btn_JobSave = QtWidgets.QPushButton(parent=self.widget_Settings)
        self.btn_JobSave.setGeometry(QtCore.QRect(130, 190, 71, 25))
        self.btn_JobSave.setFont(font)
        self.btn_JobSave.setStyleSheet("border: None;\n"
"background: rgb(235,99,0);\n"
"border-radius: 8px;\n"
"color: white;")
        self.btn_JobSave.setObjectName("btn_JobSave")
        self.btn_JobSave.clicked.connect(lambda: self.saveJob())
        
        self.widget_LoadJobs = QtWidgets.QWidget(parent=self.widget_TabContainer)
        self.widget_LoadJobs.setGeometry(QtCore.QRect(450, 0, 221, 241))
        self.widget_LoadJobs.setStyleSheet("border-left: 1px solid rgba(90, 90, 90, 0.6);")
        self.widget_LoadJobs.setObjectName("widget_LoadJobs")
        self.lbl_TitleLoadJobs = QtWidgets.QLabel(parent=self.widget_LoadJobs)
        self.lbl_TitleLoadJobs.setGeometry(QtCore.QRect(0, 0, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.lbl_TitleLoadJobs.setFont(font)
        self.lbl_TitleLoadJobs.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lbl_TitleLoadJobs.setObjectName("lbl_TitleLoadJobs")
        self.list_SavedJobs = QtWidgets.QListWidget(parent=self.widget_LoadJobs)
        self.list_SavedJobs.setGeometry(QtCore.QRect(40, 40, 141, 131))
        self.list_SavedJobs.setStyleSheet("border: 2px solid rgb(90, 90, 90);\n"
"border-radius: 10px;")
        self.list_SavedJobs.setObjectName("list_SavedJobs")
        self.list_SavedJobs.itemClicked.connect(self.loadJob)
        
        self.lbl_JobId = QtWidgets.QLabel(parent=self.widget_LoadJobs)
        self.lbl_JobId.setGeometry(QtCore.QRect(80, 180, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        self.lbl_JobId.setFont(font)
        self.lbl_JobId.setStyleSheet("border: None;")
        self.lbl_JobId.setObjectName("lbl_JobId")
        self.lbl_PageCount = QtWidgets.QLabel(parent=self.widget_LoadJobs)
        self.lbl_PageCount.setGeometry(QtCore.QRect(80, 200, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        self.lbl_PageCount.setFont(font)
        self.lbl_PageCount.setStyleSheet("border: None;")
        self.lbl_PageCount.setObjectName("lbl_PageCount")
        
        self.logo = QtWidgets.QLabel(parent=MainWindow)
        self.logo.setGeometry(QtCore.QRect(670, 15, 105, 20))
        self.logo.setStyleSheet("border: None;")
        self.logo.setObjectName("logo")
        self.logo.setPixmap(QtGui.QPixmap("./bin/full_icon.png"))
        self.logo.setScaledContents(True)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.update_SavesList()
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence Calculator"))
        self.lbl_TitleSeqSizes.setText(_translate("MainWindow", "SEQEUNCE SIZES"))
        self.btn_Sequence4.setText(_translate("MainWindow", "4"))
        self.btn_Sequence8.setText(_translate("MainWindow", "8"))
        self.btn_Sequence12.setText(_translate("MainWindow", "12"))
        self.btn_Sequence24.setText(_translate("MainWindow", "24"))
        self.btn_Sequence16.setText(_translate("MainWindow", "16"))
        self.btn_Sequence20.setText(_translate("MainWindow", "20"))
        self.btn_Sequence28.setText(_translate("MainWindow", "28"))
        self.btn_Sequence32.setText(_translate("MainWindow", "32"))
        self.lbl_TitleSettings.setText(_translate("MainWindow", "SETTINGS"))
        self.cb_AutoFormat.setText(_translate("MainWindow", "    Auto Format"))
        self.inp_JobId.setPlaceholderText(_translate("MainWindow", "JobId"))
        self.btn_IdSubmit.setText(_translate("MainWindow", "Submit"))
        self.btn_JobSave.setText(_translate("MainWindow", "Save"))
        self.lbl_TitleLoadJobs.setText(_translate("MainWindow", "LOAD JOBS"))
        self.lbl_JobId.setText(_translate("MainWindow", f"Job ID: {self.jobId if self.jobId is not None else 'Null'}"))
        self.inp_JobId.setText(_translate("MainWindow", f"{self.jobId if self.jobId is not None else ''}"))
        self.lbl_PageCount.setText(_translate("MainWindow", f"Last page: {self.pageCount}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
