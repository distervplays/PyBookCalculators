from classes.JobCalculatorStore import JobCalculatorStore
from classes.BookSequence import BookSection
from PyQt6 import QtCore, QtWidgets, QtGui
from .MainWindow import Ui_MainWindow
from configparser import ConfigParser
import os, json
import pickle

class GUI(Ui_MainWindow):
    def __init__(self, saveDir: str = './saves'):
        super(GUI, self).__init__()
        self.jcs = JobCalculatorStore(sort_sections=False)
        self.pageCount: int = 0
        self.jobId: int|None = None    
        self.saveDir = saveDir
        self.local_saveDir = None
        
        os.makedirs(self.saveDir, exist_ok=True)
        
        self.config = ConfigParser()
        self.__loadConfig()

        
    def __loadConfig(self):
        config_path = os.path.join(self.saveDir, 'config.ini')
        if os.path.exists(config_path):
            self.config.read(config_path)
        self.local_saveDir = self.config.get('Settings', 'saveDir', fallback=None) if self.config.has_section('Settings') else None
            
        
        
        
    def submitJobId(self):
        try:
            self.jobId = int(self.inp_JobId.text())
        except ValueError:
            self.jobId = None
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Icon.Warning)
            msgBox.setText("Job ID must be a whole number.")
            msgBox.setWindowTitle("Invalid Input")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msgBox.exec()
            return None
        self.retranslateUi(self.mw)
        return self.jobId
    
    def __save(self):
        os.makedirs(self.saveDir, exist_ok=True)
        
        data = {
            'jcs': self.jcs,
            'jobId': self.jobId,
        }
        
        with open(os.path.join(self.saveDir, f'job_{self.jobId}.pkl'), 'wb') as file:
            pickle.dump(data, file)
    
    def saveJob(self):
        submitted = self.submitJobId()
        if submitted is None:
            return
        suggested_filename = f"job_{self.jobId}.json" if self.jobId is not None else "job.json"
        
        if self.local_saveDir is None:
            saveDir = QtWidgets.QFileDialog.getSaveFileName(self.mw, "Select Save Path", 
                                                            os.path.join(os.path.dirname(self.saveDir), suggested_filename), 
                                                            "JSON Files (*.json)")[0]
            if not self.config.has_section('Settings'):
                self.config.add_section('Settings')
            self.config.set('Settings', 'saveDir', os.path.dirname(saveDir))
            with open(os.path.join(self.saveDir, 'config.ini'), 'w') as file:
                self.config.write(file)
                
            self.local_saveDir = os.path.dirname(saveDir)
        else:
            saveDir = os.path.join(self.local_saveDir, suggested_filename)
        
        
        if not saveDir:
            return
        try:
            data: dict = {'jobId': self.jobId}
            data.update(self.jcs.to_dict)
            data['pageArray'] = " ".join([str(obj) for obj in data['pageArray']])
            with open(saveDir, 'w') as file:
                json.dump(data, file, indent=4)
            self.__save()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msgBox.setText("Job saved successfully!")
            msgBox.setWindowTitle("Save Job")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msgBox.exec()
        except Exception as e:
            errorBox = QtWidgets.QMessageBox()
            errorBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            errorBox.setText(f"An error occurred: {str(e)}")
            errorBox.setWindowTitle("Error")
            errorBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            errorBox.exec()
            
        self.update_SavesList()
        
    def load(self, job_id: int):
        try:
            filePath = os.path.join(self.saveDir, f'job_{job_id}.pkl')
            with open(filePath, 'rb') as file:
                data = pickle.load(file)
                self.jcs = data['jcs']
                self.jobId = data['jobId']            
                self.cb_AutoFormat.setChecked(self.jcs._sort_sections)
                self.retranslateUi(self.mw)
                self.update_list_KaternSize()
            msgBox = QtWidgets.QMessageBox()
            msgBox.setIcon(QtWidgets.QMessageBox.Icon.Information)
            msgBox.setText("Job loaded successfully!")
            msgBox.setWindowTitle("Load Job")
            msgBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msgBox.exec()
        except Exception as e:
            errorBox = QtWidgets.QMessageBox()
            errorBox.setIcon(QtWidgets.QMessageBox.Icon.Critical)
            errorBox.setText(f"An error occurred: {str(e)}")
            errorBox.setWindowTitle("Error")
            errorBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            errorBox.exec()
            
    def loadJob(self, item):
        job_id = int(item.text().split(' ')[-1])
        self.load(job_id)
        
    def newJob(self):    
        self.jcs = JobCalculatorStore(sort_sections=False)
        self.cb_AutoFormat.setChecked(False)
        self.pageCount = 0
        self.jobId = None
        self.inp_jobId.setText('')
        self.retranslateUi(self.mw)
        self.update_list_KaternSize()
        self.update_list_PageSizes()
    
    def autoFormatChanged(self):
        self.jcs.sort_sections(self.cb_AutoFormat.isChecked())
        self.update_list_KaternSize()

    def remove_section(self, index: int):
        self.jcs.remove_section(index)
        self.update_list_KaternSize()

    def add_section(self, number):
        section = BookSection(number)
        self.jcs.add_section(section)
        self.update_list_KaternSize()

    def update_list_KaternSize(self):
        self.list_KaternSizes.clear()
        sections = self.jcs.sections
        self.pageCount = 0
        for section in sections:
            
            button_size = QtCore.QSize(30, 30)
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(13)
            font.setBold(True)
            
            button = QtWidgets.QPushButton(str(section.size))
            button.setFixedSize(button_size)
            button.setFont(font)
            button.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
                                 "border-radius: 10px;\n"
                                 "color: rgb(90, 90, 90);\n")
            button.clicked.connect(lambda _, obj=section: self.remove_section(obj))
            
            
            item = QtWidgets.QListWidgetItem()
            item.setSizeHint(button.size())
            self.list_KaternSizes.addItem(item)
            self.list_KaternSizes.setItemWidget(item, button)
            
            
            for page in section.pages:
                self.pageCount = max(self.pageCount, page)
        self.retranslateUi(self.mw)
            
        self.update_list_PageSizes()
            
    def update_list_PageSizes(self):
        self.list_PageSizes.clear()
        for index, section in enumerate(self.jcs.sections):
            item = QtWidgets.QListWidgetItem()
            
            
            widget = QtWidgets.QWidget()
            widget.setFixedWidth(self.list_PageSizes.viewport().width())
            widget.setContentsMargins(0, 0, 0, 0)
            
            layout = QtWidgets.QHBoxLayout(widget)
            layout.setContentsMargins(0, 0, 0, 0)
            layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
            
            font = QtGui.QFont()
            font.setFamily("Segoe UI")
            font.setPointSize(12)
            font.setBold(True)

            # Index label at the beginning of the line
            lbl_index = QtWidgets.QLabel(str(index))
            lbl_index.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            lbl_index.setFixedWidth(self.widget_PurpleSide.width())
            lbl_index.setFixedHeight(40)
            lbl_index.setStyleSheet("color: white;\n")
            lbl_index.setFont(font)
            layout.addWidget(lbl_index)

            button = QtWidgets.QPushButton(str(section.size))
            button.setFixedWidth(35)
            button.setFixedHeight(35)
            button.setFont(font)
            button.setStyleSheet("border: 1.5px solid rgb(140, 140, 140);\n"
                                 "border-radius: 10px;\n"
                                 "color: rgb(90, 90, 90);\n")
            
            button.clicked.connect(lambda: self.remove_section(int(lbl_index.text())))
            layout.addWidget(button, alignment=QtCore.Qt.AlignmentFlag.AlignVCenter)


            widget_pages = QtWidgets.QWidget(parent=widget)
            widget_pages.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
            widget_pages.setStyleSheet("border-bottom: 1.5px solid rgba(140, 140, 140, 0.4);\n"
                                       "border-left: 1.5px solid rgba(140, 140, 140, 0.4);\n")
            layout.addWidget(widget_pages, alignment=QtCore.Qt.AlignmentFlag.AlignVCenter)

            lbl_Pages = QtWidgets.QLabel(parent=widget_pages)
            lbl_Pages.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
            lbl_Pages.setText(str(', '.join(map(str, section.pages))))
            
            layout_pages = QtWidgets.QVBoxLayout()
            layout_pages.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
            layout_pages.setContentsMargins(0, 0, 0, 0)
            layout_pages.setSpacing(0)
            widget_pages.setLayout(layout_pages)
            
            lbl_Pages.setStyleSheet("border: None;\n"
                                    "padding-left: 10px;\n")
            lbl_Pages.setFont(font)
            lbl_Pages.setWordWrap(True)
            lbl_Pages.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
            
            
            def adjust_font_size(label):
                font = label.font()
                font_metrics = QtGui.QFontMetrics(font)
                text = label.text()
                rect = label.contentsRect()
                while font_metrics.boundingRect(rect, QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter, text).height() > rect.height():
                    font.setPointSize(font.pointSize() - 1)
                    font_metrics = QtGui.QFontMetrics(font)
                label.setFont(font)
            
            adjust_font_size(lbl_Pages)
            lbl_Pages.setFont(font)
            layout_pages.addWidget(lbl_Pages)
            widget_pages.setFixedHeight(lbl_Pages.sizeHint().height() + 5)


            item.setSizeHint(widget.sizeHint())
            item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsSelectable | QtCore.Qt.ItemFlag.ItemIsEnabled)
            widget_pages.setFixedHeight(item.sizeHint().height())
            lbl_Pages.setFixedHeight(item.sizeHint().height())
            lbl_Pages.setAlignment(QtCore.Qt.AlignmentFlag.AlignVCenter)
            
            self.list_PageSizes.addItem(item)
            self.list_PageSizes.setItemWidget(item, widget)
        
    def update_SavesList(self):
        self.list_SavedJobs.clear()
        jobs = []
        for filename in os.listdir(self.saveDir):
            if filename.endswith('.pkl'):
                job_id = int(filename.split('_')[1].split('.')[0])
                jobs.append((job_id, filename))
        
        jobs.sort(reverse=True, key=lambda x: x[0])
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        font.setBold(True)
        for job_id, filename in jobs:
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignHCenter)
            item.setText(f"Job ID: {job_id}")
            item.setFont(font)
            item.setSizeHint(QtCore.QSize(item.sizeHint().width(), 50))  # Increase the height to space them more apart
            self.list_SavedJobs.addItem(item)
