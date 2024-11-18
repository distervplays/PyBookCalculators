from classes.GUI import GUI
from PyQt6 import QtWidgets
import os, sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI(saveDir=os.path.join(os.getcwd(), './.load_saves'))
    ui.setupUi(MainWindow)
    MainWindow.show()
        
    sys.exit(app.exec())

# build the exe : pyinstaller --onefile --windowed main.py