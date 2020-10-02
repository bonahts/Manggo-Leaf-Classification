# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 20:34:58 2020

@author: bona
"""


import sys
import  cv2  #opencv
import numpy as np 
import matplotlib.pyplot as plt #untuk membuat grafik
import pandas as pd  #untuk dataframe
#import libGLCM as LB
import seaborn as sns 
import os.path
from PyQt5.QtGui import QImage,QPixmap,QIcon
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QTextEdit
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  ##sklearn library untuk knn classifier



class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('cobaui.ui',self)
        self.buttonopen = self.findChild(QPushButton, "buttonopen")
        self.buttongray = self.findChild(QPushButton, "buttongray")
        self.buttonresize = self.findChild(QPushButton, "buttonresize")
        self.buttonglcm = self.findChild(QPushButton, "buttonglcm")
        
        self.buttonopen.clicked.connect(self.tampil)
        self.buttongray.clicked.connect(self.konversigray)
        self.buttongray.setEnabled(False)
        self.buttonresize.setEnabled(False)
        self.buttonglcm.setEnabled(False)
        self.show()
        
        '''self.buttonopen.clicked.connect(self.tampil)
        self.buttongray.clicked.connect(self.konversigray)
        self.buttonglcm.clicked.connect(self.matr)
        self.buttongray.setEnabled(False)
        self.buttonclasifi.setEnabled(False)
        self.buttonglcm.setEnabled(False)
        self.buttonclasifi.clicked.connect(self.classification)'''
        #self.loading.setValue(0)
    def tampil(self):
        #fname = dialog.getOpenFileName(self,'OpenFile','C:\Users\bona\.spyder-py3',"Image File (*.jpg)")
        fname,filter=QFileDialog.getOpenFileName(self,'OpenFile',r'C:\Users\bona\.spyder-py3',"Image File (*.jpg)")
        imagePath = fname[0]
        """
        if fname: 
                self.loadImage(fname)
        else:
                print('Invalid Image')
        """        
        #print(fname)
    
    def loadImage(self,fname):
         self.buttonopen.setEnabled(True)
         self.buttonclasifi.setEnabled(False)
         self.buttonglcm.setEnabled(False)
         self.buttongray.setEnabled(False)
         self.result.setText('')
         self.view_2.clear()
         self.hasilGlCM.setRowCount(0)
         self.image = cv2.imread(fname, cv2.IMREAD_ANYCOLOR)
         self.processedImage = self.image.copy()
         self.previewImage = cv2.resize(self.processedImage, (256,256))
         self.output()
        
    #output rgb    
    def output(self):
        qFormat =QImage.Format_Indexed8
        if len (self.previewImage.shape) == 3:
            if (self.previewImage.shape[2]) == 4:
                qFormat = QImage.Format_RGB8888
            else:
               qFormat = QImage.Format_RGB8888
        img1 = QImage(self.previewImage, self.previewImage.shape[1], self.previewImage.shape[0], 
                             self.previewImage.strides[0], qFormat)
        img1 = img1.rgbSwapped()
        self.view.setPixmap(QPixmap.fromImage(img1))
        self.view.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
     
   # //konversi gray   
    def konversigray(self):
            self.buttonglcm.setEnabled(True)
            self.gray = cv2.cvtColor(self.processedImage, cv2.COLOR_BGR2GRAY)
            self.previewgray = cv2.resize(self.gray, (256,256))
            self.output_grayscale()
            
    #output gray        
    """def output_grayscale(self):
        qFormat =QImage.Format_Indexed8
        if len (self.previewgray.shape) == 3:
            if (self.previewgray.shape[2]) == 4:
                qFormat = QImage.Format_RGB8888
            else:
               qFormat = QImage.Format_RGB8888
        img1 = QImage(self.previewImage, self.previewImage.shape[1], self.previewImage.shape[0], 
                             self.previewImage.strides[0], qFormat)
        img1 = img1.rgbSwapped()
        self.view_2.setPixmap(QPixmap.fromImage(img1))
        self.view_2.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)"""
    
app = QApplication(sys.argv)
window = UI()
app.exec_()
