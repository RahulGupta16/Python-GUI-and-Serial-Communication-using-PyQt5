
# Final Year Project GUI Window program  script

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import pandas as pd
import matplotlib.pyplot as plt
import serial
import requests
import time, threading
import schedule
from random import randint
from ws4py.client.threadedclient import WebSocketClient

global ard_data
ard_data = serial.Serial('COM5',9600,timeout=10)
#ard_data.close()
#ard_data.open()

#while True:

#    data = ard_data.readline()
#    print(data.decode())
######### GENERATING A CLASS FOR RUNNING THE GUI SCRIPT FROM ANY OTHER SOURCE #########
class window1(QMainWindow):

    ####### CLASS CONSTRUCTOR ALONGWITH Main Window constructor ########

    def __init__(self):
        super(window1,self).__init__()
        self.setGeometry(20,30,1300,650)        # self -> QMainWindow  ,   
        self.setWindowTitle("Simulation Window")      # Title of the main window
        self.UI()
        self.w1 = None
        self.w2 = None
        self.w3 = None
        self.w4 = None
        self.w5 = None
        self.w6 = None
        self.w7 = None
        self.w8 = None
        self.w9 = None
        self.w10 = None




    ####### Contents to be present inside the main window #######

    ## Adding a label in the main window is done as ##

    def UI(self):

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        self.widget.setLayout(self.vbox)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)

        #self.setWindowTitle('Scroll Area Demonstration')
        #self.show()

        #QDialog.createGridLayout()
        #win_lout = QVBoxLayout()
        #win_lout.addWidget(self.horizontalGroupBox)
        


        self.label1 = QtWidgets.QLabel(self)            # set label on main screen
        self.label2 = QtWidgets.QLabel(self)
        self.label3 = QtWidgets.QLabel(self)            
        self.label4 = QtWidgets.QLabel(self)
        self.label6 = QtWidgets.QLabel(self)
        self.label7 = QtWidgets.QLabel(self)
        self.label8 = QtWidgets.QLabel(self)
        self.label9 = QtWidgets.QLabel(self)
        self.label10 = QtWidgets.QLabel(self)
        self.label11 = QtWidgets.QLabel(self)




        #self.prog_bar = QtWidgets.QProgressBar(self)     # Added a progress bar
        #self.prog_bar.setGeometry(200,500,170,22)
       # self.prog_bar.setValue(52)
        #self.prog_bar.move(200,500)


        #self.slide = QtWidgets.QSlider(self)
        #self.slide.setGeometry(430,500,190,22)
        




        self.label1.setText("Water Level Sensor1")            # set text of label to be printed on main e=screen
        self.label1.move(40,40)                          # set location of label to be placed on main screen as move(x_pos,y_pos)
        self.label2.setText("Water Level Sensor2")            
        self.label2.move(370,40)
        self.label3.setText("Water Level Sensor3")            
        self.label3.move(720,40)
        self.label4.setText("Water Level Sensor4")            
        self.label4.move(1000,40)
        
        self.label6.setText("MQ2 Sensor1")
        self.label6.move(40,200)
        self.label7.setText("MQ2 Sensor2")
        self.label7.move(370,200)
        self.label8.setText("MQ2 Sensor3")
        self.label8.move(720,200)
        self.label9.setText("MQ2 Sensor4")
        self.label9.move(1000,200)

        #with serial.Serial('COM5',9600,timeout=5) as ard_data:

            #  statement = ard_data.readline()
            #   decode = str(statement.decode('utf 8'))
        #self.label10.setText(decode)
            # print(decode)
        #schedule.every(2).seconds.do()
        #self.label10.move(710,170)
        
    # self.label5.setText('Refresh the content')
    # self.label5.move(100,240)


    ## Adding push button in the main window is done as ##

        self.push_but1 = QtWidgets.QPushButton(self)          # set push button to be added on main window
        self.push_but1.setText('Click for graph')               # set text to be printed on push button
        self.push_but1.move(40,130)                           # set location of the push button on main window

        self.push_but1.clicked.connect(self.graph1_box)             # Click operation to be done on push button. It is
                                                                # just representing the operation to be done after  
                                                                # clicking the push button

        self.push_but2 = QtWidgets.QPushButton(self)
        self.push_but2.setText('Click for graph')
        self.push_but2.move(370,130)
        self.push_but2.clicked.connect(self.graph2_box)

        self.push_but3 = QtWidgets.QPushButton(self)
        self.push_but3.setText('Click for graph')
        self.push_but3.move(720,130)
        self.push_but3.clicked.connect(self.graph3_box)

        self.push_but4 = QtWidgets.QPushButton(self)
        self.push_but4.setText('Click for graph')
        self.push_but4.move(1000,130)
        self.push_but4.clicked.connect(self.graph4_box)

        self.push_but6 = QtWidgets.QPushButton(self)
        self.push_but6.setText('Click for graph')
        self.push_but6.move(40,300)
        self.push_but6.clicked.connect(self.graph6_box)

        self.push_but7 = QtWidgets.QPushButton(self)
        self.push_but7.setText('Click for graph')
        self.push_but7.move(370,300)
        self.push_but7.clicked.connect(self.graph7_box)

        self.push_but8 = QtWidgets.QPushButton(self)
        self.push_but8.setText('Click for graph')
        self.push_but8.move(720,300)
        self.push_but8.clicked.connect(self.graph8_box)

        self.push_but9 = QtWidgets.QPushButton(self)
        self.push_but9.setText('Click for graph4')
        self.push_but9.move(1000,300)
        self.push_but9.clicked.connect(self.graph9_box)

       # self.push_but10 = QtWidgets.QPushButton(self)
       # self.push_but10.setText('Click for graph')
       # self.push_but10.move(710,250)
       # self.push_but10.clicked.connect(self.graph10_box)

       # self.push_but_r = QtWidgets.QPushButton(self)
       # self.push_but_r.setText('Refresh')
       # self.push_but_r.move(300,350)
       # self.push_but_r.clicked.connect(self.refresh)

      #  self.prog_but_str = QtWidgets.QPushButton(self)
      #  self.prog_but_str.setText('Start')
      #  self.prog_but_str.move(200,280)
      #  self.prog_but_str.clicked.connect(self.start_but)   ### For powering ON the led
    
      #  self.prog_but_res = QtWidgets.QPushButton(self)
      #  self.prog_but_res.setText('Reset')
      #  self.prog_but_res.move(300,280)
      #  self.prog_but_res.clicked.connect(self.reset_but)     # For powering OFF the led



        '''self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append(randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.
        '''





























      #  self.button1 = QtWidgets.QPushButton(self)
      #  self.button1.setText('Print text button')
      #  self.button1.move(250,500)
      #  self.button1.clicked.connect(self.msg_box)

      #  self.graph1 = QtWidgets.QPushButton(self)
      #  self.graph1.setText('Graph 1')
      #  self.graph1.move(300,370)
      #  self.graph1.clicked.connect(self.graph1_box)


        ### Added textbox ###
       # self.textbox1 = QLineEdit(self)    
       # self.textbox1.move(200,490)
       # self.textbox1.resize(200,35)

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
       # self.show()

        desc_button = QAction('About the GUI designer',self)     ## Added description about the gui
        desc_button.triggered.connect(self.desc_button)
        about_menu.addAction(desc_button)
        #self.show()




        self.read = QPushButton("Read", self)
        self.read.clicked.connect(self.read_data)
        self.read.setFixedSize(100, 40)
        self.read.move(400, 490)

        self.clear = QPushButton("Clear", self)
        self.clear.clicked.connect(self.clear_data)
        self.clear.setFixedSize(100, 40)
        self.clear.move(540, 490)

        self.cont =QCheckBox(self)
        self.cont.stateChanged.connect(self.up_1s)
        self.cont.move(500,400)

        self.label14 = QLabel("Water meter 1", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label14.setFont(setFnt)
        self.label14.setFixedSize(300, 45)
        self.label14.move(40,80)

        self.label15 = QLabel("Water meter 2", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label15.setFont(setFnt)
        self.label15.setFixedSize(300, 45)
        self.label15.move(370,80)

        self.label16 = QLabel("Water meter 3", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label16.setFont(setFnt)
        self.label16.setFixedSize(300, 45)
        self.label16.move(720,80)

        self.label17 = QLabel("Water meter 4", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label17.setFont(setFnt)
        self.label17.setFixedSize(300, 45)
        self.label17.move(1000,80)

        self.label19 = QLabel("MQ2 sensor 1", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label19.setFont(setFnt)
        self.label19.setFixedSize(300, 35)
        self.label19.move(40,240)

        self.label20 = QLabel("MQ2 sensor 2", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label20.setFont(setFnt)
        self.label20.setFixedSize(300, 35)
        self.label20.move(370,240)

        self.label21 = QLabel("MQ2 sensor 3", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label21.setFont(setFnt)
        self.label21.setFixedSize(300, 35)
        self.label21.move(720,240)

        self.label22 = QLabel("MQ2 sensor 4", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label22.setFont(setFnt)
        self.label22.setFixedSize(300, 35)
        self.label22.move(1000,240)



        self.TimerTask=None

        










    #global win
    
   # win = pg.plot()
    #x = np.arange(1)
        self.prog_bar1 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar1.setGeometry(200,500,170,52)
        self.prog_bar1.move(170,107)

        self.prog_bar2 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar2.setGeometry(200,500,170,52)
        self.prog_bar2.move(500,107)

        self.prog_bar3 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar3.setGeometry(200,500,170,52)
        self.prog_bar3.move(830,107)

        self.prog_bar4 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar4.setGeometry(200,500,170,52)
        self.prog_bar4.move(1130,107)

        self.prog_bar6 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar6.setGeometry(200,500,170,52)
        self.prog_bar6.move(170,280)

        self.prog_bar7 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar7.setGeometry(200,500,170,52)
        self.prog_bar7.move(500,280)

        self.prog_bar8 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar8.setGeometry(200,500,170,52)
        self.prog_bar8.move(830,280)

        self.prog_bar9 = QtWidgets.QProgressBar(self)     # Added a progress bar
        self.prog_bar9.setGeometry(200,500,170,52)
        self.prog_bar9.move(1130,280)




    def read_data(self):
        global k
        k = ard_data.readline().decode()
        self.label14.setText(k)
        self.prog_bar1.setValue(int(k))
        
        k = ard_data.readline().decode()
        self.label15.setText(k)
        self.prog_bar2.setValue(int(k))

        
        k = ard_data.readline().decode()
        self.label16.setText(k)
        self.prog_bar3.setValue(int(k))
        k = ard_data.readline().decode()
        self.label17.setText(k)
        self.prog_bar4.setValue(int(k))

        k = ard_data.readline().decode()
        self.label19.setText(k)
        self.prog_bar6.setValue(int(k))

        k = ard_data.readline().decode()
        self.label20.setText(k)
        self.prog_bar7.setValue(int(k))

        k = ard_data.readline().decode()
        self.label21.setText(k)
        self.prog_bar8.setValue(int(k))

        #k = ard_data.readline().decode()
        #self.label22.setText(k)
        #return(k)

    def clear_data(self):
        self.label14.clear()
        self.label15.clear()
        self.label16.clear()
        self.label17.clear()
        self.label19.clear()
        self.label20.clear()
        self.label21.clear()


    def up_1s(self,state):
        '''
        Threading
        Continuosly Read data for every 1Sec
        '''

        try:
            if self.TimerTask == None:
                self.TimerTask = QTimer()


            if state == QtCore.Qt.Checked:
                self.TimerTask.timeout.connect(self.read_data)
                self.TimerTask.start(1000)
            else:
                self.TimerTask.stop()
                
            pass

        except(TypeError,ValueError,AttributeError):

            print("Oops!", sys.exc_info()[0], "occured.")
            pass



    

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
        self.label5.setText("You clicked 5")

    def refresh(self):
        self.label1.setText("First Content")
        self.label2.setText("Second Content")
        self.label3.setText("Third Content")
        self.label4.setText("Fourth Content")
        self.label5.setText("Fifth Content")


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
#     ard_data.write(b'1')
        

    def reset_but(self):  
        msg = 'OFF LED ?'
        QMessageBox.question(self,'Message box',msg,QMessageBox.Ok)                     # Event associated with stop
    #    ard_data.write(b'0')
        
    def graph1_box(self, checeked):
        if(self.w1==None):
            self.w1 = another_window1()
        self.w1.show()

    def graph2_box(self, checeked):
        if(self.w2==None):
            self.w2 = another_window2()
        self.w2.show()

    def graph3_box(self, checeked):
        if(self.w3==None):
            self.w3 = another_window3()
        self.w3.show()

    def graph4_box(self, checeked):
        if(self.w4==None):
            self.w4 = another_window4()
        self.w4.show()


    def graph6_box(self, checeked):
        if(self.w6==None):
            self.w6 = another_window6()
        self.w6.show()

    def graph7_box(self, checeked):
        if(self.w7==None):
            self.w7 = another_window7()
        self.w7.show()

    def graph8_box(self, checeked):
        if(self.w8==None):
            self.w8 = another_window8()
        self.w8.show()

    def graph9_box(self, checeked):
        if(self.w9==None):
            self.w9 = another_window9()
        self.w9.show()

    def graph10_box(self, checeked):
        if(self.w10==None):
            self.w10 = another_window10()
        self.w10.show()



class another_window1(QMainWindow):

    def __init__(self):
        super(another_window1,self).__init__()
        #super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,500,300)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout)

    

class another_window2(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window3(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window4(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window5(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.setWindowTitle('Water Level Sensor 1 Graphical Simulation  ')
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window6(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.setWindowTitle('Water Level Sensor 2 Graphical Simulation  ')
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window7(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window8(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

class another_window9(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout)   

class another_window10(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setGeometry(200,200,400,600)
        self.label = QLabel("Graph window")
        layout.addWidget(self.label)
        self.setLayout(layout) 

    
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
  #  MainWindow = QtWidgets.QMainWindow()    
    win = window1()  
  #  win.setupUi(MainWindow)   
  #  MainWindow.show()                
    win.show()  
    sys.exit(app.exec_())                       


   # while True:

    #    data = ard_data.readline()
       # window1.UI.label8.setText(data)
    #    print(data.decode())
                                
