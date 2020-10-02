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
#import LB
#import tqdm

import seaborn as sns 
import os.path
#from PyQt5 import QtCore
from PyQt5.QtGui import QImage,QPixmap,QIcon
from PyQt5 import QtCore, QtGui, uic
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QPushButton, QTextEdit, QDialog
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier  ##sklearn library untuk knn classifier
from PyQt5.uic import loadUi
#from cobaui import QMainWindow


class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi('cobaui.ui',self)
        self.buttonopen = self.findChild(QPushButton, "buttonopeng")
        self.buttongray = self.findChild(QPushButton, "buttongray")
        self.buttonresize = self.findChild(QPushButton, "buttonresize")
        self.buttonglcm = self.findChild(QPushButton, "buttonglcm")
        #self.buttonclasifi = self.findChild(QPushButton, "buttonclasifi")
        
        self.buttonopeng.clicked.connect(self.tampil)
        self.buttongray.clicked.connect(self.konversigray)
        self.buttonresize.clicked.connect(self.resize)
        #self.buttonglcm.clicked.connect(self.matriksglcm)
        #self.buttonclasifi.clicked.connect(self.klasifikasi)
        
        self.buttonclasifi.setEnabled(True)
        self.buttonglcm.setEnabled(True)
        self.buttonresize.setEnabled(True)
        self.buttongray.setEnabled(True)
        """self.buttonglcm.clicked.connect(self.buttonglcm)
        self.buttonclasifi.clicked.connect(self.buttonclasifi)"""
    
        
    def tampil(self):
        #fname = dialog.getOpenFileName(self,'OpenFile','C:\Users\bona\.spyder-py3',"Image File (*.jpg)")
        fname,filter=QFileDialog.getOpenFileName(self,'OpenFile',r'C:\Users\bona\.spyder-py3',"Image File (*.jpg)")
        if fname: 
                self.loadImage(fname)
                self.loadResize(fname)
                self.konversigray(fname)
        else:
                print("Invalid Image!!!")
        
    def loadImage(self,fname):
       
        #self.labelimage.setPixmap(QPixmap(fname))
        self.buttonclasifi.setEnabled(True)
        self.buttonglcm.setEnabled(True)
        self.buttonresize.setEnabled(True)
        self.buttongray.setEnabled(True)
        #self.buttonexit.setEnabled(True)
        
        #self.result.setText('')
        #self.view_2.clear()
        #self.hasilGlCM.setRowCount(0)
        self.image = cv2.imread(fname, cv2.IMREAD_ANYCOLOR)
        #self.image = self.image.copy()
        #self.image = cv2.resize(self.image, (256,256))
        #print(self.image.size)
        self.displayImage()
    
        
    #output rgb    
    def displayImage(self):
        qFormat = QImage.Format_Indexed8
        if len (self.image.shape) == 3:
            if (self.image.shape[2]) == 4:
                qFormat = QImage.Format_RGBA8888
            else:
               qFormat = QImage.Format_RGB888
        img1 = QImage(self.image, self.image.shape[1], self.image.shape[0],self.image.strides[0], qFormat)
        # BGR to RGB
        img1 = img1.rgbSwapped()
        self.labelimage.setPixmap(QPixmap.fromImage(img1))
        self.labelimage.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
    #resizeimage    
    """def resize(self):
        if fname:
            self.loadResize(fname)
        else:
            print("Invalid Image !!!")"""
            
    def loadResize(self,fname):
        self.buttonclasifi.setEnabled(False)
        self.buttonglcm.setEnabled(False)
        self.buttonresize.setEnabled(True)
        self.buttongray.setEnabled(True)
        #self.buttonexit.setEnabled(True)
        self.image = cv2.imread(fname, cv2.IMREAD_ANYCOLOR)
        self.processedImage = self.image.copy()
        self.previewImage = cv2.resize(self.processedImage, (256,256))
        print(self.image.size)
        self.displayResize()
    #outpurresize    
    def displayResize(self):
        qFormat = QImage.Format_Indexed8
        if len (self.previewImage.shape) == 3:
            if (self.previewImage.shape[2]) == 4:
                qFormat = QImage.Format_RGBA8888
            else:
               qFormat = QImage.Format_RGB888
        img1 = QImage(self.previewImage, self.previewImage.shape[1], self.previewImage.shape[0],self.previewImage.strides[0], qFormat)
        img1 = img1.rgbSwapped()
        self.labelresize.setPixmap(QPixmap.fromImage(img1))
        self.labelresize.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
    #rgb to gray
    def konversigray(self,fname):
        self.buttonclasifi.setEnabled(False)
        self.buttonglcm.setEnabled(False)
        self.buttonresize.setEnabled(True)
        self.buttongray.setEnabled(True)
        #self.buttonexit.setEnabled(True)
        #self.buttonglcm.setEnabled(True)
        #self.image = cv2.imread(fname, cv2.IMREAD_ANYCOLOR)
        #gray = cv2.imread()
        self.gray = cv2.cvtColor(self.processedImage, cv2.COLOR_BGR2GRAY)
        self.previewgray = cv2.resize(self.gray,(256,256))
        
        self.displayGrayscale()
        
    def displayGrayscale(self):
        qFormat = QImage.Format_Indexed8
        if len (self.previewgray.shape) == 3:
            if (self.previewgray.shape[2]) == 4:
                qFormat = QImage.Format_RGBA8888
            else:
                qFormat = QImage.Format_RGB888
        img1 = QImage(self.previewgray, self.previewgray.shape[1], self.previewgray.shape[0], self.previewgray.strides[0], qFormat)
        img1 = img1.rgbSwapped()
        self.labelgrayscale.setPixmap(QPixmap.fromImage(img1))
        self.labelgrayscale.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        
    """def matriksglcm(self):
        self.buttonclasifi.setEnabled(True)
        img = self.previewgray
        varglcm0 = LB.derajat_0(img)
        norm0 = varglcm0.normalisasi_0()
        self.con_0 = LB.contrast_glcm(norm0)
        self.asm_0 = LB.asm_glcm(norm0)
        self.idm_0 = LB.idm_glcm(norm0)
        self.ent_0 = LB.entropi_glcm(norm0)
        self.kor_0 = LB.korelasi_glcm(norm0)
        
        #derajat 45
        varglcm45 = LB.derajat_45(img)
        norm45 = varglcm45.normalisasi_45()
        self.con_45 = LB.contrast_glcm(norm45)
        self.asm_45 = LB.asm_glcm(norm45)
        self.idm_45 = LB.idm_glcm(norm45)
        self.ent_45 = LB.entropi_glcm(norm45)
        self.kor_45 = LB.korelasi_glcm(norm45)
        
        #derajat_90
        varglcm90 = LB.derajat_90(img)
        norm90 = varglcm90.normalisasi_90()
        self.con_90 = LB.contrast_glcm(norm90)
        self.asm_90 = LB.asm_glcm(norm90)
        self.idm_90 = LB.idm_glcm(norm90)
        self.ent_90 = LB.entropi_glcm(norm90)
        self.kor_90 = LB.korelasi_glcm(norm90)
        
        #derajat_135
        varglcm135 = LB.derajat_135(img)
        norm135 = varglcm135.normalisasi_135()
        self.con_135 = LB.contrast_glcm(norm135)
        self.asm_135 = LB.asm_glcm(norm135)
        self.idm_135 = LB.idm_glcm(norm135)
        self.ent_135 = LB.entropi_glcm(norm135)
        self.kor_135 = LB.korelasi_glcm(norm135)
        
        #nampilkan tabel 
        self.hasilGLCM.setRowCount(4)
        self.hasilGLCM.setColumnCount(6)
        self.hasilGLCM.setHorizontalHeaderLabels(['derajat','Contrast','ASM','IDM', 'Entropi', 'Korelasi'])
        self.hasilGLCM.setItem(0,0, QTableWidgetItem("0"))
        self.hasilGLCM.setItem(0,1, QTableWidgetItem(np.array2string(self.con_0)))
        self.hasilGLCM.setItem(0,2, QTableWidgetItem(np.array2string(self.asm_0)))
        self.hasilGLCM.setItem(0,3, QTableWidgetItem(np.array2string(self.idm_0)))
        self.hasilGLCM.setItem(0,4, QTableWidgetItem(np.array2string(self.ent_0)))
        self.hasilGLCM.setItem(0,5, QTableWidgetItem(np.array2string(self.cor_0)))
        
        self.hasilGLCM.setItem(1,0, QTableWidget("45"))
        self.hasilGLCM.setItem(1,1, QTableWidgetItem(np.array2string(self.con_45)))
        self.hasilGLCM.setItem(1,2, QTableWidgetItem(np.array2string(self.asm_45)))
        self.hasilGLCM.setItem(1,3, QTableWidgetItem(np.array2string(self.idm_45)))
        self.hasilGLCM.setItem(1,4, QTableWidgetItem(np.array2string(self.ent_45)))
        self.hasilGLCM.setItem(1,5, QTableWidgetItem(np.array2string(self.cor_45)))
        
        self.hasilGLCM.setItem(2,0, QTableWidget("90"))
        self.hasilGLCM.setItem(2,1, QTableWidgetItem(np.array2string(self.con_90)))
        self.hasilGLCM.setItem(2,2, QTableWidgetItem(np.array2string(self.asm_90)))
        self.hasilGLCM.setItem(2,3, QTableWidgetItem(np.array2string(self.idm_90)))
        self.hasilGLCM.setItem(2,4, QTableWidgetItem(np.array2string(self.ent_90)))
        self.hasilGLCM.setItem(2,5, QTableWidgetItem(np.array2string(self.cor_90)))
        
        self.hasilGLCM.setItem(3,0, QTableWidget("135"))
        self.hasilGLCM.setItem(3,1, QTableWidgetItem(np.array2string(self.con_135)))
        self.hasilGLCM.setItem(3,2, QTableWidgetItem(np.array2string(self.asm_135)))
        self.hasilGLCM.setItem(3,3, QTableWidgetItem(np.array2string(self.idm_135)))
        self.hasilGLCM.setItem(3,4, QTableWidgetItem(np.array2string(self.ent_135)))
        self.hasilGLCM.setItem(3,5, QTableWidgetItem(np.array2string(self.cor_135)))
        
        
        def contrast_glcm(matrix):
            contrast = 0
            for i in range (len(matrix)):
                for j in range (len(matrix)):
                    rumus = ((i-j)**2) * matrix[i][j]
                    contrast += rumus
                return contrast
        def asm_glcm(matrix):
            asm = 0
            for i in range (len(matrix)):
                for j in range (len(matrix)):
                    rumus = matrix[i][j]**2
                    asm += rumus
            return asm 
        def idm_glcm(matrix):
            idm = 0
            for i in range (len(matrix)):
                for j in range(len(matrix)):
                    rumus = (matrix[i][j]) / (1 +(i-j)**2)
                    idm += rumus
            return idm
        
        def entropi_glcm(matrix):
            entropi = 0
            for i in range (len(matrix)):
                for j in range(len(matrix)):
                    if matrix[i][j] != 0:
                        rumus = (-matrix[i][j])* math.log(matrix[i][j])
                        entropi += rumus
                    else:
                        entropi += 0
            return entropi 
        
        def korelasi_glcm(matrix):
            korelasi = 0
            miu_i = 0
            miu_j = 0
            delta_i = 0
            delta_j = 0
            for i in range (len(matrix)):
                for j in range (len(matrix)):
                    miu_i += i * matrix[i][j]
                    miu_j += j * matrix[i][j]
                    
            for i in range (len(matirx)):
                for j in range (len(matrix)):
                    delta_i += matrix[i][j]*((i-miu_i)**2)
                    delta_j += matrix[i][j]*((j-miu_j)**2)
            
            for i in range (len(matrix)):
                for j in range (len(matrix)):
                    korelasi += ((i-miu_i)*(j-miu_j)*(matrix[i][j])) / (math.sqrt((delta_i)*(delta_j)))
                return korelasi
        
        #derajat 0
        class derajat_0:
            def __init__(self,pixel):
                self.pixel = pixel
            def normalisasi_0(self):
                jm_px_0 = np.zeros((256,256))
                for i in range (len(self.pixel)):
                    for j in range (len(self.pixel[i])-1):
                        jm_px_0[self.pixel[i][j]][self.pixel[i][j]] += 1
                        
                    tp_px_0 = jm_px_0.transpose()
                    sim_px_0 = jm_px_0 + tp_px_0
                    
                    total_px_0 = 0
                    for i in range(len(sim_px_0)):
                        for j in range(len(sim_px_0[i])):
                            total_px_0 += sim_px_0[i][j]
                    norm_px_0 = sim_px_0 / total_px_0
                    return norm_px_0
        #derajat 45
        class derjat_45:
            def __init__(self,pixel):
                self.pixel = pixel
            
            def normalisasi_45(self):
                jm_px_45 = np.zeros((256,256))
                for i in range (len(self.pixel) -1):
                    for j in range(len(self.pixel[i]) -1):
                        jm_px_45[self.pixel[i+1][j]][self.pixel[i][j+1]] +=1
                        
                    tp_px_45 = jm_px_45.transpose()
                    sim_px_45 = jm_px_45 + tp_px_45
                    
                    total_px_45 = 0
                    for i in range (len(sim_px_45)):
                        for j in range(len(sim_px_45[i])):
                            total_px_45 += sim_px_45[i][j]
                            
                    norm_px_45 = sim_px_45 / total_px_45
                    return norm_px_45
        #derajat 90
        class derajat_90:
            def __init__(self,pixel):
                self.pixel = pixel
                
            def normalisasi_90(self):
                jm_px_90 = np.zeros((256,256))
                for i in range (len(self.pixel) -1):
                    for j in range(len(self.pixel[i])):
                        jm_px_90[self.pixel[i][j]][self.pixel[i+1][j+1]] += 1
                    
                tp_px_90 = jm_px_90.transpose()
                sim_px_90 = jm_px_90 + tp_px_90
                
                total_px_90 = 0
                for i in range (len(sim_px_90)):
                    for j in range(len(sim_px_90[i])):
                        total_px_90 += sim_px_90[i]+[j]
                
                norm_px_90 = sim_px_90 / total_px_90
                return norm_px_90
        
        #derajat 135
        class derajat_135:
            def __init__(self,pixel):
                self.pixel = pixel
                
            def normalisasi_135(self):
                jm_px_135 = np.zeros((256,256))
                for i in range (len(self.pixel) -1):
                    for j in range (len(self.pixel[i]) -1):
                        jm_px_135[self.pixel[i+1][j+1]][self.pixel[i][j]] += 1
                        
                tp_px_135 = jm_px_135.transpose()
                sim_px_135 = jm_px_135 + tp_px_135
                
                total_px_135 = 0
                for i in range(len(sim_px_135)):
                    for j in range(len(sim_px_135[i])):
                        total_px_135 += sim_px_135[i][j]
                
                norm_px_135 = sim_px_135 / total_px_135
                return norm_px_135
            
        def klasifikasi(self):
             data = pd.read_csv('')
            data.head()
            print(data.Label.value_counts())
            sns.countplot(x="Label", data=data palette="bwr")
            
            lookup_fruit_name = dict()"""
                
                   
                
                
                
                        
       
        
    
app = QApplication(sys.argv)
window = UI()
window.show()
sys.exit(app.exec())
app.exec_()
