import sys

from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

from creater_an_annotation import create_annotation
from copy_dataset import copy_dataset, create_annotation_of_copy_dataset
from create_random_dataset import create_random_dataset_and_annotations
from Iterator import Iterator

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.initIterator()
        self.createAction()
        self.createMenuBar()
        self.createToolBar()
        
    def initUI(self):
                
        self.resize(1200,900)
        self.center()
        self.setWindowTitle('Bears')
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        
        polar_bear_btn=QPushButton('Next polar bear',self)
        brown_bear_btn=QPushButton('Next brown bear',self)

        
        self.lbl = QLabel(self)
        
        hbox = QHBoxLayout()
        hbox.addSpacing(1)
        hbox.addWidget(polar_bear_btn)
        hbox.addWidget(brown_bear_btn)

        vbox = QVBoxLayout()
        vbox.addSpacing(1)
        vbox.addWidget(self.lbl)
        vbox.addLayout(hbox)

        self.centralWidget.setLayout(vbox)
        
        polar_bear_btn.clicked.connect(self.next_polar_bear)
        brown_bear_btn.clicked.connect(self.next_brown_bear)

        self.folderpath = ' '
        
        
        self.show()
     
    def initIterator(self):
        self.polar_bear=Iterator('polar bear','dataset')
        self.brown_bear=Iterator('brown bear','dataset')
        
    def next_polar_bear(self):
        lbl_size = self.lbl.size()
        next_image = next(self.polar_bear)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.next_polar_bear()
                 
    def next_brown_bear(self):
        lbl_size = self.lbl.size()
        next_image = next(self.brown_bear)
        if next_image != None:
            img = QPixmap(next_image).scaled(
                lbl_size, aspectRatioMode=Qt.KeepAspectRatio)
            self.lbl.setPixmap(img)
            self.lbl.setAlignment(Qt.AlignCenter)
        else:        
            self.initIterator()
            self.next_brown_bear()
        
        
    def center(self):
        qr=self.frameGeometry()
        cp=QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
    def createMenuBar(self):
        
        menuBar = self.menuBar()
        
        self.fileMenu = menuBar.addMenu('&File')
        self.fileMenu.addAction(self.exitAction)
        self.fileMenu.addAction(self.changeAction)
        
        self.annotMenu = menuBar.addMenu('&Annotation')
        self.annotMenu.addAction(self.createAnnotAction)
        
        self.dataMenu=menuBar.addMenu('&Datasets')
        self.dataMenu.addAction(self.createData2Action)
        
    def createToolBar(self):
        fileToolBar=self.addToolBar('File')
        fileToolBar.addAction(self.exitAction)
        
        annotToolBar=self.addToolBar('Annotation')
        annotToolBar.addAction(self.createAnnotAction)
        
    def createAction(self):
        self.exitAction = QAction('&Exit')
        self.exitAction.triggered.connect(qApp.quit)

        self.changeAction = QAction('&Change dataset')
        self.changeAction.triggered.connect(self.changeDataset)

        self.createAnnotAction = QAction('&Create annotation for current dataset')
        self.createAnnotAction.triggered.connect(self.createAnnotation)

        self.createData2Action = QAction('&Create dataset2')
        self.createData2Action.triggered.connect(self.createDataset2)

        self.createData3Action = QAction('&Create dataset3')
        self.createData3Action.triggered.connect(self.createDataset3)
        
    def createAnnotation(self):
        if 'dataset2' in str(self.folderpath):
            create_annotation_of_copy_dataset()
        elif 'dataset3' in str(self.folderpath):
            create_random_dataset_and_annotations()
        elif 'dataset' in str(self.folderpath):
            create_annotation()
        compleate = QMessageBox()
        compleate.setWindowTitle("Message")
        compleate.setText("Task completed")
        compleate.exec()
            
    def createDataset2(self):
        copy_dataset()
        self.dataMenu.addAction(self.createData3Action)
        compleate = QMessageBox()
        compleate.setWindowTitle("Message")
        compleate.setText("Task completed")
        compleate.exec()
        
        
    def createDataset3(self):
        create_random_dataset_and_annotations()
        compleate = QMessageBox()
        compleate.setWindowTitle("Message")
        compleate.setText("Task completed")
        compleate.exec()
        
    def changeDataset(self):
        self.folderpath = self.folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    sys.exit(app.exec_())