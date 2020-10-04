#######################################################################
##################       Basics of PyQt5        #######################
#################                                ######################
#######################################################################


##### IMPORTED ESSENTIAL LIBRARIES ######

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QLineEdit, QMessageBox, QDialog, QVBoxLayout, QGridLayout
from PyQt5.QtCore import QAbstractTableModel, Qt
import sys
import pandas as pd
import matplotlib.pyplot as plt
import serial

ard_data = serial.Serial('COM5',9600,timeout=1)

#data = pd.read_csv(r'C:\Users\Rahul\Desktop\Kaggle-s-Titanic-survival-prediction\train.csv')

######### GENERATING A CLASS FOR RUNNING THE GUI SCRIPT FROM ANY OTHER SOURCE #########
class window1(QMainWindow):

    ####### CLASS CONSTRUCTOR ALONGWITH Main Window constructor ########

    def __init__(self):
        super(window1,self).__init__()
        self.setGeometry(500,200,700,500)        # self -> QMainWindow  ,   
        self.setWindowTitle("Simulation Window")      # Title of the main window
        self.UI()
        

    ####### Contents to be present inside the main window #######

    ## Adding a label in the main window is done as ##

    def UI(self):

        #QDialog.createGridLayout()
        #win_lout = QVBoxLayout()
        #win_lout.addWidget(self.horizontalGroupBox)



        self.label1 = QtWidgets.QLabel(self)            # set label on main screen
        self.label2 = QtWidgets.QLabel(self)
        self.label3 = QtWidgets.QLabel(self)            
        self.label4 = QtWidgets.QLabel(self)
        self.label5 = QtWidgets.QLabel(self)

        self.prog_bar = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar.setGeometry(200,45,170,22)
        self.prog_bar.setValue(52)
        self.prog_bar.move(200,45)


        self.slide = QtWidgets.QSlider(self)
        self.slide.setGeometry(430,45,190,22)




        self.label1.setText("First content")            # set text of label to be printed on main e=screen
        self.label1.move(7,30)                          # set location of label to be placed on main screen as move(x_pos,y_pos)
        self.label2.setText("Second content")            
        self.label2.move(7,60)
        self.label3.setText("Third content")            
        self.label3.move(7,90)
        self.label4.setText("Fourth content")            
        self.label4.move(7,120)
       # self.label5.setText('Refresh the content')
       # self.label5.move(100,240)


    ## Adding push button in the main window is done as ##

        self.push_but1 = QtWidgets.QPushButton(self)          # set push button to be added on main window
        self.push_but1.setText('Click Button1')               # set text to be printed on push button
        self.push_but1.move(100,30)                           # set location of the push button on main window

        self.push_but1.clicked.connect(self.event1)             # Click operation to be done on push button. It is
                                                                # just representing the operation to be done after  
                                                                # clicking the push button

        self.push_but2 = QtWidgets.QPushButton(self)
        self.push_but2.setText('Click Button2')
        self.push_but2.move(100,60)
        self.push_but2.clicked.connect(self.event2)

        self.push_but3 = QtWidgets.QPushButton(self)
        self.push_but3.setText('Click Button3')
        self.push_but3.move(100,90)
        self.push_but3.clicked.connect(self.event3)

        self.push_but4 = QtWidgets.QPushButton(self)
        self.push_but4.setText('Click Button4')
        self.push_but4.move(100,120)
        self.push_but4.clicked.connect(self.event4)

        self.push_but5 = QtWidgets.QPushButton(self)
        self.push_but5.setText('Refresh')
        self.push_but5.move(200,240)
        self.push_but5.clicked.connect(self.event5)

        self.prog_but_str = QtWidgets.QPushButton(self)
        self.prog_but_str.setText('Start')
        self.prog_but_str.move(200,280)
        self.prog_but_str.clicked.connect(self.start_but)   ### For powering ON the led
    
        self.prog_but_res = QtWidgets.QPushButton(self)
        self.prog_but_res.setText('Reset')
        self.prog_but_res.move(300,280)
        self.prog_but_res.clicked.connect(self.reset_but)     # For powering OFF the led


        self.button1 = QtWidgets.QPushButton(self)
        self.button1.setText('Print text button')
        self.button1.move(200,200)
        self.button1.clicked.connect(self.msg_box)


        ### Added textbox ###
        self.textbox1 = QLineEdit(self)    
        self.textbox1.move(200,90)
        self.textbox1.resize(200,35)

        #### Setting main menu ###
        main_menu = self.menuBar()
        file_menu = main_menu.addMenu('File')
        edit_menu = main_menu.addMenu('Edit')
        view_menu = main_menu.addMenu('View')
        help_menu = main_menu.addMenu('Help')
        about_menu = main_menu.addMenu('About')

        exit_button = QAction('Exit',self)
        exit_button.triggered.connect(self.close)
        file_menu.addAction(exit_button)
        self.show()

        desc_button = QAction('About the GUI designer',self)     ## Added description about the gui
        desc_button.triggered.connect(self.desc_button)
        about_menu.addAction(desc_button)
        self.show()

    ### Added events for click operations ###

    def event1(self):                                 # Specific function of event to be done after 
        self.label1.setText("You clicked 1")          # clicking the push button

    def event2(self):
        self.label2.setText("You clicked 2")
    
    def event3(self):
        self.label3.setText("You clicked 3")

    def event4(self):
        self.label4.setText("You clicked 4")

    def event5(self):
        self.label1.setText("First Content")
        self.label2.setText("Second Content")
        self.label3.setText("Third Content")
        self.label4.setText("Fourth Content")

    def button1_event(self):                   ## Event associated with button1 (printing the content of textbox) 
        print('Button1 clicked!!')

    def msg_box(self):                      ## Event associated with printing a message box 
        msg = self.textbox1.text()          ## Storing the text present inside the text box into 'msg' variable
        print(type(msg))
        QMessageBox.question(self,'Message box',msg,QMessageBox.Ok,QMessageBox.Cancel)      ## Displaying message box alogwith a message and with some buttons
        self.textbox1.setText("")           ## Reseting the textbox after printing the message
    
    def desc_button(self):
        msg = 'This GUI is designed for displaying the sensor values and providing graphical representation. Project is designed by Rahul alogwith Namira and Nishant for implementing their final year project'
        QMessageBox.question(self,'About the GUI designer',msg,QMessageBox.Ok)

    def start_but(self): 
        msg = 'ON LED ?'
        QMessageBox.question(self,'Message box',msg,QMessageBox.Ok)                   # Event associated with start
        ard_data.write(b'1')
        

    def reset_but(self):  
        msg = 'OFF LED ?'
        QMessageBox.question(self,'Message box',msg,QMessageBox.Ok)                     # Event associated with stop
        ard_data.write(b'0')
        


    
 # def grid_method(self):
 #       self.hortizontalGroupBox = QGroupBox('Grid')
 #       layout = QGridLayout
 #       layout.setColumnStretch(1,4)
 #      layout.setColumnStretch(2,4)
 #      layout.addWidget(QPushButton)
 #       layout.addWidget(QPushButton('Ok'),0,0)

        
        
#def display():
#    app = QApplication(sys.argv)
#    win = window1()                         
#    win.show()                                  
#    sys.exit(app.exec_())                       

#display()



if(__name__=='__main__'):
    app = QApplication(sys.argv)
    win = window1()                         
    win.show()                                  
    sys.exit(app.exec_())                       
